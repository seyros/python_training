# -*- coding: utf-8 -*-
__author__ = 'ivanov'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):  # конструктор, инициализирует ссылку на драйвер, а затем помощников
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://172.17.0.2/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

