#Below is a class representing a person. You'll see the
#Person class has three instance variables: name, age,
#and GTID. The constructor currently sets these values
#via a calls to the setters.
#
#Create a new function called same_person. same_person
#should take two instances of Person as arguments, and
#returns True if they are the same Person, False otherwise.
#Two instances of Person are considered to be the same if
#and only if they have the same GTID. It does not matter
#if their names or ages differ as long as they have the
#same GTID.
#
#You should not need to modify the Person class.

class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
       return self.age

    def get_GTID(self):
        return self.GTID

#Add your code below!
def same_person(first_person, second_person):
    if first_person.GTID == second_person.GTID:
        return True
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False.
person1 = Person("David Joyner", 30, 901234567)
person2 = Person("D. Joyner", 29, 901234567)
person3 = Person("David Joyner", 30, 903987654)
print(same_person(person1, person2))
print(same_person(person1, person3))



