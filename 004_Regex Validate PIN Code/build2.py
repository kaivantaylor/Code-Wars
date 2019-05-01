def validate_pin(pin):
    length = len(pin)

    if pin.isdigit() == True:
        if length == 4 or length == 6:
            return True
        else:
            return False
    else:
        return False
