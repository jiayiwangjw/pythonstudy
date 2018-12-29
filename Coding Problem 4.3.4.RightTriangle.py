#Write a function called solve_right_triangle. The function
#solve_right_triangle should have three parameters: opposite, 
#adjacent, and use_degrees. opposite and adjacent will be
#floats, and use_degrees will be a boolean. use_degrees
#should be a keyword parameter, and it should have a
#default value of False.
#
#The function should return a tuple containing the
#hypotenuse and angle of the right triangle (in that order).
#If use_degrees is False, the angle should be in radians.
#If use_degrees is True, the angle should be in degrees.
#
#Remember, the formula for the hypotenuse of a right
#triangle is the square root of the sum of the squared side
#lengths. You can find arctan using math.atan(), passing in
#the quotient of the opposite and adjacent as the argument.
#By default, math.atan() returns the angle in radians; you
#can pass that angle as an argument into the math.degrees()
#method to convert it to degrees; for example:
#
# angle_in_degrees = math.degrees(angle_in_radians)

import math

'''
#Write your function here!
def solve_right_triangle(opposite, adjacent, use_degrees=False):
    tuple1=()
    if use_degrees == False:
        tuple1 = (math.sqrt(opposite**2+adjacent**2), math.degrees(opposite/adjacent))
    else:
        tuple1 = (math.sqrt(opposite**2+adjacent**2), math.atan(opposite/adjacent))
        
    return tuple1
'''
def solve_right_triangle(opposite, adjacent, use_degrees = False):
    hypotenuse = (opposite ** 2 + adjacent ** 2) ** 0.5
    
    angle = math.atan(opposite / adjacent)
    
    if use_degrees == True:
        angle = math.degrees(angle)
        
    return (hypotenuse, angle)




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(5.0, 0.6435011087932844)
#(5.0, 36.86989764584402)
print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees = True))


