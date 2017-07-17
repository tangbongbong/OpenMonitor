from importlib import import_module

class DataLoaderFactory:
    loader_list = []

    def make_loader(self, loader_names):
        for loader in loader_names:
            target_loader = self.__get_class__(loader)
            self.loader_list.append(target_loader)

    def __get_class__(self, kls):
        class_name = kls.split('.')[1]
        m = import_module(kls)
        class_ = getattr(m, class_name)
        return class_()
