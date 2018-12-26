#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.
#
#Write a class called ExerciseSession. ExerciseSession
#should have a constructor that requires two strings and an
#integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or
#"High". The integer will represent the length of the
#exercise session in minutes. These should be saved in the
#instance of the class.
#
#Then, add three getters to the class. The getters should
#be named get_exercise, get_intensity, and get_duration,
#and should return the exercise string, the exercise
#intensity, and the duration, respectively.
#
#The setters should be named set_exercise, set_intensity,
#and set_duration. Each should have one parameter (besides
#self), which should be stored as the new value of
#exercise, intensity, or duration. You may assume only
#valid values will be passed in.
#
#HINT: You don't have to do any logging like you saw in
#the video! That was just an example of one benefit of
#using getters and setters, but this problem does not ask
#you to do that.


#Add your code here!
class ExerciseSession:
    
    #Next, we create the constructor, just as before. This time,
    #we'll use the same parameter names as the attribute names,
    #but remember we don't _have_ to do this:
    def __init__(self, exercise, intensity, duration):
        
        #Next, we create each attribute. Remember, attributes
        #must start with self. -- this is what allows them to
        #persist after the method is done running.
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration
    
    #Now, we need to create our getters. There will be three,
    #one for each attribute. Each getter takes no parameters
    #besides self because you don't need to give a getter any
    #input to get something back.
    def get_exercise(self):
        
        #Then, all each getter has to do is return the
        #attribute. We _could_ do other stuff, but we don't
        #have to do anything but this:
        return self.exercise
    
    #The other two getters follow the exact same pattern:
    def get_intensity(self):
        return self.intensity
    
    def get_duration(self):
        return self.duration
    
    #Now we implement the setters. Like the getters, these
    #follow a template. Each one will have two parameters:
    #self, and the new value for the corresponding
    #attribute:
    def set_exercise(self, new_exercise):
        
        #The only thing a setter needs to do is assign a
        #new value to that attribute. It does not need to
        #return anything:
        self.exercise = new_exercise
    
    #Again, the other setters follow the same pattern:
    def set_intensity(self, new_intensity):
        self.intensity = new_intensity
        
    def set_duration(self, new_duration):
        self.duration = new_duration
        


#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#Running
#Low
#60
#Swimming
#High
#30
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())




