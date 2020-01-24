import os
import datetime
from datetime import date

from bs4 import BeautifulSoup
import urllib.request

import csv
from itertools import zip_longest

# Transfer the URL into HTML for bs4
URL = "http://www.pfin.ca"
URL1 = "http://www.cbidmarkets.com/includes/leftColumn.html"

html_doc = urllib.request.urlopen(URL1)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def clean_none(lst: list):
    for item in lst:
        if item is None:
            lst.remove(item)

def get_word(lst: list):
    words = []
    for item in lst:
        words.append(item.get_text())

    return words

def csv_by_column(file_name, data):
    export_data = zip_longest(*data, fillvalue='')
    with open(file_name, 'w', encoding="ISO-8859-1", newline='') as my_file:
        wr = csv.writer(my_file)
        wr.writerows(export_data)
    my_file.close()

def check_work():
    global f, journal
    try:
        f = open("done.txt", "r")
        journal = datetime.datetime.strptime(f.read(), '%Y-%m-%d').date()
    except IOError:
        print("File not accessible")
    finally:
        f.close()
        if journal != date.today():
            os.remove("done.txt")
            print("File Removed!")


def need_work():
    global f, journal
    try:
        f = open("done.txt", "r")
        journal = datetime.datetime.strptime(f.read(), '%Y-%m-%d').date()
    except IOError:
        print("File not accessible")
    finally:
        f.close()
        return journal != date.today()


def call_the_day():
    global f
    try:
        f = open("done.txt", "w+")
        f.write(str(date.today()))
    except IOError:
        print("File not accessible")
    finally:
        f.close()
        print("Successfully done.")



    check_work()

    if not os.path.isfile('done.txt') or need_work():
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(soup.prettify())
        ps = get_word(soup.find_all("p"))
        clean_none(ps)

        name = [""]
        price = [""]
        ytm = [""]
        count = 0
        i = 0

        while i < len(ps):
            if not is_number(ps[i]):
                count += 1
                i = i + 1
            else:
                if count > 1:
                    name = name + [".", ps[i-1]]
                    price = price + [".", ps[i]]
                    ytm = ytm + [".", ps[i+1]]
                    i = i + 2
                    count = 0
                else:
                    name.append(ps[i - 1])
                    price.append(ps[i])
                    ytm.append(ps[i + 1])
                    i = i + 2
                    count = 0

        today = date.today()
        csv_by_column(file_name=str(today) + ".csv", data=[name, price, ytm])
        call_the_day()

    else:
        print("You have done the task sometime.")
