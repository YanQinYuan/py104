# 关于表单的类
from flask_wtf import form
from flask_wtf import stringField,PasswordField
from wtforms.validators import DataRequired,Email

class EmailPasswordform(Form):
    email = stringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
