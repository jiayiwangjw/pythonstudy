#Recall last exercise that you wrote a function, word_lengths,
#which took in a string and returned a dictionary where each
#word of the string was mapped to an integer value of how
#long it was.
#
#This time, write a new function called length_words so that
#the returned dictionary maps an integer, the length of a
#word, to a list of words from the sentence with that length.
#If a word occurs more than once, add it more than once. The
#words in the list should appear in the same order in which
#they appeared in the sentence.
#
#For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
#As before, you should remove any punctuation and make the
#string lowercase.
#
#Hint: To create a new list as the value for a dictionary key,
#use empty brackets: lengths[wordLength] = []. Then, you would
#be able to call lengths[wordLength].append(word). Note that
#if you try to append to the list before creating it for that
#key, you'll receive a KeyError.


#Write your function here!
"""
#this solution does eliminate duplicates
def length_words(sentence):
    sentence = sentence.lower()
   
    to_replace = ".,'!?"
    for mark in to_replace:
        sentence = sentence.replace(mark, "")
    
    sentence = sentence.split(' ')
    
    sample_dictionary={}
    for word in sentence:
        words=len(word)
        if words in sample_dictionary:
            sample_dictionary[words].append(word)
        else:
            sample_dictionary[words] = {word}
    return sample_dictionary
"""
#this solution does not eliminate duplicates
def length_words(sentence):
    
    #The preparation for this problem is the same as the
    #previous one: strip out punctuation, convert to lower
    #case, split the string by spaces, and create a new
    #dictionary to hold our results:
    
    sentence = sentence.lower()
    
    to_replace = ".,'!?"
    for mark in to_replace:
        sentence = sentence.replace(mark, "")
        
    sentence = sentence.split(' ')
    word_lengths = {}
    
    #Then, as before, we iterate through each word in the
    #sentence:
    
    for word in sentence:
        
        #However, instead of adding word as the key to the
        #dictionary, we want to add len(word) as the key.
        #The values are going to be lists, which makes things
        #more complicated: we want to be able to add things
        #to an existing list when we encounter future words
        #with the same length. That means we need to check
        #if the key already exists in the dictionary.
        #
        #There are a few ways to do this, but here's my
        #preferred way. First, check to see if len(word) is
        #already in the dictionary:
        
        if len(word) not in word_lengths.keys():
            
            #If it's not, then add it, and set its value to
            #an empty list:
            
            word_lengths[len(word)] = []
            
        #Now, we're guaranteed here that len(word) is a key
        #because if it wasn't already one, we *just* added
        #it. So, we can just go ahead and append to its list
        #without worrying about a key error.
        #
        #First, we get the list of words with the same length
        #as the current word:
        
        word_list = word_lengths[len(word)]
        
        #Then, we add the current word to that list:
        
        word_list.append(word)
        
        #Remember, lists are mutable, so word_list is pointing
        #to the same actual list as word_lengths[len(word)]. So,
        #adding word to word_list also adds it to
        #word_lengths[len(word)].
        
    
    #Now we're done, so we can return our result!
    
    return word_lengths
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))





