from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


# class LoginForm(FlaskForm):
#     name = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Имя*', validators=[DataRequired()])
    surname = StringField('Фамилия')
    email = EmailField('E-mail*', validators=[DataRequired()])
    password = PasswordField('Пароль*', validators=[DataRequired(), Length(min=6)])
    confirm_pas = PasswordField('Подтверждение пароля*', validators=[DataRequired(), EqualTo('password')])
