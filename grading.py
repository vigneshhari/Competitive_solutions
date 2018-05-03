inp = input()
for _ in range(inp):
    val = input()
    if(val < 38 ):print val ; continue
    temp = (((val / 5) + 1 ) * 5)
    if( temp  - val  <= 2   ):
        print temp;continue
    print val