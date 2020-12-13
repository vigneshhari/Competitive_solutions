for _ in range(input()):
    input()
    lis = map(int , raw_input().split())
    print ((3 * sum(set(lis))) - (sum(lis)))/2
