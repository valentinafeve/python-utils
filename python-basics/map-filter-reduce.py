import math
import statistics
from functools import reduce 

radios=[4,5,10,2.3,2.4]
areas=map(lambda r: r*r*math.pi,radios)
areasinlist=list(areas)
print(areasinlist)

data=[3,4.5,1.2,4.2,7.1,9,9,9]
avg=statistics.mean(data)
filtered=list(filter(lambda x: x<avg, data))
print(filtered)

countries=["Argentina","","Colombia","","Ecuador","Costa Rica",None]
countrieslist=list(filter(lambda filt: filt, countries))
print(countrieslist)

number=5
factorial=reduce(lambda n,m: n*m , [ x for x in range(1,number+1) ])
print(factorial)