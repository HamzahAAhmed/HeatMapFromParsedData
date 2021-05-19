#!/usr/bin/env python
file = open("temperatureData.txt", "r")
lines = file.readlines()
saveLines = []
#Makes  a file for each day
for line in lines:
    current = line.split()
    print(current)
    newFile = open(current[1]+".txt", "a+")
    newFile.write(line)
    newFile.close()
file.close()
