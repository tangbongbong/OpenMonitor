import json

import psutil

from core.AbstractDataLoader import AbstractDataLoader


class memory_info(AbstractDataLoader):
    def __init__(self):
        AbstractDataLoader.__init__(self, __name__)

    def load(self):
        AbstractDataLoader.load(self)
        jsonData = {}
        jsonData['memory_virtual'] = psutil.virtual_memory().percent
        jsonData['memory_swap'] = psutil.swap_memory().percent
        return json.dumps(jsonData)

    def before_load(self):
        AbstractDataLoader.before_load(self)

    def after_load(self):
        AbstractDataLoader.after_load(self)
