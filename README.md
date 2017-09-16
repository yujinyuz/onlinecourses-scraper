# onlinecourses-scraper
My personal scraper for https://onlinecourses.ooo

# Summary

This should serve my personal needs for scraping data from https://onlinecourses.ooo.

It should display stuffs that I'm interested to.

**Still work in progress..**

# Usage

First create a virtualenv (I prefer using virtualenvwrapper):

`pip install virtualenvwrapper`

Then do:

`mkvirtualenv scraper`
`workon scraper`

If the above says `command not found` try executing

```
source `which virtualenvwrapper.sh`
``` 
To scrape courses, type:

`python scraper.py` or `./scraper.py`
