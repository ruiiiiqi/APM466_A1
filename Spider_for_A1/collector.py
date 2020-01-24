import random
from typing import List

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXECUTABLE_PATH = 'chromedriver.exe'

WEB_1 = "https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=shortterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19"
WEB_2 = "https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=midterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19"

WEB = [WEB_1, WEB_2]


if __name__ == "__main__":

    # One can definitely optimize this file a lot. But I will not do it due to the time limit...
    for web in WEB:
        driver = webdriver.Chrome()
        driver.get(web)

        time.sleep(10)

        # Get the blue print of all necessary web link.
        a = driver.find_elements_by_partial_link_text("Government of")
        htmls = []
        for web_element in a:
            html = web_element.get_attribute("href")
            new_html = html[:html.find("bonds/")] + "bond/historical/" + html[html.find("bonds/")+6:]
            htmls.append(new_html)

        f = open("historical.txt", "a", newline="")
        for html in htmls:
            f.write(html + "\n")
        f.close()
        driver.close()
    print("historical.txt ready.")

    # Give snapshot.txt ready. If only I have done this when before historical.txt...
    f = open("historical.txt", "r", newline="")
    htmls = []
    for html in f.readlines():
        html = html[:html.find("bond/")] + "bonds/" + html[html.find("historical") + 11:]
        htmls.append(html)
    f.close()

    f = open("snapshot.txt", "w", newline="")
    for html in htmls:
        f.write(html)
    f.close()
    print("snapshot.txt ready.")
