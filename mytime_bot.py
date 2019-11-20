
from webdrivermanager import *
import argparse
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def _argument_parser():
    ap = argparse.ArgumentParser()

    ap.add_argument("-u", "--username",
                    required=True,
                    help="Your user name")

    ap.add_argument("-p", "--password",
                    required=True,
                    help="The fucking password")

    args = vars(ap.parse_args())
    return args


class MyTimeElement():
    def __init__(self, driver):
        self.driver = driver

class MyTimePage():
    mytime_path = "https://mytime.axonactive.vn.local/workinghour.html"
    elements = MyTimeElement()

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().download_and_install()[1])
        self.driver.get(self.mytime_path)


    # def login(self, user, password)



if __name__ == "__main__":
    args = _argument_parser()
    username = args.get('username', None)
    password = args.get('password', None)

    mt = MyTimePage(username, password)
