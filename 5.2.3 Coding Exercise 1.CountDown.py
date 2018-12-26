#We've written a function below called count_down(). This
#function takes an int parameter, start, and prints every
#number from that start to 0. The way we've written it uses
#recursion. Below that funtion, write a function that does
#the exact same thing, but do not use recursion.
#
#The purpose of this exercise is for you to recognize some
#example instances in which you can use recursion, and what
#differences can be seen in the actual code.
#
#Make sure to actually print 0 as the last number!

def count_down(start):
    #If we've reached 0 already, print 0 but do not call
    #another copy
    if start <= 0:
        print(start)
    
    #If we haven't reached 0 yet, print the current number,
    #then call count_down with the current number minus 1.
    else:
        print(start)
        count_down(start - 1)
        
#Do not modify the code above.
#Fill in the function below to do the same as the function
#above, but without recursion. You could use for loops,
#while loops, or some other approach.

def count_down2(start):
    #Add your code here!
    while not start == -1:
        print(start)
        start = start -1

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, 4, 3, 2, 1, 0, each on their own line.
count_down2(5)



