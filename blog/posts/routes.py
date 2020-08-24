from flask import Blueprint
from flask import render_template, url_for, flash, redirect,  abort #, make_response
from blog import db
from blog.posts.forms import PostForm
from blog.models import Post
from flask_login import  current_user, login_required
from blog.main.utils import date_format

posts_bp = Blueprint('posts_bp', __name__)


@posts_bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post is submitted', 'success')
        return redirect(url_for('main_bp.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='Update Post')


@posts_bp.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('post.html', title=post.title, post = post, date_format=date_format)


@posts_bp.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
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
        return redirect(url_for('posts_bp.post', post_id=post.id))

    form.title.data = post.title
    form.content.data = post.contents
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts_bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Posted deleted successfully', 'success')
    return redirect(url_for('main_bp.home'))

