## 5.0.regular expressions

"""
001 基础知识
"""
import re
pattern = 'fox'
pattern_matcher = re.compile(pattern)

input = 'The quick brown fox jumps over the lazy dog'
matches = pattern_matcher.search(input)
print(matches)

#<_sre.SRE_Match object; span=(16, 19), match='fox'>
 
print(matches.group())   #fox
print(matches.start())   #16
print(matches.end())     #19
print(matches.span())    #(16,19)


