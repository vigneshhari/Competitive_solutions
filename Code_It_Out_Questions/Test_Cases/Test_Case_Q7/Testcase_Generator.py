import random

file1 = open("1" , "r+")
file1.write("10\n")
for i in range(10):
    file1.write(str(random.randint(10, 15)) + " ") 
file1.close()


file2 = open("2" , "r+")
file2.write("20\n")
for i in range(20):
    file2.write(str(random.randint(50, 58)) + " ") 
file2.close()


file3 = open("3" , "r+")
file3.write("50\n")
for i in range(50):
    file3.write(str(random.randint(50, 60)) + " ") 
file3.close()


file4 = open("4" , "r+")
file4.write("100\n")
for i in range(100):
    file4.write(str(random.randint(100, 120)) + " ") 
file4.close()


file5 = open("5" , "r+")
file5.write("100\n")
for i in range(100):
    file5.write(str(random.randint(840, 880)) + " ") 
file5.close()
