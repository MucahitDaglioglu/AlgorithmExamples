"""
Armstrong Number
153 -> (1*1*1) + (5*5*5) + (3*3*3) = 1+125+27=153
"""
import  math

def ArmstrongNumber(number):
    total = 0
    for i in range(0, len(str(number))):
        digit = int(number % 10)
        number = number / 10
        total += int(math.pow(digit, 3))
    return  total

number = int(input("Enter a number:"))
total = ArmstrongNumber(number)
if number == total:
    print("{} is the Armstrong number.".format(number))
else:
    print("{} is not the Armstrong number.".format(number))