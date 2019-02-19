#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired])
    remenber_me = BooleanField('renmener_me', default=False)










