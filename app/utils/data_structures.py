def singleton(class_):
    """
    Class decorator
    @see: https://stackoverflow.com/q/6760685
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class dotdict(dict):
    """
    @see: https://stackoverflow.com/a/23689767
    dot.notation access to dictionary attributes
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
