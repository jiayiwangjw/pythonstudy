#Instead of just changing the value of GPA directly, we probably want to instead calculate a new GPA based on the old value 
#and a new grade.
class Student:
     def __init__(self, studentName, enrolled):
         self.studentName = studentName
         self.GPA = 0.0
         self.creditHours = 0
         self.enrolled = enrolled
         self.classes = []
     def updateGPA(self, newGrade, newHours):  #[1]
         newTotal = (newGrade * newHours) + (self.GPA * self.creditHours)
         self.creditHours += newHours  #[2]
         self.GPA = newTotal / self.creditHours  #[3]
      
