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

#{'Foster': [89, 97, 101], 'Rabbit': [59, 61, 67], 'Mac': [88, 99, 111], 'Farva': [45, 56, 67], 'Ursula': [73, 79, 83], 
#'Thorny': [100, 90, 80]}



"""
003 创建一个字典dict, 列值与行值同时为key
"""
#grade_dicts['Foster']['Exam 1'] == 89
#grade_dicts['Rabbit']['Exam 3'] == 67
assignments = grades[0][1:4]  #assignments == ['Exam 1', 'Exam 2', 'Exam 3']
grade_dicts = {}
for L in grades[1:]:
    grade_dicts[L[0]] = dict(zip(assignments, [int(g) for g in L[1:]]))

#{'Foster': {'Exam 1': 89, 'Exam 2': 97, 'Exam 3': 101}, 'Rabbit': {'Exam 1': 59, 'Exam 2': 61, 'Exam 3': 67}, 
#'Mac': {'Exam 1': 88, 'Exam 2': 99, 'Exam 3': 111}, 'Farva': {'Exam 1': 45, 'Exam 2': 56, 'Exam 3': 67}, 
#'Ursula': {'Exam 1': 73, 'Exam 2': 79, 'Exam 3': 83}, 'Thorny': {'Exam 1': 100, 'Exam 2': 90, 'Exam 3': 80}}



"""
004 创建一个字典dict,通过列值作为key返回该列对应的平均值
"""
#avg_grades_by_student['Mac'] - 99.333333333
from statistics import mean
avg_grades_by_student = {n:mean(g) for n, g in grade_lists.items() }  #grade_lists {'Foster': [89, 97, 101],...}

#{'Foster': 95.66666666666667, 'Rabbit': 62.333333333333336, 'Mac': 99.33333333333333, 'Farva': 56, 
#'Ursula': 78.33333333333333, 'Thorny': 90}   
    
    
"""
005 创建一个字典，通过header作为key返回对应的列值
"""
#grades_by_assignment['Exam 1'] == [100, 88, 45, 59, 73, 89]
grades_by_assignment = {} # Empty dictionary
for k, a in enumerate(assignments): # 0 Exam 1, 1 Exam 2, 2 Exam 3
     grades_by_assignment[a] = [int(L[k+1]) for L in grades[1:]]    
    
    
    
    
    
    
