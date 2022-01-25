import csv
# read the csv file

# I am currently using python 2.XX but for python 3 
# use input instead of raw_input
# input_line = input("enter command = ")
input_line = raw_input("enter command = ")
file_name = ""
date = ""

for var in input_line.split("-d"):
  if file_name == "":
    file_name = var
  else:
    date = var

# strip white space:
file_name = file_name.strip(" ")
input_date = date.strip(" ")

date_dict = dict()
'''
date_dict = {
  2018-12-09: {"cookie #1": # of occurences of that day
  ...
              }
}
'''

output = "" # separated by /n if there's multiple
mostActive = 1
cookie_dict = dict() # dictionary of cookies found in the given date

with open(file_name) as csv_file:
  # delimiter will separate the cookie from its date
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
      cookie = row[0]
      date = row[1].split("T")[0]
      # once we have the cookie found in the given date:
      if date == input_date:
        if cookie in cookie_dict:
          cookie_dict[cookie] += 1
        else:
          cookie_dict[cookie] = 1

for cookie in cookie_dict:
  occurence = cookie_dict[cookie]
  if occurence == mostActive:
    output += cookie 
    output += "\n"
  elif occurence > mostActive:
    output = cookie + "\n"
    mostActive = occurence

print(output[:-1]) # exclude the last \n
