from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

URL = 'https://www.adelaide.edu.au/course-outlines/104852/1/sem-1/'
html = urlopen(URL)

#Using beautiful soup to decode the URL webpage
soup = BeautifulSoup(html, "lxml")

#Locating the keywords that we want to extract

course_code = soup.find("div", class_ = "detail-data-content").find("th", string = "Course Code").next_sibling.next_sibling.get_text()
course_name = soup.find("div", class_ = "detail-data-content").find("th", string = "Course").next_sibling.next_sibling.get_text()
description = soup.find("div", class_ = "detail-data-content").find("th", string = "Course Description")
knowledge = soup.find("div", class_ = "detail-data-content").find("th", string = "Assumed Knowledge")
prerequisites = soup.find("div", class_ = "detail-data-content").find("th", string = "Prerequisites")

#Judging if the description, knowledge and prerequisites exist, if not, then display None

if description is None:
	description = "None"
else:
	description = description.next_sibling.next_sibling.get_text()

if knowledge is None:
	knowledge = "None"
else:
	knowledge = knowledge.next_sibling.next_sibling.get_text()

if prerequisites is None:
	prerequisites = "None"
else:
	prerequisites = prerequisites.next_sibling.next_sibling.get_text()

#Saving all the information as an one row data

data = [course_code, course_name, description, knowledge, prerequisites]

#Writing to the csv file

with open('database.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(data)