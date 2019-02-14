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



"""
003 e2 给出一个数值范围，查找出LIST OF LIST中对应的LIST
"""
[[27, 'Cleveland'],
[149, 'Cibolo'],
[59, 'Beach City'],
[60, 'College Station'],
[75, 'Colleyville']]
 
filterdata(data, 50, 100) would return [[59, 'Beach City'], [60, 'College Station'], [75, 'Colleyville']]

def filterdata(data, low, high):
      return [i for i in data if i[0] >= low and i[0] <= high]   #i[0] 27 149 59 60 75
 
 
 
"""
004 e3 找出LIST中每个值的发生次数，输出为字典DICT
"""
findcount(['Cleveland','Austin','Dallas','Austin','Cleveland']) == {'Cleveland':2, 'Austin':2, 'Dallas':1}
 
def findcount(s):  #solution 1
     from collections import defaultdict
     items = defaultdict(int)
     for i in s:
        items[i] += 1
     return dict(items)

def findcount__version1(s):  #solution 2
     from collections import Counter
     return dict(Counter(s))
 
 
 
"""
005 e4 按价格范围，以字典的形式，排出搜索排前三名的城市
"""

result2 = {'Price 0-50': ['Coppell', 'Colleyville', 'Carrollton'],
           'Price 51-100': ['Bellaire', 'Alvin', 'Alamo Heights'],
           'Price 101-200': ['Bayou Vista', 'Center Point', 'Corpus Christi'], 
           'Price 201-10000': ['Baffin Bay', 'Burnet', 'Buchanan Dam']}


TopCities = {}
#

zerofifty = filterdata(Master_list,0,50)
fiftyhundred = filterdata(Master_list,51,100)
hundredtwohundred = filterdata(Master_list,101,200)
twohundredplus = filterdata(Master_list,201,10000)

def citiescounts(data):
        cities = [i[1] for i in data]
        cities_counts = findcount(cities)
        return cities_counts

zerofifty_citycounts = citiescounts(zerofifty)
fiftyhundred_citycounts = citiescounts(fiftyhundred)
hundredtwohundred_citycounts = citiescounts(hundredtwohundred)
twohundredplus_citycounts = citiescounts(twohundredplus)

def topthree(d):
    return sorted(d, key=d.get, reverse=True)[0:3]

top3_0_50 = topthree(zerofifty_citycounts)
top3_51_100 = topthree(fiftyhundred_citycounts)
top3_101_200 = topthree(hundredtwohundred_citycounts)
top3_200plus = topthree(twohundredplus_citycounts)

TopCities = {'Price 0-50':top3_0_50, 'Price 51-100':top3_51_100,
'Price 101-200':top3_101_200,'Price 201-10000':top3_200plus}
