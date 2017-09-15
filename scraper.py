#!/usr/bin/env python

"""
    A simple script that should scrape courses available on https://onlinecourses.ooo
    Still work in progress, so yeah.. not much features for now!
"""

import requests
import sys
from bs4 import BeautifulSoup

url = "http://onlinecourses.ooo"

courses_request = requests.get(url, verify=False)

print courses_request.status_code

course_soup = BeautifulSoup(courses_request.text, 'html.parser')

items = 0

for link in course_soup.findAll('div', {'class': 'item-frame'}):

    details = {}

    for item_panel in link.findAll('div', {'class': 'item-panel'}):
        title = item_panel.find('h3', {'class': 'entry-title'}).text
        description = item_panel.find('p', {'class': 'desc entry-content'}).text

        details['title'] = title.encode('utf8')
        details['description'] = description.encode('utf8')

    for item_date in link.findAll('div', {'class': 'calendar'}):
        creation_date = item_date.find('time', {'class': 'entry-date published'}).text
        details['creation_date'] = creation_date.encode('utf8')

    categories = []

    for item_taxonomy in link.findAll('div', {'class': 'taxonomy'}):
        for category in item_taxonomy.find('p', {'class': 'category'}).findAll('a'):
            categories.append(category.text.encode('utf8'))

        details['categories'] = categories
    items = items + 1

    print """
    Title: {title}
    Description: {description}
    Creation Date: {creation_date}
    Categories: {categories}
    """.format(title=details['title'], description=details['description'], creation_date=details['creation_date'], categories=', '.join(details['categories']))

print "Total number of courses: {items}".format(items=items)
