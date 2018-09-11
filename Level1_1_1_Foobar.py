def answer(area):
    lis = []
    while area>0:
        val = int(area ** 0.5) ** 2
        lis.append(val)
        area -=val
    return lis
