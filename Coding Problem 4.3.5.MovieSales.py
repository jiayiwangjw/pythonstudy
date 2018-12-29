#Write a function called find_max_sales. find_max_sales will
#have one parameter: a list of tuples. Each tuple in the
#list will have two items: a string and an integer. The
#string will represent the name of a movie, and the integer
#will represent that movie's total ticket sales (in millions
#of dollars).
#
#The function should return the movie from the list that
#had the most sales. Return only the movie name, not the
#full tuple.


#Write your function here!
from operator import itemgetter
def find_max_sales(lis):
    result = []
#    result = max(lis,key=itemgetter(1))[0] 
#    return result#faster solution
    result = max(lis,key=itemgetter(1))
    return result[0]


"""
#sample solution 1
#This problem uses a pretty common design pattern. You'll
#learn about it in more detail later when we talk about
#linear searches in Chapter 5.2, but it's possible to
#figure it out on your own as well.
#
#What we want to do is check every movie in the list and
#see if it's bigger than our current max. If it is, it
#becomes our new max. Then, once we've checked every
#movie, whatever max we landed on is our maximum.

def find_max_sales(movie_list):
    
    #To start, we want to keep track of the movie with
    #the highest sales so far (so we can return it), and
    #what its sales were (so we can compare it). Let's
    #create these:
    
    current_max_movie = ""
    current_max_sales = -1
    
    #Note that we initially set current_max_sales to -1.
    #That's one way to guarantee that the first movie
    #we look at becomes our maximum: we know its sales
    #are going to be more than -1.
    #
    #Now, let's go through each movie in the list:
    
    for movie_tuple in movie_list:
        
        #And check if its sales are higher than our
        #current max:
        
        if movie_tuple[1] > current_max_sales:
            
            #If so, then this should become our new
            #maximum:
            
            current_max_sales = movie_tuple[1]
            
            #And its name should become our new top
            #movie:
            
            current_max_movie = movie_tuple[0]
    
    #Once we've looked at all the movies, then
    #current_max_movie will hold the highest in the
    #list:
    
    return current_max_movie

"""

"""
#Sample Solution 2
#We can make this a little bit easier, though. We don't
#actually need to keep track of the current high-grossing
#title and its actual sales separately: we can just keep
#track of the tuple that currently has the most sales.
#Check it out:

def find_max_sales(movie_list):
    
    #Instead of initializing two variables to something
    #empty, we set the current max to the first item in
    #the list. That way, we're already comparing against
    #something. If the first item is the highest-grossing
    #movie, then this variable will just never get
    #changed:
    
    current_max_tuple = movie_list[0]
    
    #Next, we run the same loop as before:
    
    for movie_tuple in movie_list:
        
        #And perform the same check, but we're checking
        #against the gross of the current max movie,
        #which is the second item in that tuple:
        
        if movie_tuple[1] > current_max_tuple[1]:
            
            #If it's higher, we point the entire tuple
            #at the new maximum movie:
            
            current_max_tuple = movie_tuple
    
    #And in the end, we return the title from the maximum
    #tuple:
    
    return current_max_tuple[0]
"""

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Rogue One
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))




