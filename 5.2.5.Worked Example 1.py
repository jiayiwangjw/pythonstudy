#Let's implement a binary search using a loop! For now,
#our search will just return True if the item is found,
#False if it's not.

#Like our linear search, our binary search needs to
#parameters: a list to search, and an item to search for.

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #Now, each iteration of the loop, we want to narrow
    #down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so
    #far. Initially, that will be the entire list, from
    #the first index to the last.
    
    min = 0
    max = len(searchList) - 1
    
    #Now, we want to loop as long as our range has any
    #numbers left to investigate. As long as there is
    #more than one number between minimum and maximum,
    #we're not done searching.
    
    while min <= max:

        #We want to check the middle item of the
        #current range, which is the average of the
        #current minimum and maximum index. For
        #example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll
        #use floor division because indices must be
        #integers.
        currentMiddle = (min + max) // 2

        #If the term in the middle is the term we're
        #looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True

        #If not, we want to check if the term we're
        #looking for should come earlier or later.

        #If the term we're looking for is less than
        #the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1

        #If the term we're looking for is greater
        #than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1

        #Each iteration of the loop, one of three
        #things happens: the term is found, max
        #shrinks, or min grows. Eventually, either
        #the term will be found, or min will be
        #equal to max.

    #If the search term was found, this line will
    #never be reached because the return statement
    #will end the function. So, if we get this
    #far, then the search term was not found, and
    #we can return False.
    return False

#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


#Now, go see how it works with recursion instead of loops
#in RecursiveBinarySearch.py! Or, print how this works with
#LoopingBinarySearchwithPrints.py.


