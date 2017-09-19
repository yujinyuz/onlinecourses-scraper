# onlinecourses-scraper
[![Build Status](https://travis-ci.org/YujinYuz/onlinecourses-scraper.svg?branch=develop)](https://travis-ci.org/YujinYuz/onlinecourses-scraper) [![codecov](https://codecov.io/gh/YujinYuz/onlinecourses-scraper/branch/develop/graph/badge.svg)](https://codecov.io/gh/YujinYuz/onlinecourses-scraper)
--------------------------------------
My personal scraper for https://onlinecourses.ooo

# Summary

This should serve my personal needs for scraping data from https://onlinecourses.ooo.

It should display stuffs that I'm interested to.

**Still work in progress..**

# Installation

First of all, clone this repository:
```
$ git clone https://github.com/YujinYuz/onlinecourses-scraper.git
$ cd onlinecourses-scraper
```

Then, create a virtualenv (I prefer using virtualenvwrapper):

`$ pip install virtualenvwrapper`

Then do:

```
$ mkvirtualenv scraper
$ workon scraper
```

If the above says `command not found` try executing

```
$ source `which virtualenvwrapper.sh`
``` 
After that, do:
```
$ pip install -r requirements.txt
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
# Sample Output

```
(scraper) yujin ~/Desktop/onlinecourses-scraper $ ./scraper.py --pages=1
[scraper.py:52 - is_connected()] Connected to the internet. Proceeding...
[scraper.py:137 - main()] Scraping...Page 1 of 1

================================================================================
Title: Learn Digital Art Photo Manipulation in Photoshop-Alone Girl
    Description: Learn Digital Art Photo Manipulation in Photoshop-Alone Girl, Transform Dull & Boring Images into Stunning Digital Artwork in Photoshop for Beginners.... more ››

    Creation Date: September 17, 2017
    Categories: 100% OFF Udemy Coupon, Online Classes, Photography
    Udemy Link: https://www.udemy.com/learn-photoshop-photo-manipulation-photoshop/?couponCode=STUDENTSZERO
================================================================================


================================================================================
Title: GCP – Google Cloud Platform Concepts
    Description: GCP - Google Cloud Platform Concepts, Google Cloud Platform GCP platform overview.Google Cloud Platform - GCP is fastest growing pubic Cloud Platform Services in the world.... more ››

    Creation Date: September 17, 2017
    Categories: 100% OFF Udemy Coupon, IT & Software, Online Classes
    Udemy Link: https://www.udemy.com/gcp-google-cloud-platform-concepts/
================================================================================


================================================================================
Title: eBay Drop Shipping Guide with no investment. Work From Home
    Description: eBay Drop Shipping Guide with no investment. Work From Home, Learn drop shipping from scratch. Making profit without investing a penny. List from Amazon,Argos, Walmart and Smyths.Welcome to Dr... more ››

    Creation Date: September 17, 2017
    Categories: 100% OFF Udemy Coupon, Business, Online Classes
    Udemy Link: https://www.udemy.com/drop-shipping-from-amazon150-store-to-ebaywork-from-home/
================================================================================


================================================================================
Title: Productive Vacations for Entrepreneurs
    Description: Productive Vacations for Entrepreneurs, Tips and Techniques for Getting the Most out of Your Time Away.Vacations and entrepreneurs may not mix, but getting out of the office can be one of the ... more ››

    Creation Date: September 17, 2017
    Categories: 100% OFF Udemy Coupon, Business, Online Classes
    Udemy Link: https://www.udemy.com/productive-vacations-for-entrepreneurs/
================================================================================


================================================================================
Title: Entrepreneurship 101: Understanding Entrepreneurship
    Description: Entrepreneurship 101: Understanding Entrepreneurship, This course is a quick introduction to entrepreneurship and a Beginners' guide to become an Entrepreneur.... more ››

    Creation Date: September 17, 2017
    Categories: 100% OFF Udemy Coupon, Business, Online Classes
    Udemy Link: https://www.udemy.com/entrepreneurship-theory-understanding-entrepreneurship/
================================================================================

Total number of courses scraped: 5

```
