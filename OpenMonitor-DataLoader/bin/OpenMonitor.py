import sys
import logging
import threading
import json
from common import constant
from pprint import pprint
from core import DataDispatcher
from core import DataLoaderFactory


def set_log():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def load_conf():
    config_data = json.load(open(constant.CONFIG_FILE_PATH))
    logging.info('Config loaded!')
    return config_data


def fetch_data_loader(config_data):
    data_loaders = config_data[constant.CONFIG_KEY_LOADER]
    return data_loaders


def dispatch(loaders):
    factory = DataLoaderFactory()
    factory.make_loader(loaders)
    dispatcher = DataDispatcher(factory.loader_list)
    dispatcher.dispatch()
    # dispat
    pass


def main():
    set_log()
    logging.info('OpenMonitor is loading....')
    logging.info('load conf ....')
    conf = load_conf()
    logging.info('fetch data loader....')
    loaders = fetch_data_loader(conf)
    logging.info('dispatch ....')
    dispatch(loaders)
    logging.info('OpenMonitor start successful!')


if __name__ == '__main__':
    main()
