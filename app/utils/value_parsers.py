def parse_comma_separated_text_list(text: str) -> list:
    """
    Transforms a comma separated text list to a list
    """
    parts = []

    # Collect comma separated but only when not in between ()-groups
    if text.find(",") > -1:
        partsSplit = text.split(",")
        collector = None
        for splitter in partsSplit:
            if collector is not None:
                splitter = f"{collector},{splitter}"
                if splitter.count("(") != splitter.count(")"):
                    collector = splitter
                else:
                    parts.append(splitter)
                    collector = None
            elif splitter.count("(") != splitter.count(")"):
                collector = splitter
            else:
                parts.append(splitter)
    else:
        parts.append(text)

    return list(map(lambda part: clean_text_of_hipsus(part), parts))


def parse_boolean(value: str) -> bool:
    """
    Ensures a boolean
    """
    if isinstance(value, bool):
        return value
    elif isinstance(value, str):
        return value.lower() in ("yes", "true", "tru", "t", "1")
    elif isinstance(value, int):
        return value == 1
    return False


def parse_tuple(tuple_value, default_value=None) -> tuple:
    """
    Parses a tuple
    """
    if isinstance(tuple_value, tuple):
        return tuple_value
    elif isinstance(tuple_value, list) and len(tuple_value) == 2:
        return (tuple_value[0], tuple_value[1])
    elif isinstance(tuple_value, str):
        cleared_value = tuple_value.removeprefix("[").removesuffix("]").removeprefix("(").removesuffix(")")
        parts = parse_comma_separated_text_list(cleared_value)
        return parse_tuple(parts, default_value)
    return default_value


def ensure_type(value, value_type):
    value_pattern = str(value_type).removeprefix("<class '").removesuffix("'>")
    match value_pattern:
        case "str":
            value = str(value)
        case "tuple":
            value = parse_tuple(value)
        case "bool":
            value = parse_boolean(value)
    return value


def clean_text_of_hipsus(text: str) -> str:
    return text.strip().removeprefix("'").removesuffix("'").removeprefix('"').removesuffix('"')
