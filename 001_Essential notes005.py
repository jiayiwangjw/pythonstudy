#problem5_AirBnB-TX

"""
001 e0 从一个LIST中，找出一个string，去除掉$
"""
[['$27', 'https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX'],
 ['$149', 'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX'],
 ['$59',
  'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX'],
 ['$60',
  'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX'],
 ['$75', 'https://www.airbnb.com/rooms/17325114?location=Colleyville%2C%20TX']]

prices = ['$27' , '$149' , '$59' , '$60' , '$75']
convertint(prices) == [27 , 149 , 59 , 60 , 75]

def convertint(prices):

