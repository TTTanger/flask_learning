from flask import Blueprint, render_template

bp = Blueprint("docsify", __name__, url_prefix='/docsify', template_folder='docs', static_folder='docs')

@bp.route('/')
def docs():
    return render_template('index.html')