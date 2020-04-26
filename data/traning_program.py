import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Traning(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'traning_program'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.String)#спортивная категория человека
    duration = sqlalchemy.Column(sqlalchemy.INTEGER)#длительность в днях
    program = sqlalchemy.Column(sqlalchemy.TEXT)#Сама программа