from abc import ABC, abstractmethod
import logging


class AbstractDataLoader(ABC):
    def __init__(self, loader_name):
        self.name = loader_name

    @abstractmethod
    def load(self):
        logging.info("Loading data from %s", self.name)

    @abstractmethod
    def before_load(self):
        logging.info("Before loading data from %s", self.name)

    @abstractmethod
    def after_load(self):
        logging.info("After loading data from %s", self.name)
