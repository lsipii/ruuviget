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


def parse_comma_separated_text_list(text: str) -> list:
    """
    Transforms a comma separated text list to a list
    """
    return list(map(lambda l: l.strip(), text.split(",")))
