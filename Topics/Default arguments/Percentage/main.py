def get_percentage(number, ndigits=None):

    x = number * 100
    result = str(round(x, ndigits)) + "%"
    return result
