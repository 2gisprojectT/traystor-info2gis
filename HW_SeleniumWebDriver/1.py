# =*- coding: utf-8 -*-

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SLTest(TestCase):
    def test(self):
        driver = webdriver.Firefox()
        driver.get("http://info.2gis.ru")
        driver.find_element_by_id("cityselect").click()
        select = driver.find_element_by_class_name("cityselector__input")
        select.send_keys("New-York")
        err = driver.find_element_by_class_name("cityselector__empty")
        assert "Такого города пока нет в 2ГИС. Проверьте правильность написания или попробуйте выбрать из списка городов.", err.text
        driver.close()

if __name__ == '__main__':
    unittest.main()
