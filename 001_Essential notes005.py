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




#problem7_Hamlet Sentence Generator
"""
006 e0 创建一个LIST OF LIST，每一个LIST都对应STRING中的某一句
"""
#Sentences end with '.', '?', and '!'.
#You should convert all letters to lowercase.
#For each word, strip out any punctuation.

hamsplits[0] == ['and', 'can', 'you', 'by', ..., 'dangerous', 'lunacy']
hamsplits[-1] == ['madness', 'in', 'great', ..., 'not', 'unwatchd', 'go']

hamlet_text = """
And can you by no drift of circumstance Get from him why he puts on this confusion Grating so harshly all his days of 
quiet With turbulent and dangerous lunacy? He does confess he feels himself distracted. But from what cause he will by 
no means speak. Nor do we find him forward to be sounded But with a crafty madness keeps aloof When we would bring 
him on to some confession Of his true state. Did he receive you well? Most like a gentleman. But with much forcing of 
his disposition. Niggard of question. but of our demands Most free in his reply. Did you assay him? To any pastime? 
Madam it so fell out that certain players We o'er-raught on the way. of these we told him. And there did seem in him a 
kind of joy To hear of it. they are about the court And as I think they have already order This night to play before 
him. 'Tis most true. And he beseech'd me to entreat your majesties To hear and see the matter. With all my heart. and 
it doth much content me To hear him so inclined. Good gentlemen give him a further edge And drive his purpose on to 
these delights. We shall my lord. Sweet Gertrude leave us too. For we have closely sent for Hamlet hither That he as 
'twere by accident may here Affront Ophelia. Her father and myself lawful espials Will so bestow ourselves that seeing 
unseen We may of their encounter frankly judge And gather by him as he is behaved If 't be the affliction of his love 
or no That thus he suffers for. I shall obey you. And for your part Ophelia I do wish That your good beauties be the 
happy cause Of Hamlet's wildness. so shall I hope your virtues Will bring him to his wonted way again To both your 
honours. Madam I wish it may. Ophelia walk you here. Gracious so please you We will bestow ourselves. Read on this 
book. That show of such an exercise may colour Your loneliness. We are oft to blame in this 'Tis too much proved that 
with devotion's visage And pious action we do sugar o'er The devil himself. O 'tis too true! How smart a lash that 
speech doth give my conscience! The harlot's cheek beautied with plastering art Is not more ugly to the thing that 
helps it Than is my deed to my most painted word. O heavy burthen! I hear him coming. let's withdraw my lord. To be 
or not to be. that is the question. Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous 
fortune Or to take arms against a sea of troubles And by opposing end them? To die. to sleep. No more. and by a sleep 
to say we end The heart-ache and the thousand natural shocks That flesh is heir to 'tis a consummation Devoutly to be 
wish'd. To die to sleep. To sleep. perchance to dream. ay there's the rub. For in that sleep of death what dreams may 
come When we have shuffled off this mortal coil Must give us pause. there's the respect That makes calamity of so long 
life. For who would bear the whips and scorns of time The oppressor's wrong the proud man's contumely The pangs of 
despised love the law's delay The insolence of office and the spurns That patient merit of the unworthy takes When he 
himself might his quietus make With a bare bodkin? who would fardels bear To grunt and sweat under a weary life But 
that the dread of something after death The undiscover'd country from whose bourn No traveller returns puzzles the 
will And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make 
cowards of us all. And thus the native hue of resolution Is sicklied o'er with the pale cast of thought And 
enterprises of great pith and moment With this regard their currents turn awry And lose the name of action. Soft you 
now! The fair Ophelia! Nymph in thy orisons Be all my sins remember'd. Good my lord How does your honour for this 
many a day? I humbly thank you. well well well. My lord I have remembrances of yours That I have longed long to 
re-deliver. I pray you now receive them. No not I. I never gave you aught. My honour'd lord you know right well you 
did. And with them words of so sweet breath composed As made the things more rich. their perfume lost Take these 
again. for to the noble mind Rich gifts wax poor when givers prove unkind. There my lord. Ha ha! are you honest? My 
lord? Are you fair? What means your lordship? That if you be honest and fair your honesty should admit no discourse 
to your beauty. Could beauty my lord have better commerce than with honesty? Ay truly. for the power of beauty will 
sooner transform honesty from what it is to a bawd than the force of honesty can translate beauty into his likeness. 
this was sometime a paradox but now the time gives it proof. I did love you once. Indeed my lord you made me believe 
so. You should not have believed me. for virtue cannot so inoculate our old stock but we shall relish of it. I loved 
you not. I was the more deceived. Get thee to a nunnery. why wouldst thou be a breeder of sinners? I am myself 
indifferent honest. but yet I could accuse me of such things that it were better my mother had not borne me. I am 
very proud revengeful ambitious with more offences at my beck than I have thoughts to put them in imagination to give 
them shape or time to act them in. What should such fellows as I do crawling between earth and heaven? We are arrant 
knaves all. believe none of us. Go thy ways to a nunnery. Where's your father? At home my lord. Let the doors be shut 
upon him that he may play the fool no where but in's own house. Farewell. O help him you sweet heavens! If thou dost 
marry I'll give thee this plague for thy dowry. be thou as chaste as ice as pure as snow thou shalt not escape 
calumny. Get thee to a nunnery go. farewell. Or if thou wilt needs marry marry a fool. for wise men know well enough 
what monsters you make of them. To a nunnery go and quickly too. Farewell. O heavenly powers restore him! I have 
heard of your paintings too well enough. God has given you one face and you make yourselves another. you jig you 
amble and you lisp and nick-name God's creatures and make your wantonness your ignorance. Go to I'll no more on't. 
it hath made me mad. I say we will have no more marriages. those that are married already all but one shall live. the 
rest shall keep as they are. To a nunnery go. O what a noble mind is here o'erthrown! The courtier's soldier's 
scholar's eye tongue sword. The expectancy and rose of the fair state The glass of fashion and the mould of form The 
observed of all observers quite quite down! And I of ladies most deject and wretched That suck'd the honey of his 
music vows Now see that noble and most sovereign reason Like sweet bells jangled out of tune and harsh. That 
unmatch'd form and feature of blown youth Blasted with ecstasy. O woe is me To have seen what I have seen see what I 
see! Love! his affections do not that way tend. Nor what he spake though it lack'd form a little Was not like madness. 
There's something in his soul O'er which his melancholy sits on brood. And I do doubt the hatch and the disclose Will 
be some danger. which for to prevent I have in quick determination Thus set it down. he shall with speed to England 
For the demand of our neglected tribute Haply the seas and countries different With variable objects shall expel 
This something-settled matter in his heart Whereon his brains still beating puts him thus From fashion of himself. 
What think you on't? It shall do well. but yet do I believe The origin and commencement of his grief Sprung from 
neglected love. How now Ophelia! You need not tell us what Lord Hamlet said. We heard it all. My lord do as you 
please. But if you hold it fit after the play Let his queen mother all alone entreat him To show his grief. let her 
be round with him. And I'll be placed so please you in the ear Of all their conference. If she find him not To England 
send him or confine him where Your wisdom best shall think. It shall be so. Madness in great ones must not unwatch'd 
go.
"""

hamsplits = []

def hamsplits__soln1():
    global hamsplits
    cleaned_0 = hamlet_text.lower().replace("?", ".").replace("!", ".")
    cleaned_1 = ''.join([c for c in cleaned_0 if c.isalpha() or c.isspace() or c == '.'])
    sentences = cleaned_1.split(".")
    hamsplits = [s.split() for s in sentences]
    if not hamsplits[-1]: # "... go." -> extra sentence
        hamsplits = hamsplits[:-1]  #delete the last  []

hamsplits__soln1()


"""

"""





