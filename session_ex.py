from flask import Flask, request,  url_for, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123abc"
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route("/")
def home():
    return "<h1>Welcome</h1>" \
            "<a href='/login'>Login</a> | " \
            "<a href='/user'>User</a>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if "username" in session:
            return redirect(url_for('user'))
        return "<form method='post' action=''>" \
            "<input type='text' name='username'> " \
            "<input type='submit'> " \
            "</form>"
    else:
        session.permanent = True
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))


@app.route("/user")
def user():
    if 'username' in session:
        return f"<h2>Hello {session['username']}</h2>" \
            "<p><a href='/logout'>Logout</a></p>"
    else:
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)