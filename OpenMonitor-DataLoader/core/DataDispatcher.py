import logging
import time
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import schedule

from common import constant


class DataDispatcher:
    pool = ThreadPool(constant.THREAD_POOL_SIZE)

    def __init__(self, data_loaders):
        self.data_loaders = data_loaders

    def dispatch(self):
        schedule.every(2).seconds.do(self.__cycle_dispatch__)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def exit(self):
        schedule.cancel_job(self.__cycle_dispatch__)

    def __cycle_dispatch__(self):
        self.pool.map(self.__dispatch__, self.data_loaders)

    def __dispatch__(self, data_loader):
        data_loader.before_load()

        data = self.__load_data__(data_loader.load, data_loader.name)
        map_data = self.__map_data__(data_loader, data)
        self.__persist_data__(map_data)

        data_loader.after_load()

    def __load_data__(self, load_func, loader_name):
        start_time = time.time()
        data = load_func()
        elapsed_time = time.time() - start_time
        logging.info("Load data time: %d ms , loader: %s" % (elapsed_time, loader_name))
        return data

    def __map_data__(self, data_loader, data):
        logging.info(data)
        return {
            "data": data,
            "plugin": data_loader.name,
            "time": time.time()
        }

    def __persist_data__(self, data):
        r = requests.post(constant.CONFIG_URL, data=data)
        logging.info("post data %s, status:%s, reason:%s" % (json.dumps(data), r.status_code, r.reason))
