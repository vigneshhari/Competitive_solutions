def fib(limit):
  if (limit < 2):
    return 1;
  n_1 = 1
  n_2 = 1;
  times = 2
  sum = 2
  while True :
    n_new = n_1 + n_2;
    n_1 = n_2;
    n_2 = n_new;
    sum += n_new
    if(sum > limit ):break
    times += 1
  return times;

def power(limit):
    mul = 0
    sum  = 0
    while True:
        sum = sum + 2 ** mul
        if(sum > limit):break
        mul += 1
    sum = sum - 2 ** mul
    if(limit - sum >= (2** (mul-1) + 2** (mul -2)   )): mul+=1
    return mul

def answer(total_lambs):
    if total_lambs >= 10 and total_lambs <= 10 ** 9:
        return  fib(total_lambs) - power(total_lambs)
    return 0

print answer(13)

print "max " , fib(13)
print "min " , power(13)