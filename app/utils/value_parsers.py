def parse_comma_separated_text_list(text: str) -> list:
    """
    Transforms a comma separated text list to a list
    """
    return list(map(lambda l: l.strip(), text.split(",")))


def parse_boolean(value: str) -> bool:
    """
    Ensures a boolean
    """
    if isinstance(value, bool):
        return value
    elif isinstance(value, str):
        return value.lower() in ("yes", "true", "t", "1")
    elif isinstance(value, int):
        return value == 1
    return False
