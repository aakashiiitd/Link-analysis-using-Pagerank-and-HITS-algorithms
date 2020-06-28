import csv
import json
import pandas as pd
"""f = open('soc-Epinions1.txt', 'r+')
i=0
for line in f.readlines():
    if(i>=4):
        s=line.split()
        with open('edges.csv','a',newline='') as employee_file:
            employee_writer=csv.writer(employee_file)
            employee_writer.writerow([s[0],s[1],1])
    i=i+1
f.close()

with open('vertices.csv','w',newline='') as employee_file:
    i=0 
    while(i<76000):
        employee_writer=csv.writer(employee_file)
        employee_writer.writerow([i,i])
        i=i+1"""

csvFilePath = "edges.csv"
jsonFilePath = "edges.json"
arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    #print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
