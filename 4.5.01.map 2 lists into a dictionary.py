#Write a function called phonebook that takes two lists as
#input:
#
# - names, a list of names as strings
# - numbers, a list of phone numbers as strings
#
#phonebook() should take these two lists and create a
#dictionary that maps each name to its phone number. For
#example, the first name in names should become a key in
#the dictionary, and the first number in numbers should
#become the value corresponding to the first name. Then, it
#should return the dictionary that results.
#
#Hint: Because you're mapping the first name with the first
#number, the second name with the second number, etc., you do
#not need two loops. For a similar exercise, check back on
#Coding Problem 4.3.3, the Scantron grading problem.
#
#You may assume that the two lists have the same number of
#items: there will be no names without numbers or numbers
#without names.


#Write your function here!
def phonebook(name, number):
    dictionary = {}
    dictionary = dict(zip(name, number))
    return dictionary


"""
sample solution
"""
def phonebook(name_list, number_list):
    
    #First, we need to create the empty dictionary that
    #we'll populate:
    
    phonebook = {}
    
    #Next, we want to simultaneously iterate over both
    #name_list and number_list, one by one. To do that,
    #we should use a for loop -- that way, we have a 
    #variable to use as the index to both lists. Since
    #the lists are the same length, the loop can be over
    #either one's length:
    
    for i in range(len(name_list)):
        
        #Next we want to get the name and number out:
        
        name = name_list[i]
        number = number_list[i]
        
        #And finally, we can add this new key and value
        #to our dictionary:
        
        phonebook[name] = number
        
        #We could compress these three lines down to just
        #this one:
        #
        #phonebook[name_list[i]] = number_list[i]
        

    #Then, we return the phonebook we just created:
    
    return phonebook
"""   

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Jackie': '404-555-1234', 'Joshua': '678-555-5678', 'Marguerite': '770-555-9012'

name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))


