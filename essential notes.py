#选取List of List的一行
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
