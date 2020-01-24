import random
from typing import List
import csv

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Spider_for_A1 import an_li

EXECUTABLE_PATH = 'chromedriver.exe'

def list_to_str(my_list: List[str]):
    result = ""
    for item in my_list:
        result = result + " " + item

    return result

if __name__ == "__main__":

    f = open("historical.txt", "r", newline="")
    htmls = []
    for html in f.readlines():
        htmls.append(html)
    f.close()

    an_li.an_li()

    prices = []
    i = 0
    for html in htmls:
        driver = webdriver.Chrome()
        driver.get(html)

        time.sleep(5)

        tbody = driver.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name('tr')[6:16]
        price = []
        for line in tr:
            price.append(line.find_elements_by_tag_name("td")[2].text)
            price.reverse()
        prices.append(price)

        driver.close()

        print(str(i) + " webs finished in total, with " + str(32 - i) + " webs left to scrap.")
        i = i + 1

    f = open("prices.txt", "w", newline="")
    for price in prices:
        f.write(list_to_str(price) + "\n")
    f.close()
    print("prices.txt is ready, my lord.")