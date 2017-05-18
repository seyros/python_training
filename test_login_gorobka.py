# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login_gorobka(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_login_gorobka(self):
        success = True
        wd = self.wd
        wd.get("http://searchbox-1.dev.search.km:9013/auth/login")
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='login-form']//button[.='Войти']").click()
        wd.find_element_by_link_text("Пользователи").click()
        wd.find_element_by_link_text("Маркеры").click()
        wd.find_element_by_link_text("Подсказки").click()
        wd.find_element_by_link_text("Опечатки").click()
        wd.find_element_by_link_text("Чёрный список").click()
        wd.find_element_by_link_text("Синонимы").click()
        wd.find_element_by_link_text("Поиск").click()
        wd.find_element_by_id("searchInput").click()
        wd.find_element_by_id("searchInput").clear()
        wd.find_element_by_id("searchInput").send_keys("rhjrjpz,hf")
        wd.find_element_by_link_text("рамблер").click()
        wd.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
