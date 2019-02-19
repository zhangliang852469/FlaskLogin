#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views, models

app = Flask(__name__) # 初始化一个应用

app.config.from_object('config') # CSRF

db = SQLAlchemy(app)