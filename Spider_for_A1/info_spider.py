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

    # Start scrap info of each bond
    f = open("snapshot.txt", "r", newline="")
    htmls = []
    for line in f.readlines():
        htmls.append(line.strip())
    f.close()

    an_li.an_li()

    infos = []
    i = 0
    for html in htmls:
        driver = webdriver.Chrome()
        driver.get(html)

        time.sleep(5)

        tbody = driver.find_elements_by_tag_name("tbody")
        tr = tbody[3].find_elements_by_tag_name("tr")

        id = tr[0].find_elements_by_tag_name("td")[1].text
        coupon = tr[10].find_elements_by_tag_name("td")[1].text
        issue_date = tr[8].find_elements_by_tag_name("td")[1].text
        maturity_date = tr[15].find_elements_by_tag_name("td")[1].text
        info = [id, coupon, issue_date, maturity_date]
        infos.append(info)

        driver.close()

        print(str(i) + " webs finished in total, with " + str(32-i) + " webs left to scrap.")
        i = i + 1

    f = open("infos.txt", "w", newline="")
    for info in infos:
        f.write(list_to_str(info) + "\n")
    f.close()
    print("infos.txt is ready, my lord.")

