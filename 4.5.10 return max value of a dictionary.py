#Write a function called most_oscars, which takes in one
#parameter, a dictionary. This dictionary maps names to the
#number of Academy Awards for which they have been nominated.
#This function should return a tuple containing the name and
#number of nominations for the person who has the most
#nominations.
#
#You may assume there will not be a tie for the actor with
#the most nominations (although there may be other ties in
#the list).


#Write your function here!
"""
solution 1
"""
import operator
def most_oscars(dict):
   
   key = max(dict.items(), key=operator.itemgetter(1))[0]
   return (key, dict[key])

"""
solution 2
"""
def most_oscars(oscar_dict):
    
    #There are several slightly different ways we could do this. This is mine, but yours might differ.
    #
    #At a high level, we want to keep track of who has the most nominations of the people we've looked at
    #so far, and update that if we encounter someone with more nominations. So, we need to keep track of a name...
    
    current_max_name = ""
    
    #...and a number. However, we can easily look up the number associated with the current name in the
    #dictionary, so I'm not going to have a separate variable for that. You'll see why shortly.
    #
    #So, now we need to iterate through all the keys in the dictionary. We could also go ahead and
    #iterate over the values, but let's stick to just the keys:
    
    for person in oscar_dict:
        
        #Now we want to check if this current person has more Oscars than the current maximum
        #we've found. The only caveat is that if this is the first person we've checked, we want to
        #copy their name in no matter what. So, we do this:
        #
        #If this is the first person, set this person as our current_max_person:
        
        if current_max_person == "":
            current_max_person = person
            
        #Otherwise, if this is not the first person, but this person has more nominations than the
        #current max person, set this person as our current_max_person:
        elif oscar_dict[current_max_person] < oscar_dict[person]:
            current_max_person = person
    
    #When that loop is done, current_max_person will be the key in the dictionary that corresponds to the
    #largest value. So, we can return that key and its value from the dictionary:
    
    return (current_max_person, oscar_dict[current_max_person])



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))




