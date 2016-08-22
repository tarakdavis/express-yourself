import re


def binary(string):
    return re.match(r'[01]', string)


def binary_even(string):
    return re.match(r'^[01]+0$', string)


def hex(string):
    return re.match(r'^[0-9A-F]+$', string)


def word(string):
    return re.match(r'^\w*[-]*[a-z]+$', string)


def words(string, count=None):
    match = re.findall(r'\b\w*[-]*[a-z]+\b', string)
    if count and match:
        return len(match) == count
    return bool(match)


def phone_number(string):
    return re.match(r'(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?\s*(\d{4})', string)


def money(string):
    return re.match(r'^\$(?:0|[0-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$', string)


def zipcode(string):
    return re.match(r"^\d{5}(\-?\d{4})?$", string)


def date(string):
    return re.match(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)
