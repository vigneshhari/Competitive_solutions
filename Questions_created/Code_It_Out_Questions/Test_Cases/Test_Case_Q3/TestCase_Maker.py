
# Boundaries go from  1000
# File 1

import random

file1 = open("1", "r+")

file1.write("100\n")
 
for i in range(2,102):

    file1.write(str(random.randint(5, 100)) + "\n") 

# File 2 


file2 = open("2", "r+")

file2.write("500\n")

for i in range(2,502):

    file2.write(str(random.randint(5, 1000)) + "\n") 

file1.close()
file2.close()

#File 3

file3 = open("3", "r+")

file3.write("1000\n")

for i in range(2,1002):
    file3.write(str(random.randint(5, 10000)) + "\n") 

file3.close()

#File 4

file4 = open("4", "r+")

file4.write("5000\n")

for i in range(2,5002):
    file4.write(str(random.randint(5, 100000)) + "\n") 

#File 5

file5 = open("5", "r+")

file5.write("10000\n")

for i in range(2,10002):
    file5.write(str(random.randint(5, 100000)) + "\n") 

