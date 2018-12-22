#Write function called third_character that accepts a
#string as an argument and returns the third character
#of the string. If the user inputs a string with fewer than
#3 characters, return "Too short". 


#Write your function here!
def third_character(str):
    if len(str) < 3:
        return "Too short"
    else:
        return str[2]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, o, and "Too short", each on a different line.
print(third_character("CS1301"))
print(third_character("Georgia Tech"))
print(third_character("GT"))



