import re


def words(string):
    match = re.findall(r'\b\w*[-]*[a-z]+\b', string)
    if match:
        return


def phone_number(string):
    match = re.match(r'(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?\s*(\d{4})', string)
    if match:
        return


def money(string):
    return re.match(r'^\$(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$', string)


def zipcode(string):
    return re.match(r"^\d{5}(\-?\d{4})?$", string)


def date(string):
    return re.match(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)
