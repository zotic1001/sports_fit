from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class TraningForm(FlaskForm):  # форма добавления программыв тренировок
    title = StringField('Заголовок', validators=[DataRequired()])
    program = TextAreaField("Содержание")
    category = SelectField("Для кого эта программа", validators=[DataRequired()],
                           choices=[("MN", "Мужчина нормального веса"), ("MF", "Мужчина полный"),
                                    ("MVF", "Мужчина очень полный"), ("MT", "Мужчина худой"),
                                    ("MVT", "Мужчина очень худой"), ("FN", "Женщина нормального веса"),
                                    ("FVF", "Женщина очень полная"), ("FF", "Женщина полная"),
                                    ("FVT", "Женщина очень худая"), ("FT", "Женщина худая")], coerce=str)
    duration = IntegerField("Длительность программы в днях", validators=[DataRequired()])
    submit = SubmitField('Применить')