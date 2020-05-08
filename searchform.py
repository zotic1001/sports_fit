from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, Form


class SearchForm(FlaskForm):  # форма поиска по программам тренировок
    category = SelectField("Для кого эта программа",
                           choices=[("MN", "Мужчина нормального веса"), ("MF", "Мужчина полный"),
                                    ("MVF", "Мужчина очень полный"), ("MT", "Мужчина худой"),
                                    ("MVT", "Мужчина очень худой"), ("FN", "Женщина нормального веса"),
                                    ("FVF", "Женщина очень полная"), ("FF", "Женщина полная"),
                                    ("FVT", "Женщина очень худая"), ("FT", "Женщина худая"),
                                    ("ALL", "Все категории")], coerce=str)
    duration = StringField("Длительность программы в днях")
    submit = SubmitField('Поиск')