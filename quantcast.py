import csv
from http.cookiejar import Cookie
import sys
# read the csv file

input_line = ""
for line in sys.stdin:
  input_line = line

file_name = ""
date = ""

for var in input_line.split("-d"):
  if file_name == "":
    file_name = var
  else:
    date = var

# strip white space:
file_name = file_name.strip(" ")
date = date.strip(" ")

cookie_dict = dict()
date_dict = dict()

with open(file_name) as csv_file:
  # delimiter will separate the cookie from its date
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    line_count += 1
    if line_count > 0:
      cookie = row[0]
      date, time = row[1].split("T")
      # check for cookie
      if cookie in cookie_dict:
        cookie_dict[cookie] += 1
      else:
        cookie_dict[cookie] = 1
      # check for date:
      if date in date_dict:
        date_dict[date].append(cookie)
      else:
        date_dict[date] = [cookie]

# now we can finally return the mostActiveCookie:
cookies = date_dict[date]
output = "" # separated by /n if there's multiple
mostActive = 1

for cookie in cookies:
  if cookie_dict[cookie] == mostActive:
    output += cookie
    output += "\n"
  elif cookie_dict[cookie] > mostActive:
    mostActive = cookie_dict[cookie]
    output = cookie + "\n"

sys.stdout(output[:-1]) # exclude the last \n
