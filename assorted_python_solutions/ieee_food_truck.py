import sys
from math import radians, cos, sin, asin, sqrt


def distance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    diflon = lon2 - lon1
    diflat = lat2 - lat1
    temp1 = sin(diflat/2)**2 + cos(lat1) * cos(lat2) * sin(diflon/2)**2
    temp2 = 2 * asin(sqrt(temp1))
    dist = 6378.137 * temp2
    return dist
'''
18.9778972,72.8321983
1.0
Date&Time,Latitude,Longitude,PhoneNumber
10/21/2016 13:34,18.912875,72.822318,9020320100
10/21/2016 10:35,18.9582233,72.8275845,9020320024
10/21/2016 15:20,18.95169982,72.83525604,9020320047
10/21/2016 15:23,18.9513048,72.8343388,9020357980

'''

print  distance(18.9778972,72.8321983, 18.97523003,72.83494865)
orglat , orglong = [float(x) for x in raw_input().split(" ")]
dis = float(raw_input())
raw_input()


