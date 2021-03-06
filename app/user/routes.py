from app import db
from app.helpers import page_title, admin_required
from app.models import User, Role
from app.user import bp
from app.user.forms import CreateUserForm, EditProfileForm, SettingsForm, PasswordOnlyForm
from app.user.helpers import gen_role_choices
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from werkzeug import check_password_hash

no_perm_url = "index"

@bp.route("/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template("user/profile.html", user=user, title=page_title("View User '%s'" % user.username))

@bp.route("/<username>/edit", methods=["GET", "POST"])
@login_required
def edit(username):
    # TODO: make a custom decorator for this?
    if current_user.has_admin_role() or current_user.username == username:
        form = EditProfileForm()

        if current_user.has_admin_role():
            form.roles.choices = gen_role_choices()
        else:
            del form.roles

        user = User.query.filter_by(username=username).first_or_404()

        if form.validate_on_submit():
            user.about = form.about.data

            if(form.password.data):
                user.set_password(form.password.data)

                if current_user.username == user.username:
                    user.must_change_password = False
                elif current_user.has_admin_role():
                    # user must reset password after it has been changed by an admin
                    user.must_change_password = True

            if current_user.has_admin_role():
                new_user_roles = Role.query.filter(Role.id.in_(form.roles.data)).all()

                admin_role = Role.query.get(1)

                if username == current_user.username and current_user.has_admin_role() and admin_role not in new_user_roles:
                    new_user_roles.append(admin_role)
                    flash("You can't revoke your own admin role.", "danger")

                if user.id == 1 and admin_role not in new_user_roles:
                    new_user_roles.append(admin_role)
                    flash("The original admin can't be removed.", "danger")

                user.roles = new_user_roles

            db.session.commit()
            flash("Your changes have been saved.", "success")

            return redirect(url_for("user.profile", username=username))
        elif request.method == "GET":
            form.about.data = user.about

            if current_user.has_admin_role():
                user_roles = []
                for role in user.roles:
                    user_roles.append(str(role.id))

                form.roles.data = user_roles

        return render_template("user/edit.html", form=form, user=user, title=page_title("Edit User '%s'" % user.username))
    else:
        flash("You dont have the neccessary role to perform this action.", "danger")
        return redirect(url_for(no_perm_url))

@bp.route("/create", methods=["GET", "POST"])
@login_required
@admin_required(no_perm_url)
def create():
    form = CreateUserForm()

    form.roles.choices = gen_role_choices()

    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)

        new_user_roles = Role.query.filter(Role.id.in_(form.roles.data)).all()
        new_user.roles = new_user_roles

        new_user.created = datetime.utcnow()

        db.session.add(new_user)
        db.session.commit()

        flash("New user " + new_user.username + " created.", "success")
        return redirect(url_for('user.profile', username=new_user.username))
    else:
        return render_template("user/create.html", form=form, title=page_title("Add User"))

@bp.route("/password", methods=["GET", "POST"])
@login_required
def password():
    form = PasswordOnlyForm()

    if form.validate_on_submit():
        if check_password_hash(current_user.password_hash, form.password.data):
            flash("You must choose a different password.", "danger")
        else:
            current_user.set_password(form.password.data)
            current_user.must_change_password = False
            flash("Password was changed.", "success")

        db.session.commit()

        return redirect(url_for('index'))

    return render_template("user/password.html", form=form, title=page_title("Change Password"))

@bp.route("/list")
@login_required
@admin_required(no_perm_url)
def list():
    users = User.query.all()

    return render_template("user/list.html", users=users, title=page_title("User List"))

@bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    form = SettingsForm()

    if form.validate_on_submit():
        current_user.dateformat = form.dateformat.data
        current_user.editor_height = form.editor_height.data
        current_user.use_direct_links = form.use_direct_links.data
        current_user.use_embedded_images = form.use_embedded_images.data
        current_user.markdown_phb_style = form.markdown_phb_style.data
        current_user.quicklinks = form.quicklinks.data

        flash("Settings changed.", "success")

        db.session.commit()
    elif request.method == "GET":
        form.dateformat.data = current_user.dateformat
        form.editor_height.data = current_user.editor_height
        form.use_direct_links.data = current_user.use_direct_links
        form.use_embedded_images.data = current_user.use_embedded_images
        form.markdown_phb_style.data = current_user.markdown_phb_style
        form.quicklinks.data = current_user.quicklinks

    return render_template("user/settings.html", form=form, title=page_title("User Settings"))