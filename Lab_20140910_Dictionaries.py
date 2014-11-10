#Lab: Data Munging - Dictionaries

import requests
import csv

web_request = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
web_data = web_request.text

#1. Get count of each instance of education (index 3)
reader = csv.reader(web_data.splitlines())

EdDict = {}
for row in reader:
	if row:
		if row[3] in EdDict:
			EdDict[row[3]] = EdDict[row[3]] + 1 #can also use EdCounter[row[3]] += 1
		else:
			EdDict[row[3]] = 1

print "Question 1: Count by Education"
for key, value in sorted(EdDict.iteritems()):
	print key+':', value

#2. Get count of combinations of gender and education (index 9)
reader = csv.reader(web_data.splitlines())

EdGendDict = {}
for row in reader:
	if row:
		if str(row[3])+str(row[9]) in EdGendDict:
			EdGendDict[str(row[3]) + str(row[9])] += 1 
		else:
			EdGendDict[str(row[3]) + str(row[9])] = 1

print '\n', "Question 2: Count by Gender/Education"
for key, value in sorted(EdGendDict.iteritems()):
	print key+':', value

#3. Find average hours per week (index 12) for groups above
reader = csv.reader(web_data.splitlines())

HrsDict = {}
for row in reader:
	if row:
		if str(row[3])+str(row[9]) in HrsDict:
			HrsDict[str(row[3]) + str(row[9])] += int(row[12])  
		else:
			HrsDict[str(row[3]) + str(row[9])] = int(row[12])

print '\n', "Question 3: Average Hours by Gender/Education"
for key, value in sorted(HrsDict.iteritems()):
	print key+':', value/EdGendDict[key]

#4. Is any sample size too small to have a meaningful average?

'''

Preschool Female=31 (n=16)
Preschool Male=38 (n=35)
1-4th Female=31 (n=46)
1-4th Male=40 (n=122)
12th Female=31(n=144)
12th Male=37 (n=289)

Sample sizes for these groups are on the smaller side as compared to 
other groups, simply comparing numbers in 2 and 3. 

'''


