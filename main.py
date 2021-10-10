import math

question = input("what mathematical equation do you want to use:- ")

#finding gcd of two numbers
if (question == "gcd"):
    gcd1 = int(input("What is the first number you want a gcd of:- "))
    gcd2 = int(input("What is the second number you want a gcd of:- "))
    totalgcd = math.gcd(gcd1,gcd2)
    print(totalgcd)

#finding the facorial of a number
elif(question == "factorial"):
    factorialinput = int(input("what is the number you want the factorial of:- "))
    totalfactorial = math.factorial(factorialinput)
    print(totalfactorial)

#finding the exponent of a base and power
elif(question == "exponent"):
    baseinput = int(input("what is the base of the exponent:- "))
    powerinput = int(input("what is the power you want to raise the base to:- "))
    totalpower = math.pow(baseinput, powerinput)
    print(totalpower)

#finding the log base 10 of an integer
elif(question == "log10"):
    logxinput = int(input("What is the number you want to get a log base 10 of:- "))
    totallog = math.log10(logxinput)
    print(totallog)

#Error message
else:
    print("That is not a function in the code")






