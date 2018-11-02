"""


121 101 112 32 109 111 109 114 10 109 111 109 114 32 114 111 104 106 121 32 100 114 98 114 109
"""
'''
yep -> two
pmr -> one
momr -> nine
gobr -> five
rohjy -> eight
drbrm -> seven
xrtp -> zero

a b c d e f g h i j k l m n o p q r s t u v w x y z
- v - s w - f g - h - - n - i o - e - r - - - z t -

#t-19
#w-22
#o-14
'''

'''
2
yep momr
momr rohjy drbrm'''
'''
2
2 9
9 8 7
== 99999
'''
'''
3
yep pmr
pmr momr drbrm
yep xrtp gobr rohjy'''

'''
3
2 1
1 9 7
2 0 5 8
== 111222111
'''


map = { "xrtp": 0, "pmr": 1, "yep": 2, "yjtrr": 3, "gpit": 4, "gobr": 5, "doc": 6, "drbrm": 7, "rohjy": 8, "momr": 9, "yrm": 10, "rarbrm": 11,
"yerabr": 12, "yjotyrrm": 13, "gpityrrm": 14, "gogyrrm": 15, "docyrrm": 16, "drbrmyrrm": 17, "rohjyyrrm": 18, "momryrrm": 19, "yermyu": 20 }

def p(N):
    result = 1
    for n in range( int(N) ):
        arr = [ str(map[x]) for x in input().split() ]
        result *= int("".join(arr), 16)
    print (result)

p(input())

# I have found happiness
