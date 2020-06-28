import csv
import json
import pandas as pd

"""f = open('edges.csv', 'r+')
for line in f.readlines():
    s=line.split(',')
    with open('SIM_edges.csv','a',newline='') as employee_file:
        if(s[0]=="18" or s[1]=="18"):
            employee_writer=csv.writer(employee_file)
            employee_writer.writerow([s[0],s[1],1])

f.close()"""
    
csvFilePath = "SIM_edges.csv"
jsonFilePath = "SIM_edges.json"
arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    #print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
