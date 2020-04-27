from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, Form


class TraningForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    program = TextAreaField("Содержание")
    category = SelectField("Для кого эта программа", validators=[DataRequired()],
                           choices=[("MN", "Man Normal-weight"), ("MF", "Man fat-weight"),
                                    ("MVF", "Man very fat weight"), ("MT", "Man thin weight"),
                                    ("MVT", "Men very-thin weight"), ("FN", "Women normal-weight"),
                                    ("FVF", "Woman very fat weight"), ("FF", "Woman fat weight"),
                                    ("FVT", "Woman very thin"), ("FT", "Woman thin")], coerce=str)
    duration = IntegerField("Длительность программы в днях", validators=[DataRequired()])
    submit = SubmitField('Применить')