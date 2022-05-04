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
