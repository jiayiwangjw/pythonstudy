## 5.0.regular expressions

"""
001 基础知识
"""
import re
pattern = 'fox'
pattern_matcher = re.compile(pattern)

input = 'The quick brown fox jumps over the lazy dog'
matches = pattern_matcher.search(input)
print(matches)           #<_sre.SRE_Match object; span=(16, 19), match='fox'>
 
print(matches.group())   #fox
print(matches.start())   #16
print(matches.end())     #19
print(matches.span())    #(16,19)


"""
002 Module-level searching 跳过pattern object的创建，直接进行Module-level searching
"""
matches_2 = re.search ('jump', input)
assert matches_2 is not None
print ("Found", matches_2.group (), "@", matches_2.span ())
#Found jump @ (20, 24)

#match() - Determine if the RE matches at the beginning of the string.
#search() - Scan through a string, looking for any location where this RE matches.
#findall() - Find all substrings where the RE matches, and returns them as a list.
#finditer() - Find all substrings where the RE matches, and returns them as an iterator.


"""
003 Creating pattern groups
"""
re_names2 = re.compile ('''^              # Beginning of string
                           ([a-zA-Z]+)    # First name
                           \s+            # At least one space. 
                           ([a-zA-Z]+\s)? # Optional middle name
                           ([a-zA-Z]+)    # Last name
                           $              # End of string
                        ''',
                        re.VERBOSE)
print (re_names2.match ('Rich Vuduc').groups ())              #('Rich', None, 'Vuduc')
print (re_names2.match ('Rich S Vuduc').groups ())            #('Rich', 'S ', 'Vuduc')
print (re_names2.match ('Rich Salamander Vuduc').groups ())   #('Rich', 'Salamander ', 'Vuduc')


"""
004 Tagging pattern groups
\s | Matches whitespace characters, which include the \t, \n, \r, and space characters
*  | Greedily matches the expression to its left 0 or more times
+  | Greedily matches the expression to its left 1 or more times
"""
re_names3 = re.compile ('''^
                           (?P<first>[a-zA-Z]+)
                           \s             
                           (?P<middle>[a-zA-Z]+\s)?
                           \s*            
                           (?P<last>[a-zA-Z]+) 
                           $
                        ''',
                        re.VERBOSE)
print (re_names3.match ('Rich Vuduc').group ('first'))            #Rich
print (re_names3.match ('Rich S Vuduc').group ('middle'))         #S
print (re_names3.match ('Rich Salamander Vuduc').group ('last'))  #Vuduc











