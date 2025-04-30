import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase



class History(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'history'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    file = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    res_file = sqlalchemy.Column(sqlalchemy.String, nullable=True)
