carbon,hydrogen,oxygen = [int(x) for x in raw_input().split(" ")]
water = 0
gas = 0
glucose = 0
if (carbon,hydrogen,oxygen) == (0,0,0) or (carbon,hydrogen) == (0,0) or (hydrogen,oxygen) == (0,0) or (carbon,oxygen) == (0,0) or oxygen == 0:
    print 'Error'
    exit(0)
if hydrogen == 0:
    if oxygen == 2*carbon:
        co = carbon
    else:
        print 'Error'
        exit(0)
elif carbon == 0:
    if hydrogen == 2*oxygen:
        w = oxygen
    else:
        print 'Error'
else:
    glucose = carbon/6
    gas = carbon - (carbon/6)*6
    water = (hydrogen - (hydrogen / 12) * 12) / 2
print water,gas,glucose