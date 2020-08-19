from flask import render_template, url_for, flash, redirect #, make_response, request, abort
from blog import app
from blog.forms import LoginForm, RegistrationFrom
#from blog.models import User, Post


posts = [
    {
        'author' : 'Dharmender Rawat',
        'title' : 'Blog # 1',
        'contents' : 'This is my first blog',
        'date_posted' : 'August 16, 2020'
    },
    {
        'author': 'Anil Kumar',
        'title': 'Blog # 2',
        'contents': 'This is my second blog',
        'date_posted': 'August 20, 2020'
    }
]



@app.route("/")
@app.route("/home")
def home():
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    return render_template('index.html', posts=posts, title="Home")


@app.route("/home/<username>")
def homeuser(username):
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    return render_template('index.html', username=username)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    print("Debug:", form.username.data)

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if (form.validate_on_submit()):
        if form.email.data == 'admin@admin.com':
            flash('Login successful', 'success')
            return redirect(url_for('home'))

            # response = make_response( render_template('index.html', username= form.email.data) )
            # response.set_cookie('loggeduser', form.email.data)
            # return response
        else:
            flash('Login failed', 'danger')
            # return abort(401)

    return render_template('login.html', title='Login', form=form)


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
