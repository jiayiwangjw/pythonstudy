#Let's implement Mergesort! This is a complex problem
#because it applies recursion to sorting algorithms, but
#it's also by far the most efficient sorting algorithm we'll
#cover.

#First, we need a function definition: MergeSort should take
#as input one list.

def mergesort(lst):
    
    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only
    #one item, we should just return that one-item list.
    
    if len(lst) <= 1:
        return lst
    
    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:

        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(lst) // 2

        #lst[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])

        #And same for the right side.
        right = mergesort(lst[midpoint:])

        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.

        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            #If the first number in left is lower, add
            #it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]

            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        #newlist is now the sorted version of lst! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.

        return newlist

#Let's try it out!
print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

#It works! To see more about how it works, check out
#MergesortwithPrints.py. To get a succinct version of
#this algorithm, checkout MergesortShort.py.
