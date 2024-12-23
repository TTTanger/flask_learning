import os

from PIL import Image
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flaskr.auth import login_required
from flaskr.db import get_db
# from urllib.parse import unquote


bp = Blueprint('blog', __name__)

def compress_image(image, max_size):
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    if original_width > original_height:
        new_width = max_size
        new_height = int(max_size / aspect_ratio)
    else:
        new_height = max_size
        new_width = int(max_size * aspect_ratio)

    image = image.resize((new_width, new_height), Image.LANCZOS)
    return image

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    files = db.execute(
        'SELECT id, filename, post_id'
        ' FROM file'
    ).fetchall()
    comments = db.execute(
        'SELECT c.id, body, created, speaker_id, username, post_id'
        ' FROM comment c JOIN user u ON c.speaker_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts, comments=comments, files=files)

@bp.route('/<int:post_id>/comment', methods=('GET', 'POST'))
@login_required
def comment(post_id):
    if request.method == 'POST':
        body = request.form['comment']
        db = get_db()
        db.execute(
            'INSERT INTO comment (post_id, body, speaker_id) VALUES (?, ?, ?)',
            (post_id, body, g.user['id'])
        )
        db.commit()
        return redirect(url_for('blog.index'))
    else:
        return redirect(url_for('blog.index'))
    
@bp.route('/<int:post_id>/<int:comment_id>/delete_comment', methods=('POST',))
@login_required
def delete_comment(post_id, comment_id):
    if request.method == 'POST':
        db = get_db()
        db.execute('DELETE FROM comment WHERE id = ? AND post_id = ?', (comment_id, post_id))
        db.commit()
        return redirect(url_for('blog.index'))

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        filepath = None

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        error = None
        
        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print("Uploaded File:", filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                
                if filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}:
                    # Compress the imgs
                    file = Image.open(file)
                    file = compress_image(file, 800)
                else:
                    pass
                file.save(filepath)
            elif file and not allowed_file(file.filename):
                flash("The file is not allowed!")
                return redirect(request.url)
            else:
                filename = None
            db = get_db()
            cursor = db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )

            post_id = cursor.lastrowid

            if filename:
                db.execute(
                    'INSERT INTO file (filename, post_id)'
                    ' VALUES (?, ?)',
                    (filename, post_id)
                )
            db.commit()
            return redirect(url_for('blog.index'))
            
    return render_template('blog/create.html')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/downloads/<name>')
def download_file(name):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        filepath = None
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        error = None
        
        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

                if filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}:
                    # Compress the imgs
                    file = Image.open(file)
                    file = compress_image(file, 800)
                else:
                    pass
                
                file.save(filepath)
            elif file and not allowed_file(file.filename):
                flash("The file is not allowed!")
                return redirect(request.url)
            else:
                filename = None
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.execute(
                'UPDATE file SET filename = ?'
                ' WHERE id = ?',
                (filename, id),
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


@bp.route('/contact')
def contact():
    return render_template('blog/contact.html')
