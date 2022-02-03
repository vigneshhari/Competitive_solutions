for i in xrange(input()):
    a , b = raw_input().split()
    try:
        b = int(b)
    except:
        print "Error Code: invalid literal for int() with base 10: '{}'".format(b)
        continue
    try:
        a = int(a)
    except:
        print "Error Code: invalid literal for int() with base 10: '{}'".format(a)
        continue

    if(b == 0):
        print "Error Code: integer division or modulo by zero"
    else:
        print a / b
