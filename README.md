# onlinecourses-scraper
My personal scraper for https://onlinecourses.ooo

# Summary

This should serve my personal needs for scraping data from https://onlinecourses.ooo.

It should display stuffs that I'm interested to.

**Still work in progress..**

# Installation

First create a virtualenv (I prefer using virtualenvwrapper):

`pip install virtualenvwrapper`

Then do:

`mkvirtualenv scraper`
`workon scraper`

If the above says `command not found` try executing

```
source `which virtualenvwrapper.sh`
``` 

# Usage
```
OnlineCourses Scraper.

Usage:
    scraper.py (-h | --help)
    scraper.py --pages=<num_of_pages>
    scraper.py --courses=<num_of_courses>

Options:
    -h --help                   Show this screen.
    --version                   Show version.
    --pages=<num_of_pages>      Specify number of pages to be scraped.
    --courses=<num_of_courses>  Specify number of courses to be scraped.
```
