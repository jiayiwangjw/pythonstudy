##problem1_Boozy Containers

header = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime',
'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime',
'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']

data_rows = [['GP', 'F', '18', 'U', 'GT3', 'A', '4', '4', 'at_home', 'teacher', 'course', 'mother', '2', '2', '0', 'yes', 'no', 'no', 'no',
'yes', 'yes', 'no', 'no', '4', '3', '4', '1', '1', '3', '6', '5', '6', '6'], ['GP', 'F', '17', 'U', 'GT3', 'T', '1', '1', 'at_home',
'other', 'course', 'father', '1', '2', '0', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', '5', '3', '3', '1', '1', '3', '4', '5',
'5', '6'], ['GP', 'F', '15', 'U', 'LE3', 'T', '1', '1', 'at_home', 'other', 'other', 'mother', '1', '2', '3', 'yes', 'no', 'yes', 'no',
'yes', 'yes', 'yes', 'no', '4', '3', '2', '2', '3', '3', '10', '7', '8', '10'], ['GP', 'F', '15', 'U', 'GT3', 'T', '4', '2', 'health',
'services', 'home', 'mother', '1', '3', '0', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', '3', '2', '2', '1', '1', '5', '2',
'15', '14', '15'],['GP', 'F', '16', 'U', 'GT3', 'T', '3', '3', 'other', 'other', 'home', 'father', '1', '2', '0', 'no', 'yes', 'yes',
'no', 'yes', 'yes', 'no', 'no', '4', '3', '2', '1', '2', '5', '4', '6', '10', '10']]

"""
001 通过List的header信息，寻找另一个list的指定行对应的内容
"""
def lookup_value(col_name, row_id, header, data_rows):
     col_id = header.index(col_name)  # "age" --> 2
     return data_rows[row_id][col_id] # 18

#lookup_value('age', 0, header, data_rows) == '18'
#lookup_value('G2', 3, header, data_rows) == '14'


"""
002 通过List的header信息，寻找另一个list的对应列的全部内容
"""
def lookup_column_values(col, header, data_rows):
     col_id = header.index(col)  #得到index
     return [row[col_id] for row in data_rows]  #遍历每一行

#values = lookup_column_values('age', header, data_rows)
#assert values[:5] == ['18', '17', '15', '15', '16']


"""
003 通过List的header信息，寻找另一个list的对应列的唯一值unique value
"""

def get_unique_values(col, header, data_rows):
      return list(set(lookup_column_values(col, header, data_rows)))

#solution2
def get_unique_values(col, header, data_rows):
    col_id = header.index(col)  
    value = [row[col_id] for row in data_rows] 
    return list(set(value))


"""
004  构建一个字典dw_avg_grade， key为列'Dalc'和'Walc'的各种组合(a,b)， value为该组合所对应的G3平均值
"""
#The column 'Dalc' contains the student's self-reported drinking frequency during the weekday
#Similarly, 'Walc' is the self-reported drinking frequency on the same scale, but for the weekend (instead of weekday).
print("Unique values of 'Dalc':", get_unique_values('Dalc', header, data_rows))
Unique values of 'Dalc': ['5', '1', '4', '3', '2']

#(Dalc=3, Walc=2): 12.0
#(Dalc=4, Walc=4): 11.3

from collections import defaultdict # Optional, but might help

# Relevant data to analyze:
Dalc_values = lookup_column_values('Dalc', math_header, math_data_rows)
Walc_values = lookup_column_values('Walc', math_header, math_data_rows)
G3_values = lookup_column_values('G3', math_header, math_data_rows)

#-->{pair(a,b): mean=grade/occurances}

dw_counts = defaultdict(int)  #defaultdict(int, {})
dw_sums = defaultdict(int)
for d, w, g3 in zip(Dalc_values, Walc_values, G3_values):
    key = (int(d), int(w))  #required tuple (a,b)
    value = int(g3)
    dw_counts[key] += 1   #count the pairs {(1, 1): 42, (2, 3): 6, (1, 2): 12....}
    dw_sums[key] += value  # {(1, 1): 468, (2, 3): 60, (1, 2): 150....}
    
dw_avg_grade = {}
for key in dw_sums.keys():   #key: (1, 1)  (2, 3)  (1, 2)
    dw_avg_grade[key] = round(dw_sums[key] / dw_counts[key], 1)  #{(1, 1): 11.1, (2, 3): 10.0, (1, 2): 12.5....}



#problem2_DNA Sequence Analysis
dna_seq = 'ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT'
print("=== Sequence (Number of bases: {}) ===\n\n{}".format(len(dna_seq), dna_seq))

"""
005 构建一个字典 对出现的字母进行计数
"""
def count_bases(s):
    assert type(s) is str
    assert all([b in ['A', 'C', 'G', 'T'] for b in s])
    #
    # YOUR CODE HERE
    #
    return dict((x, s.count(x)) for x in set(s))

#solution 2
    from collections import Counter
    return dict(Counter(s))

#result: {'A': 501, 'G': 508, 'C': 507, 'T': 496}






