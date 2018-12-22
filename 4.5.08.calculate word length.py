#Write a function called word_lengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should be lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, exclamation points, and apostrophes.
#
#For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
#Hint: Use the split() method to split by spaces, and don't
#forget to remove punctuation marks.  Remember also: strings
#are immutable, so operations like my_string.lower() don't
#change the value of my_string like list methods: to save
#those results, you'd write my_string = my_string.lower().
#
#Your dictionary should not have any duplicate keys (in fact,
#Python won't allow a dictionary to have duplicate keys).


def word_lengths(sentence):
    
    #First, let's transform the sentence so we can focus
    #only on the words we care about. We want to convert
    #the sentence to lower case:
    
    sentence = sentence.lower()
    
    #Then we want to get rid of all the punctuation. The
    #directions said we need only worry about five
    #symbols: .,'!?. So, we take care of this by
    #replacing each of those in the sentence with nothing:
    
    to_replace = ".,'!?"
    for mark in to_replace:
        sentence = sentence.replace(mark, "")
        
    #We could have also done this one line at a time, but
    #this method above is prettier.
    #
    #Next, we split the sentence into words by spaces:
    
    sentence = sentence.split(' ')
    
    #And create an empty dictionary to hold the results:
    
    word_lengths = {}
    
    #Now we iterate over each word in the sentence:
    
    for word in sentence:
        
        #And add it as a key to the dictionary, with its
        #value as the length of that word:
        
        word_lengths[word] = len(word)
        
    
    #Once that's done, we're done! We return the
    #dictionary that we just created:
    
    return word_lengths


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
