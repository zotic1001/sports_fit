from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ChangeForm(FlaskForm):  # форма изменения параметров пользователя
    weight = StringField("Ваш вес", validators=[DataRequired()])
    height = StringField("Ваш рост", validators=[DataRequired()])
    age = StringField("Ваш возраст", validators=[DataRequired()])
    need = SelectField("Цель занятий спортом", coerce=str, choices=[("LW", 'Похудеть'), ("MW", 'Поддерживать вес'),
                                                                    ("GW", "Набрать массу")])
    submit = SubmitField('Подтвердить')
