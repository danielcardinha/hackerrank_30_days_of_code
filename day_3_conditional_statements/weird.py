def weird(value):
    remainder = value % 2

    # If remainder is not 0, then its an odd number, then return Weird
    if remainder != 0:
        return "Weird"
    elif value in (2, 4):
        return "Not Weird"
    elif 6 <= value <= 20:
        return "Weird"
    else:
        return "Not Weird"
