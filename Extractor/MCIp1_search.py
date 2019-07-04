from urllib.request import urlopen

from bs4 import BeautifulSoup

import re

print("Please enter the parameter that you want to extraxt on the course-outlines: ")

input = input()

parts = ['https://www.adelaide.edu.au/course-outlines/search/?vs=','&search=Search&adv_acad_career=0&adv_campus=0&adv_year=0&adv_subject=0&adv_course_type=0&adv_termid=0']

url = input.replace(' ','+').join(parts)

html = urlopen(url)

soup = BeautifulSoup(html, "lxml")

courses = soup.find_all("a", href=re.compile("/course-outlines/"))

for course in courses:
	print(course.get_text()[-1])
	if "Semester" in course.get_text() or "Trimester" in course.get_text():
		print("https://www.adelaide.edu.au" + course['href'])