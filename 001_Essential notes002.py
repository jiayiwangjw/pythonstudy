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


##1.3-more Python exercises --  problem04_Flatten List
"""
002 Flatten a complex LIST
"""
# L = [['a', ['cat'], 2],[[[3]], 'dog'], 4, 5] --> ['a', 'cat', 2, 3, 'dog', 4, 5]

def flatten(L):
    assert type(L) is list

    flatList = []
    for i in L:
        if type(i) is not list:
            flatList += [i]
        else:
            flatList += flatten(i)  #use recursion
    return flatList   


##1.3-more Python exercises -- problem05_Pair Counts
"""
003 找出组合是数字连续的个数
"""
#L1=[1,2,3,4,5,6,7,8,9]
#L2=[1,1,1,2,2,3,4,10]
#L3=[1,4,7,9]
#L4=[]
#    assert count_pairs(L1)==8, "Test Case L1 failed"   1，2  2，3  3，4  4，5  5，6  6，7  7，8  8，9
#    assert count_pairs(L2)==9, "Test Case L2 failed"   1，2  1，2  1，2  1，2  1，2  1，2  2，3，2，3，3，4
#    assert count_pairs(L3)==0, "Test Case L3 failed"
#    assert count_pairs(L4)==0, "Test Case L4 failed"


from collections import Counter
def count_pairs(L):   #L [1, 1, 1, 2, 2, 5, 8, 8]
    assert type(L)==list
    counts = Counter(L)    #counts   ({1: 3, 2: 2, 5: 1, 8: 2})
    unique_items = sorted(counts.keys())  #[1, 2, 5, 8]
    unique_pairs = zip(unique_items[1:], unique_items[:-1])   #zip([2, 5, 8], [1, 2, 5])  -->[(2, 1), (5, 2), (8, 5)]
    unit_diff_combos = [counts[b]*counts[a] for b, a in unique_pairs if (b-a) == 1]   #[6]
    return sum(unit_diff_combos)
    


