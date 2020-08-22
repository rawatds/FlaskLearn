from flask import render_template, url_for, flash, redirect, request, abort #, make_response
from blog import app, bcrypt, db
from blog.forms import LoginForm, RegistrationForm, UpdateAccountForm, PostForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
import datetime , pytz
from dateutil.tz import tzlocal


def date_format(mydate):
    mydate = mydate.replace(tzinfo=pytz.UTC)

    # Convert UTC to localtimezone, and then format it
    mydate = mydate.replace(tzinfo=pytz.UTC)

    #return mydate.astimezone(pytz.timezone('UTC')).astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')
    #return mydate.tz=pytz.UTC).astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')
    return mydate.astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')

# posts = [
#     {
#         'author' : 'Dharmender Rawat',
#         'title' : 'Blog # 1',
#         'contents' : 'This is my first blog',
#         'date_posted' : 'August 16, 2020'
#     },
#     {
#         'author': 'Anil Kumar',
#         'title': 'Blog # 2',
#         'contents': 'This is my second blog',
#         'date_posted': 'August 20, 2020'
#     }
# ]

@app.route("/")
@app.route("/home")
def home():
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title="Home", date_format=date_format)


@app.route("/home/<username>")
def homeuser(username):
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    return render_template('index.html', username=username)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    print("Debug:", form.username.data)

    if form.validate_on_submit():

        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(form.username.data, form.email.data, hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}! Pls login to continue.', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if (form.validate_on_submit()):

            user = User.query.filter_by(email= form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.rememberme.data)

                redir_url = request.args.get('next')
                print('redir_url:', redir_url)
                return redirect(redir_url) if redir_url else redirect(url_for('home'))

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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    #form_picture.save(picture_path)
    i.save(picture_path)
    return picture_fn


@app.route("/account",  methods=['GET', 'POST'])
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
        return redirect(url_for('account'))

    form.username.data = current_user.username
    form.email.data = current_user.email
    dp = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', dp_url = dp, form=form)

@app.route("/login2")
def login2():
    return render_template('login2.html')
    # loggeduser = request.cookies.get("loggeduser")
    # return "<h2>Hello " + loggeduser + "</h2>"


@app.route("/test")
def test():
    return """
        <head>
          <title>Test Page</title>
          <link href="../static/site.css" rel="stylesheet">
        </head>

        <body>

          <div id="main">
          <h1>Welcome to Test page</h1>
          <h2>The whole contents of this page are created using triple-quote string</h2>

          <p>Pages (HTML)</p>
          <p>Style Sheets (CSS)</p>
          <p>Computer Code (JavaScript)</p>
          <p>Live Data (Files and Databases)</p>
          </div>

        </body>
    """

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post is submitted', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('post.html', title=post.title, post = post, date_format=date_format)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Only the user who created the post can edit it
    if post.author != current_user:
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.contents = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))

    form.title.data = post.title
    form.content.data = post.contents
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Posted deleted successfully', 'success')
    return redirect(url_for('home'))
