from importlib import import_module


class DataLoaderFactory:
    def make_loader(self, loader_names):
        loader_list = []
        for loader in loader_names:
            target_loader = self.__get_class__(loader)
            loader_list.append(target_loader)
        return loader_list

    def __get_class__(self, kls):
        class_name = kls.split('.')[1]
        m = import_module(kls)
        class_ = getattr(m, class_name)
        return class_()
