__author__ = 'vignesh'

for i in range(0,input()):
    dogs,walkers = [int(x) for x in raw_input().split()]
    dog_size = []
    for t in range(dogs):
        dog_size.append(input())
    dog_size.sort()
    grp = dogs/walkers
    ans = 0
    for w in range(walkers-1):
        val = 0
        
        size = dog_size[:grp]
        ans = ans + max(size) - min(size)
        del dog_size[:grp]
        print dog_size
    ans = max(dog_size) - min(dog_size)
    print ans
