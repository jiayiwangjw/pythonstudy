#Python, like most languages, actually uses numbers in the 
#background to represent individual characters in a string. 
#For example, "a" is assigned the numeric value of 97. 
#We call this the ordinal value. www.asciitable.com shows
#a table of ordinal values: the ordinal value is listed in
#the 'dec' column, and the actual character is listed in
#'chr' column.
#
#You'll notice, though, that many of the characters here
#are weird. The first 31 are cryptic characters that have
#special meaning to the computer. The extended codes haven't
#really been used since Windows came along. Beyond these
#255, the higher numbers are actually used to represent
#emojis.
#
#Now, think about when you're asked to create a password.
#Typically, there are restrictions on what characters you
#can use. How do you check if a password is valid? You
#could have a list of valid characters and check each
#character against that list, but that would be a really
#long list. Instead, let's use ordinal values.
#
#Write a function called "valid_char" that determines
#if a single character (a string of length one) has an
#ordinal value corresponding to a valid character for a
#password. Valid characters are any character on the
#keyboard except spaces. Return True if it's a valid
#character, False if it is not.
#
#Hint: you can find the ordinal value of a character using 
#the built-in Python function ord(): ord("a") -> 97
#
#Hint 2: the range of legal characters will be one
#continuous range (e.g. characters 55 through 65, not
#separate ranges like 55 through 65 and 69 through 79).
#You can use asciitable.com to look up what range you
#should use.


#Write your function here!
def valid_char(s):
    s = ord(s)
    if s in range(33, 127):
        return True
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False

print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))



