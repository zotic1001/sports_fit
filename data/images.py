import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase, create_session
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Images(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'images'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    image = sqlalchemy.Column(sqlalchemy.BLOB)
    training_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("traning_program.id"))
    training_program = orm.relation('Traning')
