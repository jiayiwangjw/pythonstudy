#Recall in the lesson on sorts that we had you complete the
#Bubble and Selection sort, and we showed you Merge sort.
#We didn't show any of insertion sort, and I bet you can
#guess why.
#
#Implement insertion sort below.
#
#Name your function 'insertion'. insertion should take as
#input a list, and return as output a sorted list. Note that
#even though technically a sorting method does not have to
#return the sorted list, yours should.
#
#If you're stuck on where to start, or having trouble
#visualizing or understanding how exactly insertion sort
#works, check out this website - https://visualgo.net/sorting
#It provides a visual representation of all of the sorting
#algorithms as well as pseudocode you can base your own code
#off of.


#Write your code here!
def insertion(alist):
    for index in range(1, len(alist)):
        current = alist[index]
        position = index
        
        while position > 0 and alist[position - 1] > current:
            alist[position] = alist[position -1]
            position = position - 1
        alist[position] = current
        
    return alist


#The code below will test your function. If your function
#works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 1, 3, 2, 4]))


