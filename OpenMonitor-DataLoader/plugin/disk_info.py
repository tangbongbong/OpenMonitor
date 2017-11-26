import json

import psutil

from core.AbstractDataLoader import AbstractDataLoader


class disk_info(AbstractDataLoader):
    def __init__(self):
        AbstractDataLoader.__init__(self, __name__)

    def load(self):
        AbstractDataLoader.load(self)
        jsonData = {}
        jsonData['disk_usage'] = psutil.disk_usage('/').percent
        jsonData['disk_partitions'] = psutil.disk_partitions()
        return json.dumps(jsonData)

    def before_load(self):
        AbstractDataLoader.before_load(self)

    def after_load(self):
        AbstractDataLoader.after_load(self)
