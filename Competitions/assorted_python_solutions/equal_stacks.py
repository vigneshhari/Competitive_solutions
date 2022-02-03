raw_input()
stack1 = map(int , raw_input().split(" "))
stack2 = map(int , raw_input().split(" "))
stack3 = map(int , raw_input().split(" "))
sum1 = sum(stack1)
sum2 = sum(stack2)
sum3 = sum(stack3)
out = 0
while sum1 != sum2 or sum2 != sum3:
    if(sum1 >= sum2 and sum1 >= sum3):
        num = stack1[0]
        del stack1[0]
        sum1 -= num
    elif(sum2 >= sum3 and sum2 >= sum1):
        num = stack2[0]
        del stack2[0]
        sum2 -= num
    elif(sum3 >= sum1 and sum3 >= sum2):
        num = stack3[0]
        del stack3[0]
        sum3 -= num
    out += num

print sum1