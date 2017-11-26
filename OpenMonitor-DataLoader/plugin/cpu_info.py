from core.AbstractDataLoader import AbstractDataLoader
import psutil
import json


class cpu_info(AbstractDataLoader):
    def __init__(self):
        AbstractDataLoader.__init__(self, __name__)

    def load(self):
        AbstractDataLoader.load(self)
        jsonData = {}
        jsonData['cpu_percent'] = psutil.cpu_percent()
        jsonData['cpu_percent_per_cpu'] = psutil.cpu_percent(interval=1, percpu=True)
        jsonData['cpu_count'] = psutil.cpu_count()
        jsonData['cpu_freq_max'] = psutil.cpu_freq().max
        jsonData['cpu_freq_min'] = psutil.cpu_freq().min
        jsonData['cpu_freq_current'] = psutil.cpu_freq().current
        return json.dumps(jsonData)

    def before_load(self):
        AbstractDataLoader.before_load(self)

    def after_load(self):
        AbstractDataLoader.after_load(self)
