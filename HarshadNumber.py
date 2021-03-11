"""
Harshad Number
18 -> 1+8 = 9 -- divides  (Harshad number)
1729 -> 1+7+2+9=19 -- divides (Harshad number)
"""

def HarshadNumber(number):
    total = 0
    while number > 0:
        numeral = int(number % 10)
        number = number / 10
        total += numeral

    return total

number = int(input("Enter a number:"))
total = HarshadNumber(number)

if number % total == 0:
    print("{} is the Harshad number.".format(number))
else:
    print("{} is not the Harshad number.".format(number))