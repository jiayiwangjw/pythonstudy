#Imagine you're writing some code for an exercise tracker.
#The tracker measures heart rate, and should display the
#average heart rate from an exercise session.
#
#However, the tracker doesn't automatically know when the
#exercise session began. It assumes the session starts the
#first time it sees a heart rate of 100 or more, and ends
#the first time it sees one under 100.
#
#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).
#
#You may assume that the list will only cross the 100 beats
#per minute threshold once: once it goes above 100 and below
#again, it will not go back above.


#Add your function here!
def average_heart_rate(beats):
    j2 = [i for i in beats if i >= 100]
    result = sum(j2)//len(j2)
    return result

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))


