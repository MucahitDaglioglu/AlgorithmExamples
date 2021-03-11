"""
Tau Number
12 divisors -> 1,2,3,4,6,12
6 in total piece 12/6 - remaining=0 (12 is the Tau number)
"""

number = int(input("Enter a number:"))
divisorNumber = 0

for i in range(1,number+1):
    if number%i == 0:
        divisorNumber=divisorNumber+1

if number%divisorNumber == 0:
    print("{} is the Tau number.".format(number))

else:
    print("{} is not the Tau number.".format(number))