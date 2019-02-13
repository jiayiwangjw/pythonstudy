## 5.0.regular expressions


"""
000 必须理解的基础知识

* 对它前面的正则式匹配0到任意次重复， 尽量多的匹配字符串。 ab* 会匹配 'a'， 'ab'， 或者 'a'``后面跟随任意个 ``'b'。
+ 对它前面的正则式匹配1到任意次重复。 ab+ 会匹配 'a' 后面跟随1个以上到任意个 'b'，它不会匹配 'a'。
? 对它前面的正则式匹配0到1次重复。 ab? 会匹配 'a' 或者 'ab'。
"{m}" 对其之前的正则式指定匹配 m 个重复；少于 m 的话就会导致匹配失败。比如， a{6} 将匹配6个 'a' , 但是不能是5个。
\s 对于 Unicode (str) 样式： 匹配任何Unicode空白字符（包括 [ \t\n\r\f\v]。。
"""
#  https://docs.python.org/zh-cn/3/library/re.html

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



"""
005 识别email地址
"""
#A username must begin with an alphabetic character [a-zA-Z]. It may be followed by any number of additional alphanumeric characters [\w]
#or any of the following special characters: . (period), - (hyphen), _ (underscore), or + (plus). [.\-+]

#A domain name must end with an alphabetic character [a-zA-Z]. It may consist of any of the following characters: alphanumeric characters, 
#. (period), - (hyphen), or _ (underscore). [\w.\-]

# \w | Matches alphanumeric characters, which means a-z, A-Z, and 0-9. It also matches the underscore, _.
# *  | Greedily matches the expression to its left 0 or more times

def parse_email (s):
     pattern =   '''
                    ^
                    (?P<userID>[a-zA-Z][\w.\-+]*)
                    @
                    (?P<domain>[\w.\-]*[a-zA-Z])
                    $
                 '''   
     re_names = re.compile(pattern, re.VERBOSE)
     matches = re_names.match(s)
     if matches:
            return (matches.group('userID'), matches.group('domain'))
     else:
            raise ValueError("Incorrect email address")


"""
006 电话号码识别1
"""
# "(404) 555-1212" format
# i.e., a three-digit area code enclosed in parentheses followed by a seven-digit local number in three-hyphen-four digit format.

#It should also ignore all leading and trailing spaces, as well as any spaces that appear between the area code and local numbers.

#However, it should NOT accept any spaces in the area code (e.g., in '(404)') NOR should it in the seven-digit local number.

# \d  | Matches digits, which means 0-9.
# {m} | Matches the expression to its left m times, and not less.
# \s  | Matches whitespace characters, which include the \t, \n, \r, and space characters
# *   | Greedily matches the expression to its left 0 or more times

def parse_phone1 (s):
    pattern =   '''
                    ^
                    \s*                     # Matches whitespace and Repeats a character zero or more times
                    \((?P<areacode>\d{3})\) # Area code   \(...\)
                    \s*
                    (?P<digits3>\d{3})      # Local prefix (3 digits)
                    -
                    (?P<digits4>\d{4})      # Local suffix (4 digits)
                    $
                 '''   
    re_names = re.compile(pattern, re.VERBOSE)
    matches = re_names.match(s)
    if matches:
        return (matches.group('areacode'), matches.group('digits3'), matches.group('digits4'))
    else:
        raise ValueError("Incorrect phone number")

"""
007 电话号码识别2
"""
#(404) 555-1212
#(404) 5551212
#404-555-1212
#404-5551212
#404555-1212
#4045551212

def parse_phone2 (s):
        pattern = '''
            ^\s*              # leading spaces
            (?P<areacode>
               \d{3}-?        # "xxx" or "xxx-"
               | \(\d{3}\)\s* # OR "(xxx) "
            )
            (?P<digits3>\d{3}) # xxx
            -?                # Dash (optional)
            (?P<digits4>\d{4}) # xxxx
            \s*$              # trailing spaces
            '''
        re_names = re.compile(pattern, re.VERBOSE)
        matches = re_names.match(s)
        if matches is None:
            raise ValueError("'{}' is not in the right format.".format (s))
        areacode = re.search('\d{3}', matches.group ('areacode')).group()
        digits3 = matches.group ('digits3')
        digits4 = matches.group ('digits4')
        return (areacode, digits3, digits4)









