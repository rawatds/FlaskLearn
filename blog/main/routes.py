from flask import Blueprint
from flask import render_template, request
from blog.main.utils import date_format

from blog.models import Post

main_bp = Blueprint('main_bp', __name__)


@main_bp.route("/")
@main_bp.route("/home")
def home():
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('index.html', posts=posts, title="Home", date_format=date_format)


@main_bp.route("/home/<username>")
def homeuser(username):
    # return "<h2><font color='green'>Hello World !!!</font></h2>"
    return render_template('index.html', username=username)


@main_bp.route("/about")
def about():
    return render_template('about.html', title="About")



@main_bp.route("/test")
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

