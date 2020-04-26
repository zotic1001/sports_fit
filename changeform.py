from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user

class ChangeForm(FlaskForm):
    weight = StringField("Ваш вес", validators=[DataRequired()])
    height = StringField("Ваш рост", validators=[DataRequired()])
    age = StringField("Ваш возраст", validators=[DataRequired()])
    need = SelectField("Цель занятий спортом", coerce=str, choices=[("LW", 'Похудеть'), ("MW", 'Поддерживать вес'),
                                                                    ("GW", "Набрать массу")])
    submit = SubmitField('Подтвердить')
