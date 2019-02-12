"""
001 选取List of List的一行
"""
grades = [
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

students = [i[0] for i in grades[1:]]  #['Thorny', 'Mac', 'Farva', 'Rabbit', 'Ursula', 'Foster']



"""
002 创建一个字典dict, 列值为key
"""
#grade_lists['Mac'] == [88, 99, 111]
#grade_lists['Ursula'] == [73, 79, 83]
grade_lists = {}
for i in grades[1:]:
    grade_lists[i[0]] = [int(g) for g in i[1:]]



"""
003 创建一个字典dict, 列值行值同时为key
"""
#grade_dicts['Foster']['Exam 1'] == 89
#grade_dicts['Rabbit']['Exam 3'] == 67
assignments = grades[0][1:4]  #assignments == ['Exam 1', 'Exam 2', 'Exam 3']
grade_dicts = {}
for L in grades[1:]:
    grade_dicts[L[0]] = dict(zip(assignments, [int(g) for g in L[1:]]))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
