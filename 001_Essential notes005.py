#problem5_AirBnB-TX

"""
001 e0 从一个LIST中，去除掉$， 且将string转成integer
"""
[['$27', 'https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX'],
 ['$149', 'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX'],
 ['$59', 'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX'],
 ['$60', 'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX'],
 ['$75', 'https://www.airbnb.com/rooms/17325114?location=Colleyville%2C%20TX']]

prices = ['$27' , '$149' , '$59' , '$60' , '$75']
convertint(prices) == [27 , 149 , 59 , 60 , 75]

def convertint(prices):
   return [int(i.split("$")[1]) for i in prices]

[i.split("$") for i in prices] #--> [['', '27'], ['', '149'], ['', '59'], ['', '60'], ['', '75']]
[i.split("$")[1] for i in prices] #--> ['27', '149', '59', '60', '75']


"""
002 e1 从一个包含多个URL的LIST中，找出CITY名
"""
urls = ['https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX',
        'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX',
        'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX',
        'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX']

parseurls(urls) == ['Cleveland','Cibolo','Beach City','College Station']

import re
def parseurl(urls):
    raw_locs = get_raw_locations(urls)
    cities = clean_raw_locations(raw_locs)
    return cities
   
def get_raw_locations(urls):
    locs = []
    for url in urls:
        start = re.search('location=', url).span()[1]     #without[1], then (38, 47) (38, 47) (38, 47) (38, 47)
        stop = re.search('%2C', url).span()[0]  #without[0], then (56, 59) (53, 56) (59, 62) (64, 67) 
        locs.append(url[start:stop])
    return locs   #['Cleveland', 'Cibolo', 'Beach%20City', 'College%20Station']

def clean_raw_locations(locs):
    cleaned = []
    for raw_loc in locs:
        cleaned.append(' '.join(raw_loc.split('%20')))
    return cleaned   #['Cleveland', 'Cibolo', 'Beach City', 'College Station']


