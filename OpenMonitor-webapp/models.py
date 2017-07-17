from sqlalchemy import Column, Integer, String, TEXT, DATETIME
from database import Base
from marshmallow import Schema, fields, post_load


# Create your models here.

class Sample(Base):
    __tablename__ = 'SAMPLE'
    id = Column(Integer, primary_key=True)
    data = Column(TEXT)
    load_time = Column(DATETIME, index=True)
    loader_name = Column(String(64))

    def __init__(self, data, load_time, loader_name):
        self.data = data
        self.loader_name = loader_name
        self.load_time = load_time

    def __repr__(self):
        return '<Sample %r>' % (self.data)


class SampleSchema(Schema):
    data = fields.Str()
    loader_name = fields.Str()
    load_time = fields.DateTime()

    @post_load
    def make_sample(self, data):
        return Sample(**data)


