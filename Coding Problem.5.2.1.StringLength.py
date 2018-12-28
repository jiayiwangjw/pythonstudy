#We've started a recursive function below called
#measure_string that should take in one string parameter,
#myStr, and returns its length. However, you may not use
#Python's built-in len function.
#
#Finish our code. We are missing the base case and the
#recursive call.
#
#HINT: Often when we have recursion involving strings, we
#want to break down the string to be in its simplest form.
#Think about how you could splice a string little by little.
#Then think about what your base case might be - what is
#the most basic, minimal string you can have in python?
#
#Hint 2: How can you establish the base case has been
#reached without the len() function?

#You may not use the built-in 'len()' function.

def measure_string(myStr):
    if myStr == "":   #Complete this line!
    	return 0 #Complete this line!
    else:
        return 1 + measure_string(myStr[1:])  #Complete this line!
    
    
#The line below will test your function. As written, this
#should print 13. You may modify this to test your code.
print(measure_string("13 characters"))

