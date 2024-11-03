def calculate_interest(time, interest_rate, amount):

    decimal_rate = interest_rate / 100

    interest = decimal_rate * time * amount
    print(interest)


calculate_interest(36, 10.65, 2000000)
