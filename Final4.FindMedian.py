#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!

def find_median(file):
    with open(file) as file:
        list2 = file.readlines()  #read text file line by line into a list
    list2 = [x.strip() for x in list2]  #remove whitespace characters like '\n'
    results = list(map(int, list2))  #convert string to int in a list ['1','2']-->[1,2]
    
    #pure Python to calculate median. Do not use Numpy
    theValues = sorted(results)
    if len(theValues) % 2 == 1:
                return theValues[int((len(theValues)+1)/2-1)]
    else:
                lower = theValues[int(len(theValues)/2-1)]
                upper = theValues[int(len(theValues)/2)]
                return (float(lower + upper)) / 2 
    
#from numpy import median        
#   results = median(results)   
#   return results
    file.close()




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))


