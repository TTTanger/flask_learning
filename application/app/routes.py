from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy 

main = Blueprint('main', __name__)

# db = SQLAlchemy(main)
# main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(main.root_path, 'data.db') # sqlite:////数据库文件的绝对地址

# 以后改成在线数据库
users = {
    "admin": generate_password_hash("admin")
}


# @main.context_processor
# def inject_user():
#     user = User.query.first()
#     return dict(user=user)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@main.route('/')
def home():
    if 'username' in session:
        return render_template("index.html", title="Home", name=session['username'])
    return redirect(url_for('login'))
