#We've started a recursive function below called
#exponent_calc(). It takes in two integer parameters, base
#and expo. It should return the mathematical answer to
#base^expo. For example, exponent_calc(5, 3) should return
#125: 5^3 = 125.
#
#The code is almost done - we have our base case written.
#We know to stop recursing when we've reached the simplest
#form. When the exponent is 0, we return 1, because anything
#to the 0 power is 1. But we are missing our recursive call!
#
#Fill in the marked line with the recursive call necessary
#to complete the function. Do not use the double-asterisk
#operator for exponentiation. Do not use any loops.
#
#Hint: Notice the similarity between exponentiation and
#factorial:
#  4! = 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1
#  2^4 = 2 * 2^3, 2^3 = 2 * 2^2, 2^2 = 2 * 2^1, 2^1 = 2 * 2^0

def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base, (expo-1))
    
    #Complete this line!

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 125
print(exponent_calc(5, 3))




