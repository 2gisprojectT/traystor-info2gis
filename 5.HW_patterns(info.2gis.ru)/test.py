# -*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page

class Subscribe(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://info.2gis.ru/novosibirsk/company/news/subscribe")

    def test_subscribe(self):
        self.page.subscribe.enterTown()
        self.page.subscribe.enterEmail('fgoor@mail.ru')
        error = self.page.subscribe.enableShareButton()
        self.assertTrue(error,'button is not active')

    def test_unsubscribe(self):
        self.page.unsubscribe.clickUnsub()
        self.page.unsubscribe.enterEmail('fgoor@mail.ru')
        error = self.page.unsubscribe.resultE()
        self.assertEqual(u'Укажите правильный адрес электронной почты', error, 'wrong data')

    def tearDown(self):
        self.driver.close()

class Feedback(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://help.2gis.ru/feedback/")

    def test_feedback(self):
        self.page.feedback.name('kkk')
        self.page.feedback.email('dghdgh@mail.ru')
        self.page.feedback.post('dfsfsdg')
        errorName = self.page.feedback.resultName()
        errorEmail = self.page.feedback.resultEmail()
        errorPost = self.page.feedback.resultPost()
        self.assertNotEqual(u'Укажите ваше имя', errorName, 'wrong or null name')
        self.assertNotEqual(u'Укажите правильный адрес электронной почты', errorEmail,'wrong email')
        self.assertNotEqual(u'Укажите ваш адрес электронной почты', errorEmail,'null email')
        self.assertNotEqual(u'Введите текст сообщения', errorPost, 'wrong or null post')

    def tearDown(self):
        self.driver.close()

class EnterTown(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://info.2gis.ru/")

    def test_enterTown(self):
        enter = u'Норильск'
        self.page.enter_town.inputTown(enter)
        self.assertMultiLineEqual(enter, self.page.enter_town.result(), 'wrong input')

    def tearDown(self):
        self.driver.close()

class Distribution(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://techno.2gis.ru/")

    def test_distribution(self):
        self.page.distribution.email('jnjkbnmail@ndsdnh.ru')
        self.page.distribution.button()
        result = self.page.distribution.result()
        self.assertEqual(u'Мы добавили вас в рассылку',result,'fuck')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
