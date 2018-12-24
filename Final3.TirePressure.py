#Imagine you're writing the code for an onboard vehicle
#monitoring system. One thing the system does is measure
#tire pressure. It does this by taking a measurement every
#10 seconds. However, lots of environmental conditions can
#lead to intermittent bad readings: if it takes a reading
#as a car goes over a bump, for example, it will be way
#higher than it would have been otherwise. So, the system
#needs to know to ignore these ratings, as well as only
#process the more recent measurements. Let's tell the system
#that the only valid tire pressures are between 15 and 55.
#
#Write a function called tire_pressure. tire_pressure
#should have one parameter, a list of integers. The list
#represents a series of tire pressure measurements over the
#past several minutes.
#
#tire_pressure should return the average of the last 5
#measurements that are greater than or equal to 15 and less
#than or equal to 55. Round the result to 1 decimal place
#(you can use round(some_float, 1) to round to 1 decimal
#place).
#
#For example, if the list of measurements was this:
#
# [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
#
#tire_pressure would return 35.0: the last five measurements
#in range are all 35. You may assume there will be at least
#5 measurements in the proper range.


#Add your code here!
def tire_pressure(a_list):
    newlist = [i for i in a_list if i >= 15 and i <=55]
    newlist = newlist[-5:]
    sum1 = sum(newlist)
    avg = round(sum1/5,1)
    return avg


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 35.0
a_list = [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
print(tire_pressure(a_list))





