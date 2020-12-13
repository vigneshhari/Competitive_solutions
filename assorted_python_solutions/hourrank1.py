for _ in range(input()):
    h0  , m0 ,h1 , m1 = map(int , raw_input().split())
    k = input()
    print (( (h0 + k) - h1 ) * 60) + (m0-m1) 