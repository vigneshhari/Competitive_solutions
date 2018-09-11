
'''

Using Algebra to solve equation eliminating third variable for max efficiency


'''

for i in range(1,998):
    for j in range(i+1,998):
        temp = (1000 * i ) + (1000 *j) - (i*j)
        if(temp == 500000):print i * j * (1000 - i - j);break