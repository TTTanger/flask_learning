from flask import Flask
from .models import init_db
import os

def create_app():
    # 获取路径
    basedir = os.path.abspath(os.path.dirname(__file__))
    real_template_folder=os.path.join(basedir, '..', 'templates')
    real_static_folder=os.path.join(basedir, '..', 'static')
    # 实例化 Flask 应用，并指定模板文件夹的位置
    app = Flask(__name__, template_folder=real_template_folder, static_folder=real_static_folder)
    
    # 用于保持会话安全
    app.secret_key = 'tanger1023'  

    # 配置数据库
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')

    # 初始化数据库
    init_db(app)

    # 注册蓝图
    from .routes import main
    app.register_blueprint(main)

    return app