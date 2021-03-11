#Decimal To Binary Conversion

def DecimalToBinary(number):
    binary = 0
    i = 1
    while number != 0:
        remaining = number % 2
        number = int(number / 2)
        binary = binary + remaining * i
        i = i * 10

    return binary

number = int(input("Enter a number:"))
result = DecimalToBinary(number)
print(result)