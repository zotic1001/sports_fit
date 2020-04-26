import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase, create_session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    age = sqlalchemy.Column(sqlalchemy.Integer)#возраст
    height = sqlalchemy.Column(sqlalchemy.Integer)#рост в см
    weight = sqlalchemy.Column(sqlalchemy.Integer)#вес в кг
    gender = sqlalchemy.Column(sqlalchemy.String)#пол
    need = sqlalchemy.Column(sqlalchemy.String)#цель занятий
    body_type = sqlalchemy.Column(sqlalchemy.INTEGER)#Телосложение

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    def update_weight(self, weight, session):
        self.weight = weight
        session.commit()
    def update_height(self, height, session):
        self.height = height
        session.commit()
    def update_age(self, age, session):
        self.age = age
        session.commit()
    def update_need(self, need, session):
        self.need = need
        session.commit()
