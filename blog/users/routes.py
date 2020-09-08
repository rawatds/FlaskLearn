from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request,session
from blog import  bcrypt, db
from blog.users.forms import LoginForm, RegistrationForm, UpdateAccountForm,  RequestResetForm, ResetPasswordForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from blog.main.utils import save_picture, send_reset_email,date_format

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))

    form = RegistrationForm()
    print("Debug:", form.username.data)

    if form.validate_on_submit():

        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(form.username.data, form.email.data, hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}! Pls login to continue.', 'success')

        return redirect(url_for('users_bp.login'))
    return render_template('register.html', title='Register', form=form)


@users_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))

    form = LoginForm()

    if (form.validate_on_submit()):

            user = User.query.filter_by(email= form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                session['power-by'] = 'DSRDSRDSR'
                login_user(user, remember=form.rememberme.data)

                redir_url = request.args.get('next')
                print('redir_url:', redir_url)
                return redirect(redir_url) if redir_url else redirect(url_for('main_bp.home'))

                # if form.email.data == 'admin@admin.com':
                #     flash('Login successful', 'success')
                #     return redirect(url_for('home'))

                # response = make_response( render_template('index.html', username= form.email.data) )
                # response.set_cookie('loggeduser', form.email.data)
                # return response
            else:
                flash('Login failed! Please check the email and password combination.', 'danger')
                # return abort(401)

    return render_template('login.html', title='Login', form=form)

@users_bp.route("/logout")
def logout():
    logout_user()
    session.clear()
    session.delete()
    return redirect(url_for('main_bp.home'))


@users_bp.route("/account",  methods=['GET', 'POST'])
@login_required
def account():
    # if not current_user.is_authenticated:
    #     flash('You need to be login first before you can see the Accounts section', 'danger')
    #     return redirect(url_for('login'))

    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn = save_picture(form.picture.data)
            current_user.image_file = picture_fn

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users_bp.account'))

    form.username.data = current_user.username
    form.email.data = current_user.email
    dp = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', dp_url = dp, form=form)


@users_bp.route("/user/posts/<username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()

    posts = Post.query.filter_by(author=user)\
                        .order_by(Post.date_posted.desc())\
                        .paginate(page=page, per_page=5)

    return render_template('user_posts.html', posts=posts, title=username + "'s Post", date_format=date_format, user=user)


@users_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))

    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)

        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users_bp.login'))



    return render_template('reset_request.html', title="Reset Password", form=form)


@users_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))

    user = User.verify_reset_token(token)
    if user is None:
        flash('The token is expired or invalid.', 'warning')
        return redirect(url_for('userbp.reset_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()

        flash('Your password has been updated', 'success')
        return redirect(url_for('userbp.login'))

    return render_template('reset_token.html', title="Reset Password", form=form)

