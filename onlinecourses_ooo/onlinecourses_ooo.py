# -*- coding: utf-8 -*-

"""OnlineCourses Scraper

Usage:
    onlinecourses (-h | --help)
    onlinecourses get [options]

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
    onlinecourses get --pages=5
    onlinecourses get --courses=5
"""

import requests
from bs4 import BeautifulSoup
from docopt import docopt
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

site = 'https://onlinecourses.ooo/page/{page}'
print_template = """
{sep}
Title: {title}
    Description: {description}

    Creation Date: {creation_date}
    Categories: {categories}
    Udemy Link: {udemy_link}
{sep}
"""


def fetch_request(url):
    """Fetches request without SSL verification."""
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,fil;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'onlinecourses.ooo',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
    }
    return requests.get(url, verify=False, headers=headers)


def fetch_pages(pages=1):
    """Fetches the page and generates a soup for each page."""
    page_soups = []

    for page in range(pages):
        response = fetch_request(site.format(page=page + 1))
        soup = BeautifulSoup(response.text, 'lxml')
        page_soups.append(soup)

    return page_soups


def fetch_courses(soups):
    """Fetches each course inside a given page."""
    courses = []
    for soup in soups:
        course = soup.find_all('div', class_='item-frame')
        courses.append(course)

    return courses


def parse_course_details(course_pages):
    """Parses the course details and returns the details as a dictionary."""
    course_details = []

    for course_page in course_pages:
        for course in course_page:
            details = {}
            item_panel = course.find('div', class_='item-panel')

            details['title'] = item_panel.find('h3', class_='entry-title').text
            details['description'] = item_panel.find('p', class_='entry-content').text
            details['creation_date'] = course.find('div', class_='calendar').find('time', class_='entry-date published').text
            course_categories = course.find('div', class_='taxonomy').find('p', class_='category').find_all('a')
            details['categories'] = [category.text for category in course_categories]
            course_url = course.find('h3', class_='entry-title').find('a').get('href')
            details['udemy_link'] = parse_udemy_course_url(course_url)
            course_details.append(details)

    return course_details


def parse_udemy_course_url(course_url):
    """Parses or generates a udemy course url of a given link inside a page."""
    response = fetch_request(course_url)
    course_soup = BeautifulSoup(response.text, 'lxml')

    link = course_soup.find('div', class_='link-holder').find('a').get('href')

    if "udemy" in link:
        return link

    udemy_link = fetch_request(link)
    if udemy_link.status_code == 200:
        return udemy_link.url

    return "Not available."


def print_courses(course_details):
    """Display the course details on the console."""
    for course in course_details:
        print(print_template.format(sep="=" * 79, title=course['title'], description=course['description'], categories=course['categories'], udemy_link=course['udemy_link'], creation_date=course['creation_date']))


def main():
    args = docopt(__doc__, options_first=False)
    pages = int(args.get('--pages'))
    # add_interest = args.get('--add-interests')
    # courses = int(args.get('--courses'))

    page_soups = fetch_pages(pages)
    course_pages = fetch_courses(page_soups)
    course_details = parse_course_details(course_pages)
    print_courses(course_details)


if __name__ == '__main__':
    main()
