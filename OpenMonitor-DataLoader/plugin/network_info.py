import json

import psutil

from core.AbstractDataLoader import AbstractDataLoader


class network_info(AbstractDataLoader):
    def __init__(self):
        AbstractDataLoader.__init__(self, __name__)

    def load(self):
        AbstractDataLoader.load(self)
        jsonData = {}
        jsonData['net_io_counters'] = {
            'byte_sent': psutil.net_io_counters().bytes_sent / 8 / 1024 / 1024,
            'bytes_recv': psutil.net_io_counters().bytes_sent / 8 / 1024 / 1024,
        }

        jsonData['net_if_addrs'] = psutil.net_if_addrs()
        jsonData['net_if_stats'] = psutil.net_if_stats()
        # jsonData['net_connection'] = psutil.net_connections(kind='inet4')
        return json.dumps(jsonData)

    def before_load(self):
        AbstractDataLoader.before_load(self)

    def after_load(self):
        AbstractDataLoader.after_load(self)
