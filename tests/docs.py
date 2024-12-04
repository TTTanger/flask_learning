from flask import Blueprint, render_template

bp = Blueprint("docs", __name__, url_prefix='/docs', template_folder='docs', static_folder='docs')

@bp.route('/')
def docs():
    return render_template('index.html')