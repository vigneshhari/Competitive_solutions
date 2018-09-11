
# Boundaries go from  200 , 10^3 , 10^4 , 10^5 , 10^7
# File 1

file1 = open("1" , "r+")

file1.write("100 200\n")
 
for i in range(2,102):

    file1.write(str(i) + "\n")

# File 2 

done = []

file2 = open("2" , "r+")

file2.write("200 1000\n")

for i in range(2,202):
    file2.write(str(i) + "\n")

file1.close()
file2.close()

#File 3

file3 = open("3" , "r+")

file3.write("200 10000\n")

for i in range(2,202):
    file3.write(str(i) + "\n")

file3.close()

#File 4

file4 = open("4" , "r+")

file4.write("10000 100000\n")

for i in range(2,10002):
    file4.write(str(i) + "\n")

