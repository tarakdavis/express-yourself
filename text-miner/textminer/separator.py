import re


def words(string):
    string = string.split()
    match = [word for word in string if re.match(r'^\w*\-?[a-z]*$', word)]
    if match != []:
        return match
    else:
        return None


def phone_number(string):
    match = re.match(r'(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?\s*(\d{4})', string)
    if match:
        return
    else:
        return None


def money(string):
    match = re.match(r'^\$(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$', string)
    if match:
        return
    else:
        return None


def zipcode(string):
    match = re.match(r"^\d{5}(\-?\d{4})?$", string)
    if match:
        return
    else:
        return None


def date(string):
    match = re.match(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)
    if match:
        return
    else:
        return None
