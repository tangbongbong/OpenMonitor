from flask import Flask
from flask import request
from database import init_db
from database import db_session
from datetime import datetime,timedelta
from flask import render_template
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


@app.route('/sample/query', methods=['POST'])
def get_sample():
    loader = request.form.get('loader_name')
    time_delta = int(request.form.get('time_delta'))
    end_time = datetime.now()
    start_time = end_time - timedelta(seconds=time_delta)
    samples = []
    for sample in db_session.query(models.Sample).filter(models.Sample.loader_name == loader) \
        .filter(models.Sample.load_time >= start_time, models.Sample.load_time <= end_time):
        samples.append(sample)
    return sample_schema.dumps(samples, many=True).data


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
