# 此文件相当于 class 的 __init__
from flask import Flask

app = Flask(__name__, DEBUG = True # 启动 FLASK 的 DEBUG 模式)
app.config.from_object('config')
app.config.from_pyfile('config.py') # 从 instance 加载配置变量
# 现在通过 app.config["VAR_NAME"] ,我们可以访问对应变量
