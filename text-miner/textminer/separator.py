import re


def words(string):
    string = string.split()
    match = [word for word in string if re.match(r'^\w*\-?[a-z]+$', word)]
    if match != []:
        return match
    else:
        return None


def phone_number(string):
    phone_numbers = {}
    try:
        results = re.search(r"\(?([0-9]{3})\)?\.?\s?-?([0-9]{3})\-?\.?([0-9]{4})", string).groups()
        phone_numbers["area_code"] = results[0]
        phone_numbers["number"] = '-'.join(results[1:])
        return phone_numbers
    except AttributeError:
        return None


def money(string):
    cash_money = {}
    try:
        groups = re.search(r"(^\$)((?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$)", string).groups()
        cash_money['currency'] = groups[0]
        amount = groups[1].replace(',', '')
        cash_money['amount'] = float(amount)
        return cash_money
    except AttributeError:
        return None


def zipcode(string):
    zipcode = {}
    try:
        match = re.match(r"^(\d{5})\-?(\d{4})?$", string).groups()
        zipcode["zip"] = match[0]
        if match[1]:
            zipcode["plus4"] = match[1]
        else:
            zipcode["plus4"] = None
        return zipcode
    except AttributeError:
        return None


def date(string):
    dates = {}
    try:
        match = re.match(r"(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})", string).groups()
        if len(match[0]) < 4:
            dates["month"] = int(match[0].lstrip('0'))
            dates["day"] = int(match[1].lstrip('0'))
            dates["year"] = int(match[2])
        else:
            dates["year"] = int(match[0])
            dates["month"] = int(match[1].lstrip('0'))
            dates["day"] = int(match[2].lstrip('0'))
        return dates
    except AttributeError:
        return None


def email(string):
    email = {}
    try:
        match = re.search(r"([a-z0-9.]+)@([a-z]+\.[a-z]{2,4})", string).groups()
        email["local"] = match[0]
        email["domain"] = match[1]
        return email
    except AttributeError:
        return None


def address(string):
    address = {}
    try:
        match = re.search(r"(\d+[\w\s]+)[\n,]([\w\s]+), ([A-Z]{2}) (\d{5})\-?(\d{4})?", string).groups()
        address["address"] = match[0]
        address["city"] = match[1].strip()
        address["state"] = match[2]
        address["zip"] = match[3]
        if match[4]:
            address["plus4"] = match[4]
        else:
            address["plus4"] = None
        return address
    except AttributeError:
        return None
