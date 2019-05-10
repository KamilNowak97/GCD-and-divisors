number1 = int(input("Write first number: "))
number2 = int(input("Write second number: "))

divisorsTab = []
setDivisorsTab = set()
#Brute force - fin
def divisors(number):
    out = []
    for i in range(1, number + 1, 1):
         if number % i == 0:
             out.append(i)
    return out


#GCD
def GCD(number1,number2):
    while number2 != 0:
        out = number1 % number2
        number1 = number2
        number2 = out
    return number1

print("--------------Brute force-------------------------")
print("Divisors of number {0} are: {1}".format(number1,divisors(number1)))
print("Divisors of number {0} are: {1}".format(number2,divisors(number2)))
print("------------------------------")
print("GCD of {0} and {1} is: {2} ".format(number1,number2,GCD(number1,number2)))

