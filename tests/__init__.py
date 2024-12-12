import os

from flask import Flask, render_template


def page_not_found(e):
    return render_template('blog/notfound.html'), 404

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'instance/test_upload_folder')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        print("Upload_folder is created at: ", UPLOAD_FOLDER)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tests.sqlite'),
        UPLOAD_FOLDER=UPLOAD_FOLDER,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)

    '''Register area'''
    # register the blueprints
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    from . import docsify
    app.register_blueprint(docsify.bp)
    app.add_url_rule('/', endpoint='index')

    # register 404
    app.register_error_handler(404, page_not_found)

    return app