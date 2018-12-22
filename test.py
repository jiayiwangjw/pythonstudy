
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
