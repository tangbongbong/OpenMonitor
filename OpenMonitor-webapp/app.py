from flask import Flask
from flask import request
from database import init_db
from database import db_session
import models

app = Flask(__name__)
init_db()

sample_schema = models.SampleSchema()


@app.route('/sample/add', methods=['POST'])
def add_sample():
    sample = sample_schema.loads(request.data.decode("utf-8"))
    db_session.add(sample.data)
    db_session.commit()
    return "OK"
