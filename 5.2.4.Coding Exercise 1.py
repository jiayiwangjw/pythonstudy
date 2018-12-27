#We've written the function, sort_with_bubbles, below. It takes
#in one list parameter, lst. However, there are two problems in
#our current code:
# - There's a missing line
# - There's a semantic error (the code does not raise an
#   error message, but it does not perform correctly)
#
#Find and fix these problems! Note that you should only need
#to change or add code where explicitly indicated.
#
#Hint: If you're stuck, use an example input list and trace
#the code and how it modifies your list on paper. For
#example, try writing out what happens to the following list:
#
#  [34, 16, 2, 78, 4, 6, 1]

"""
def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True
    
    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        
        #Start off assuming a swap did not occur
        swap_occurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                lst[i] = lst[i + 1]
                temp = lst[i]   # delete this line
                lst[i + 1] = temp

                #One more line is needed here; add it!
            
    return lst
"""
def sort_with_bubbles(alist):
    for i in range(len(alist)-1,0,-1):  #(4,0,-1)
        for j in range(i): #4,3,2,1
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_bubbles([5, 3, 1, 2, 4]))


