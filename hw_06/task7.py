def is_prime(number):
    number_divisors = 2
    if number > 1:
        for i in range(1, int(number * 0.5)):
            i += 1
            if number % i == 0:
                number_divisors += 1
                if number_divisors > 2:
                    return 'False'
    else:
        return 'False'
    if number_divisors == 2:
        return 'True'
