def FizzBuzzWoof(number):
    return 'Fizz' * (not number % 3) + \
           'Buzz' * (not number % 5) + \
           'Woof' * (not number % 7) \
           or str(number)

