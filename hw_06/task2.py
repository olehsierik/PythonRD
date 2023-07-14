def check_age(age):
    if type(age) == int and 0 < age <= 110:
        if age >= 18:
            return 'Adult'
        else:
            return 'Child'
    else:
        return 'Error'
