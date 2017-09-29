#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OnlineCourses Scraper.

Usage:
    scraper.py (-h | --help)
    scraper.py get-courses [options]

Options:
    -h --help                   Show this screen.
    --version                   Show version.
    --pages=<num_of_pages>      Specify number of pages to be scraped.
                                [default: 1]
    --courses=<num_of_courses>  Specify number of courses to be scraped.
                                [default: 0]
    --add-interests             Prompt for topics that interests the user.
                                [default: False]

Examples:
    scraper.py --pages=5
    scraper.py --courses=3
    scraper.py --pages=2 --interests=Python, Javascript
    scraper.py --pages=3 --courses=12

Author:
    YujinYuz
"""

import logging
import requests
import sys
import urllib
from bs4 import BeautifulSoup
from docopt import docopt
from requests.packages.urllib3.exceptions import InsecureRequestWarning

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
logging.basicConfig(level=logging.INFO,
                    format=FORMAT)
logger = logging.getLogger(__name__)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

display_template = """
================================================================================
Title: {title}
    Description: {description}

    Creation Date: {creation_date}
    Categories: {categories}
    Udemy Link: {udemy_link}
================================================================================
"""


def is_connected():
    try:
        test_url = "https://www.google.com"
        urllib.urlopen(test_url)
    except:
        raise Exception('Error: Unable to connect to the internet.')
    else:
        logger.info("Connected to the internet. Proceeding...")
        return True

    return False

def get_request(url, page_number=1):
    url = url.format(page_number=page_number)

    try:
        page_request = requests.get(url, verify=False)

        if not page_request.status_code == 200:
            return False
        else:
            return page_request
    except Exception as e:
        logger.warning(e)


def get_course_soup(url):
    course_request = requests.get(url, verify=False)

    if not course_request.status_code == 200:
        return False
    else:
        return BeautifulSoup(course_request.text, 'html.parser')


def get_courses(soup):
    course_soup = soup

    return course_soup.findAll('div', {'class': 'item-frame'})


def get_course_details(course):
    details = {}

    item_detail = course.find('div', {'class': 'item-panel'})
    course_url = get_course_url(course)

    details['title'] = item_detail.find(
        'h3', {'class': 'entry-title'}).text.encode('utf8')
    details['description'] = item_detail.find(
        'p', {'class': 'entry-content'}).text.encode('utf8')
    details['creation_date'] = course.find('div', {'class': 'calendar'}).find(
        'time', {'class': 'entry-date published'}).text.encode('utf8')

    item_categories = course.find(
        'div', {
            'class': 'taxonomy'}).find(
        'p', {
            'class': 'category'}).findAll('a')

    details['categories'] = [ category.text.encode(
        'utf8') for category in item_categories ]
    details['udemy_link'] = get_udemy_course_url(course_url)

    return details


def get_udemy_course_url(course_url):
    course_soup = get_course_soup(course_url)
    udemy_link = ''
    link = course_soup.find('div', {'class': 'link-holder'}) \
                        .find('a') \
                        .get('href') \
                        .encode('utf8')

    if "udemy" in link:
        return link

    try:
        udemy_link = link.split('&')[2].split('=')[1]
        udemy_link = urllib.unquote(udemy_link).decode('utf8')
    except IndexError as e:
        logger.warning("Error occured. Unable to parse url: {url} - {exception}. Trying another method.".format(url=link, exception=e))
        try:
            udemy_link = requests.get(link)

            if udemy_link.status_code == 200:
                udemy_link = udemy_link.url.encode('utf8')
        except Exception as e:
            logger.warning("Still unable to parse url: {url} - {exception}.".format(url=link, exception=e))

    return udemy_link


def get_course_url(course):
    course_url = course.find(
        'h3', {'class': 'entry-title'}).find('a').get('href')
    return course_url

def display_to_screen(interests, details):
    interests = [ interest.strip() for interest in interests.split(',') ]

    display = [ interest for interest in interests if interest in details['categories'] ]

    for interest in interests:
        if interest in details['categories'] \
            or interest in details['title'] \
            or interest in details['description']:
                return True

    return False


def main():
    args = docopt(__doc__, version='v0.0.1')
    if not is_connected():
        raise

    url = "http://onlinecourses.ooo/page/{page_number}"
    num_of_pages = int(args['--pages'])
    num_of_courses = int(args['--courses'])
    add_interests = args['--add-interests']
    interests = ""

    if add_interests:
        print("Enter your interests using comma-separated values")
        interests = raw_input("> ")

    items = 0

    for page in range(num_of_pages):
        logger.info("Scraping...Page {page} of {pages}".format(
            page=page + 1,
            pages=num_of_pages))

        page_request = get_request(url, page_number=page + 1)
        page_soup = BeautifulSoup(page_request.text, 'html.parser')
        courses = get_courses(page_soup)

        for course in courses:
            details = get_course_details(course)

            if display_to_screen(interests, details):
                print(display_template).format(
                    title=details['title'],
                    description=details['description'],
                    creation_date=details['creation_date'],
                    categories=', '.join(details['categories']),
                    udemy_link=details['udemy_link'])

            if num_of_courses > 0:
                if items == num_of_courses:
                    break

            items = items + 1

    print("Total number of courses scraped: {items}".format(items=items))


if __name__ == '__main__':
    main()
