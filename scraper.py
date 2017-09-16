#!/usr/bin/env python

"""
    A simple script that should scrape courses available on https://onlinecourses.ooo
    Still work in progress, so yeah.. not much features for now!
"""

import requests
import sys
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

display_template = """
=========================================================================
Title: {title}
    Description: {description}

Creation Date: {creation_date}
Categories: {categories}
=========================================================================
"""

def get_request(url, page_number=1):
    url = url.format(page_number=page_number)

    course_request = requests.get(url, verify=False)

    if not course_request.status_code == 200:
        return False
    else:
        return course_request

def get_courses(soup):
    course_soup = soup

    return course_soup.findAll('div', {'class': 'item-frame'})

def get_course_details(course):
    details = {}
    categories = []

    for item_detail in course.findAll('div', {'class': 'item-panel'}):
        details['title'] = item_detail.find('h3', {'class': 'entry-title'}).text.encode('utf8')
        details['description'] = item_detail.find('p', {'class': 'desc entry-content'}).text.encode('utf8')

    for item_date in course.findAll('div', {'class': 'calendar'}):
        details['creation_date'] = item_date.find('time', {'class': 'entry-date published'}).text.encode('utf8')

    for item_taxonomy in course.findAll('div', {'class': 'taxonomy'}):
        for category in item_taxonomy.find('p', {'class': 'category'}).findAll('a'):
            categories.append(category.text.encode('utf8'))

    details['categories'] = categories

    return details

def main():
    url = "http://onlinecourses.ooo/page/{page_number}"
    num_of_pages = int(sys.argv[1]) if len(sys.argv[1]) > 0 else 1
    items = 0

    for i in range(1, num_of_pages + 1):
        course_request = get_request(url, page_number=i)
        course_soup = BeautifulSoup(course_request.text, 'html.parser')
        courses = get_courses(course_soup)

        for course in courses:
            details = get_course_details(course)

            print display_template.format(title=details['title'], description=details['description'], creation_date=details['creation_date'], categories=', '.join(details['categories']))

            items = items + 1

    print "Total number of courses: {items}".format(items=items)

if __name__ == '__main__':
    main()
