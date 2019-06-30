from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True   # 去掉jinja语句占据的空行和空格
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# flask-oment 集成了Moment.js库，
# 一个用于处理时间和日期的开源javascript库


from sayhello import views, errors, commands
#  为了避免循环依赖， 这些导入语句在构造文件的末尾定义
