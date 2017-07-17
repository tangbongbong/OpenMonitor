from multiprocessing.dummy import Pool as ThreadPool
from common import constant
import logging
import time


class DataDispatcher:
    pool = ThreadPool(constant.THREAD_POOL_SIZE)

    def __init__(self, data_loaders):
        self.data_loaders = data_loaders

    def dispatch(self):
        self.pool.map(self.__dispatch__, self.data_loaders)

    def __dispatch__(self, data_loader):
        data_loader.before_load()

        data = self.__load_data__(data_loader.load, data_loader.name)
        map_data = self.__map_data__(data)
        self.__persist_data__(map_data)

        data_loader.after_load()

    def __load_data__(self, load_func, loader_name):
        start_time = time.time()
        data = load_func()
        elapsed_time = time.time() - start_time
        logging.info("Load data time: %d ms , loader: %s" % (elapsed_time, loader_name))
        return data

    def __map_data__(self, data):
        logging.info(data)
        pass

    def __persist_data__(self, data):
        pass
