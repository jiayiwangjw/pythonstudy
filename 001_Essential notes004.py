
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
001 通过List的index寻找另一个list的内容
"""
def lookup_value(col_name, row_id, header, data_rows):
     col_id = header.index(col_name)  # "age" --> 2
     return data_rows[row_id][col_id] # 18

#lookup_value('age', 0, math_header, math_data_rows) == '18'
#lookup_value('G2', 3, math_header, math_data_rows) == '14'
