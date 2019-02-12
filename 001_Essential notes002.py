##1.3-more Python exercises -- problem03_Count Unique Characters
"""
001 计数有多少个唯一的数字和字母
"""
#UniqueCharacters('ewwwffioj122434') == (6, 4)
#UniqueCharacters('9090909p0y90p90y90') == (2,2)
#UniqueCharacters('ieowjfiojfioj2342io4ji') == (6,3)

def UniqueCharacters(s):
    return (len(set([i for i in s if i.isalpha()])), len(set([i for i in s if i.isdigit()])))

"""
    #[i for i in s if i.isalpha()]  --> ['e', 'w', 'w', 'w', 'f', 'f', 'i', 'o', 'j']
    #set([i for i in s if i.isalpha()])  --> {'e', 'f', 'i', 'j', 'o', 'w'}
    #len(set([i for i in s if i.isalpha()]))  --> 6
    
    #[i for i in s if i.isnumeric()]  --> ['1', '2', '2', '4', '3', '4']
    #set([i for i in s if i.isnumeric()])  -->  {'1', '2', '3', '4'}
    #len(set([i for i in s if i.isnumeric()]))  --> 4
"""




