import random
from typing import List

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXECUTABLE_PATH = 'chromedriver.exe'


def an_li():
    f = open("an_li.txt", "r", newline="")
    AN_LI = []
    for line in f.readlines():
        AN_LI.append(line.strip())
    f.close()

    an_li = webdriver.Chrome()
    an_li.get(AN_LI[random.choice(range(len(AN_LI)))])
    time.sleep(10)
    an_li.find_element(By.XPATH, '//button[@aria-label="播放"]').click()
    print("It will take around 10 min for each project, how about eating this 安利~ (ÒωÓױ)?")

print("用我软件，吃我安利 o(*￣▽￣*)ブ")
