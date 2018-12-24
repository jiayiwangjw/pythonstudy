#Write a function called next_fib. next_fib should take
#have two parameters: a list of integers and a single integer.
#For this description, we'll call the single integer n.
#
#next_fib should modify the list to add the next n pseudo-
#Fibonacci numbers to the end of the sequence. A pseudo-
#Fibonacci number is the sum of the previous two numbers in
#the sequence, but in our case, the previous two numbers may
#not be the original numbers from the Fibonacci sequence.
#
#For example, if the original list given was:
#
# a_list = [5, 5, 10, 15, 25, 40, 65]
#
# Then next_fib(a_list, 3) would return:
#       [5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
#
#All the original numbers in the list are still there, and
#three new ones have been added.
#
#You may assume the list parameter will always have at least
#two numbers.
#
#HINT: Python gets mad if you try to change a list while
#iterating over it with a for-each loop. You'll have to get
#clever with a for or while loop to do this!


#Add your code here!
def next_fib(a_list, n):
    count = 0
#    i= len(a_list)  #7  (0,1,...6) -->(0,1,...6,...,6+n)
    for i in range(len(a_list), (len(a_list)+n)) :  #(7,10)
         if count <= n:
            a_list.append(a_list[i-1]+a_list[i-2])
            count +=1
    return a_list

"""
#Sampel solution for Fibonacci Sequence

def fibGenerator():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

fibonaccinumbers = []
fib = fibGenerator()
for n in range(20):
    fibonaccinumbers.append(next(fib))
"""


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[5, 5, 10, 15, 25, 40, 65, 105, 170, 275] 
a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))





