# File Handling in python

# File Opening
f = open("test-file-1.txt","w")
f.write("Line 1:This is the line in test-file-1.txt\n")
f.write("Line 2:This is the line in test-file-1.txt")

f = open("test-file-1.txt","a")
for i in range(1,1001):
    f.write(str(i) + " Line 1 \n")

for i in range(1001,1101):
    f.write(str(i) + " Line 2 \n")

f = open("test-file-1.txt","r")
print(f.read())
print(f.read(10))
print(f.read(20))
print(f.read(30))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
try:
    with open("test-file1.txt") as f:
        print(f.read())
except Exception as e:
    print(e)

import os
os.remove("test-file-1.txt")
