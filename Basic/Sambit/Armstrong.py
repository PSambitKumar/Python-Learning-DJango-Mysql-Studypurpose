import math


def armstrong():
    number = int(input("Enter a Number to Check?\n"))
    originalNumber = number
    result = 0
    while originalNumber != 0:
        reminder = originalNumber % 10
        result += math.pow(reminder, 3)
        originalNumber //= 10

    if number == result :
        print(str(number) + " is an Armstrong Number.")
    else:
        print(str(number) + " is not an Armstrong Number.")
