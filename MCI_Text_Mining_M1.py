from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import time

def extractor(URL):

	print(URL)

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

	print(course_name + " DONE!")


def main():

	print("Please enter the parameter that you want to extraxt on the course-outlines: ")

	parameter = input()

	print("Please enter the year that you want include")

	year = input()

	parts = ['https://www.adelaide.edu.au/course-outlines/search/?vs=','&search=Search&adv_acad_career=0&adv_campus=0&adv_year=0&adv_subject=0&adv_course_type=0&adv_termid=0']
	url = parameter.replace(' ','+').join(parts)

	#Using beautiful soup to decode the URL webpage
	html = urlopen(url)
	soup = BeautifulSoup(html, "lxml")

	#Extracting all the course URL
	courses = soup.find_all("a", href=re.compile("/course-outlines/"))

	#Wirte the title to the csv file
	title = ['course_id','course_name','course_detail','course_k','course_pr']

	with open('database.csv', 'a+') as f:
	    writer = csv.writer(f)
	    writer.writerow(title)
	f.close()

	for course in courses:

		#Filter out unnecessary information and send others to extractor
		if "Semester" in course.get_text() or "Trimester" in course.get_text():
			URL = "https://www.adelaide.edu.au" + course['href']
			if "2019" in year:
				if course.get_text()[-1] == "9":
					extractor(URL)
					time.sleep(1)
					continue
			if "2018" in year:
				if course.get_text()[-1] == "8":
					extractor(URL)
					time.sleep(1)
					continue
			if "2017" in year:
				if course.get_text()[-1] == "7":
					extractor(URL)
					time.sleep(1)
					continue
			if "2016" in year:
				if course.get_text()[-1] == "6":
					extractor(URL)
					time.sleep(1)
					continue
			if "2015" in year:
				if course.get_text()[-1] == "5":
					extractor(URL)
					time.sleep(1)
					continue
			if "2014" in year:
				if course.get_text()[-1] == "4":
					extractor(URL)
					time.sleep(1)
					continue

		#Protecting the server
		
			#print("https://www.adelaide.edu.au" + course['href'])


if __name__ == '__main__':
	main()