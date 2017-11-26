import json
import psutil

from core.AbstractDataLoader import AbstractDataLoader


class senors_info(AbstractDataLoader):
    def __init__(self):
        AbstractDataLoader.__init__(self, __name__)

    def load(self):
        AbstractDataLoader.load(self)
        jsonData = {}
        jsonData['sensors_temp'] = psutil.sensors_temperatures()
        jsonData['sensors_fans'] = psutil.sensors_fans()
        return json.dumps(jsonData)

    def before_load(self):
        AbstractDataLoader.before_load(self)

    def after_load(self):
        AbstractDataLoader.after_load(self)
