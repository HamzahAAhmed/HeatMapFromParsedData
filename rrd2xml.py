#!/usr/bin/env python

import os
from lxml import etree

subdirectories = []
temp = []
time = []

for root, dirs, files in os.walk("/dev/shm/heatmap/OpenHPC"):
    for i in dirs:
        if "compute" in i:
            subdirectories.append(i)

#for i in subdirectories:
#    os.system("cd /dev/shm/heatmap/OpenHPC/" + i + " && rrdtool dump cpu_temp.rrd cpu_temp.xml")

for i in subdirectories:
    with open(i+"/cpu_temp.xml") as f:
        doc = etree.parse(f)
    it = iter(doc.xpath(
        '//comment()[following-sibling::row] | //row/v/text()'
    ))
    for db_date, db_value in zip(it, it):
        with open("temperatureData.txt", 'a+') as f:
            f.write(i + " " + db_date.text.strip()[0:23] + " " +  db_value + "\n")
