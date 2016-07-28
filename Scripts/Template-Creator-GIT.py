# Referenced from - https://packetpushers.net/python-jinja2-tutorial/
import os
import jinja2
import csv
import sys

# Variables 
# Change the file paths as needed. 
# DON'T use an absolute path to the template - Jinja expects a directory
# Must use quotes to string the path
# Files may be sent to the C:\Users\User directory
TemplateDirectory = 'C:\\Users\\USER\\PATH\\TO\\DIRECTORY\\'
CSVDATA = 'C:\\Users\\USER\PATH\\TO\\CSVFILE.csv'

# The jinja2.FileSystemLoader() is where you'll input the directory path or variable holding the path
# If entering the path manually, use quotes to string the path.
# If using a variable, don't input as a string. The variable already holds a string'd path
env = jinja2.Environment(loader=jinja2.FileSystemLoader(TemplateDirectory))

# Specify the template located inside the referenced directory. 
template = env.get_template('TEMPLATE-FILENAME.txt')

# 1. Python will open the CSVDATA file
# 2. Take the values under each header (first row in the CSV) and output a new .txt file with the template variables being substituted for the CSV values in each row
# 3. The newly created .txt files will have the hostname set as the .txt file's name
# 4. Each row in the CSV will create a .txt file that'll be saved in the directory you specified for the jinja2.FileSystemLoader()
for row in csv.DictReader(open(CSVDATA)):
	with open (row['hostname']+'.txt', 'w+') as opencsv:
		opencsv.write(template.render(row))