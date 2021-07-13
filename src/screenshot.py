import time
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import argparse as ag
import threading


class Selenium:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def get(self, url: str):
        self.driver.get(url)

    def selector(self, selector: str) -> WebElement:
        WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return self.driver.find_element_by_css_selector(selector)

    def screenshot(self, filename:str = '/mnt/screenshot.png') -> None:
        self.driver.set_window_size(1024, 1600)
        self.driver.save_screenshot(filename)


# Authenticating to the store next.
def authentication(sel: Selenium, url: str, username: str, password: str) -> None:
    sel.get(url)
    time.sleep(30)
    sel.selector("#user").send_keys(username)
    sel.selector("#password").send_keys(password)
    sel.selector("#submit_lbl").click()


def screenshot(sel: Selenium, filename:str = "/mnt/screenshot.png") -> None:
    time.sleep(30)
    sel.screenshot(filename)


def connect(url: str, username: str, password: str) -> Selenium:
    sel = Selenium()
    authentication(sel, url, username, password)

    return sel


def getParameter() -> Tuple[str, str, str]:
    parser = ag.ArgumentParser(description='Automatically open browser with selenium')
    parser.add_argument('--username', type=str, default='root')
    parser.add_argument('--password', type=str, required=True)
    parser.add_argument('--nodename', type=str, required=True)
    args = parser.parse_args()
    username = args.username
    password = args.password
    url = f'https://m-{args.nodename}.ipmi.ihme.washington.edu'

    return username, password, url


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    username, password, url = getParameter()
    sel:Selenium = connect(url, username, password)
    screenshot(sel)
