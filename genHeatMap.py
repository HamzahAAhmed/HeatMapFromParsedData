#!/usr/bin/env python3
#date = str(input("Enter Date (YYYY-MM-DD Format): "))
#time = str(input("Enter Time (HH:MM:SS Milatary Format) "))
date = "2019-09-04"
time = "09:10:00"
#opens file with data for input date
file = open(date+".txt", "r")
lines = file.readlines()
lines.sort()
linesAtTime = []

#find all temperatures at time input
for line in lines:
    current = line.split()
    if current[2]==time:
        linesAtTime.append(current)
file.close()

for i in linesAtTime:
    print(i[4])

temperature = []
for i in linesAtTime:
    temperature.append(float(i[4]))
f = open("temp1.txt", "w+")
for i in temperature:
    f.write(str(i) + ", ")
f.close()