#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page

class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://2gis.ru")

    def test_path(self):
        self.page.pathfinding.clkWay()
        self.page.pathfinding.enterPath(u'титова', u'зорге')
        self.page.pathfinding.findWay(), self.page.pathfinding.findWay()
        err = self.page.pathfinding.result()
        assert "Вы на месте!", err.text

    def test_share(self):
        self.page.search_bar.search(u'кафе')
        self.page.extras.clk()
        pageLink = self.page.extras.lnk()
        self.assertEqual(pageLink, self.page.extras.lnk(), 'wrong data')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
