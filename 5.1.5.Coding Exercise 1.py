#Classes can also have references to other instances of
#themselves. Consider this Person class, for example, 
#that allows for an instance of a father and mother
#to be given in the constructor.
#
#Create 3 instances of this class. The first should have 
#the name "Mr. Burdell" with an age of 53. The second
#instance should have a name of "Mrs. Burdell" with an age
#of 53 as well. Finally, make an instance with the name of
#"George P. Burdell" with an age of 25. This final instance
#should also have the father attribute set to the instance 
#of Mr. Burdell, and the mother attribute set to the 
#instance of Mrs. Burdell. Finally, store the instance of 
#George P. Burdell in a variable called george_p. (It does
#not matter what variable names you use for Mr. and Mrs.
#Burdell.)

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

#Write your code here!
first_instance = Person("Mr. Burdell", 53)
second_instance = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, first_instance, second_instance)




#The code below will let you test your code. It isn't used
#for grading, so feel free to modify it. As written, it
#should print George P. Burdell, Mrs. Burdell, and Mr.
#Burdell each on a separate line.
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)


