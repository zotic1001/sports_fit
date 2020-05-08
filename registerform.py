from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm): # форма регистрации
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    weight = StringField("Ваш вес", validators=[DataRequired()])
    height = StringField("Ваш рост", validators=[DataRequired()])
    gender = SelectField("Ваш пол", coerce=str, choices=[("M", 'Мужской'), ("F", 'Женский')])
    age = StringField("Ваш возраст", validators=[DataRequired()])
    need = SelectField("Цель занятий спортом", coerce=str, choices=[("LW", 'Похудеть'), ("MW", 'Поддерживать вес'),
                                                                    ("GW", "Набрать массу")])
    body_type = SelectField("Ваше телосложение", coerce=int,
                            choices=[(0, "Обычное"), (-5, "Худощавое"), (5, "Крупное")])
    submit = SubmitField('Войти')
