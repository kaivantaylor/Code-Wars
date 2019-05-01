def validate_pin(pin):
    length = len(pin)

    try:
        x = int(pin)

        if (length == 4 or length == 6) and (x >= 0):
            return True
        else:
            return False

    except ValueError:
        return False
#does not work for test cases
