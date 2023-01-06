"""User Registration and Authentication."""
import os
import imghdr
from time import time
from flask import current_app, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename

from app.auth import auth
from app.auth.models import UserAuth, Profile
from app.auth.forms import LoginForm, RegisterForm
from app.auth.utils import get_avatar, check_permissions


@auth.route('/login', methods=['POST', 'GET'])
def login():
    """Website authentication."""
    form = LoginForm()

    form.next.label.text = ''
    if request.method == 'GET':
        next = request.args.get('next')
        form.next.data = next

    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('main.start'))

    if form.validate_on_submit():

        user = UserAuth.select().where(UserAuth.email == form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = form.next.data
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    """Registration on the site."""
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserAuth.select().where(UserAuth.email == form.email.data).first()
        if user:
            flash(f'User with email: "{form.email.data}" already exists.')
            return redirect(url_for('auth.signup'))

        profile = Profile(avatar=get_avatar(form.email.data.lower()))
        profile.save()
        new_user = UserAuth(name=form.username.data.capitalize(),
                            email=form.email.data,
                            password=form.password.data,
                            role=1,
                            profile=profile.id)
        new_user.save()
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    """User logout."""
    logout_user()
    return redirect(url_for('main.start'))


@auth.route('/profile/<int:user_id>')
@login_required
def show_profile(user_id):
    user = UserAuth.select().where(UserAuth.id == user_id).first()
    if not user:
        abort(404)

    if check_permissions(current_user.id):
        return render_template(
            'auth/profile.html',
            title=f'Profile {user.name}',
            user=user
        )

    if user.id != current_user.id:
        flash('You don\'t have access to this page')
        return redirect(url_for('main.index'))

    return render_template(
        'auth/profile.html',
        title=f'Profile {current_user.name}',
        user=user
    )


@auth.route('/profile/upload/avatar/<int:user_id>', methods=['POST'])
@login_required
def upload_avatar(user_id):
    if not os.path.isdir(current_app.config['UPLOAD_FOLDER']):
        os.mkdir(current_app.config['UPLOAD_FOLDER'])

    if request.method == 'POST':
        user = UserAuth.select().where(UserAuth.id == user_id).first()
        filename = request.files['avatar'].filename
        if filename:
            filename = f'{time()}_{secure_filename(filename)}'
            path_to_file = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            request.files['avatar'].save(path_to_file)
            image_type = imghdr.what(path_to_file)

            if image_type not in current_app.config['ALLOWED_EXTENSIONS']:
                os.remove(path_to_file)
                flash(f'{filename} is not allowed image type')
                return redirect(url_for('auth.show_profile', user_id=user.id))

            url_to_avatar = current_app.config['UPLOAD_URL'] + filename
            profile = Profile.select().where(Profile.id == user.profile.id).first()
            profile.avatar = url_to_avatar
            profile.save()

            flash(f'{filename} uploaded')
            return redirect(url_for('auth.show_profile', user_id=user.id))

    flash('Nothing to upload')
    return redirect(url_for('auth.show_profile', user_id=user.id))
