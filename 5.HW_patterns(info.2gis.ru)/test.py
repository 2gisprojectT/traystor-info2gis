# -*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from pages.page_subscribe_and_unsubscribe import PageSubscribeAndUnsubscribe
from pages.page_feedback import PageFeedback
from pages.page_enter_town import PageEnterTown
from pages.page_distribution import PageDistribution
class Subscribe(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page_subscribe_and_unsubscribe = PageSubscribeAndUnsubscribe(self.driver)
        self.driver.implicitly_wait(10)
        self.page_subscribe_and_unsubscribe.open("http://info.2gis.ru/novosibirsk/company/news/subscribe")

    def test_subscribe(self):
        self.page_subscribe_and_unsubscribe.subscribe.enterTown()
        self.page_subscribe_and_unsubscribe.subscribe.enterEmail('fgoor@mail.ru')
        error = self.page_subscribe_and_unsubscribe.subscribe.enableShareButton()
        self.assertTrue(error,'button is not active')

    def test_unsubscribe(self):
        self.page_subscribe_and_unsubscribe.unsubscribe.clickUnsub()
        self.page_subscribe_and_unsubscribe.unsubscribe.enterEmail('fgoor@mail.ru')
        error = self.page_subscribe_and_unsubscribe.unsubscribe.resultE()
        self.assertEqual(u'Укажите правильный адрес электронной почты', error, 'wrong data')

    def tearDown(self):
        self.driver.close()

class Feedback(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page_feedback = PageFeedback(self.driver)
        self.driver.implicitly_wait(10)
        self.page_feedback.open("http://help.2gis.ru/feedback/")

    def test_feedback(self):
        self.page_feedback.feedback.name('kkk')
        self.page_feedback.feedback.email('dghdgh@mail.ru')
        self.page_feedback.feedback.post('dfsfsdg')
        errorName = self.page_feedback.feedback.resultName()
        errorEmail = self.page_feedback.feedback.resultEmail()
        errorPost = self.page_feedback.feedback.resultPost()
        self.assertNotEqual(u'Укажите ваше имя', errorName, 'wrong or null name')
        self.assertNotEqual(u'Укажите правильный адрес электронной почты', errorEmail,'wrong email')
        self.assertNotEqual(u'Укажите ваш адрес электронной почты', errorEmail,'null email')
        self.assertNotEqual(u'Введите текст сообщения', errorPost, 'wrong or null post')

    def tearDown(self):
        self.driver.close()

class EnterTown(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page_enter_town = PageEnterTown(self.driver)
        self.driver.implicitly_wait(10)
        self.page_enter_town.open("http://info.2gis.ru/")

    def test_enterTown(self):
        enter = u'Норильск'
        self.page_enter_town.enter_town.inputTown(enter)
        self.assertMultiLineEqual(enter, self.page_enter_town.enter_town.result(), 'wrong input')

    def tearDown(self):
        self.driver.close()

class Distribution(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page_distribution = PageDistribution(self.driver)
        self.driver.implicitly_wait(10)
        self.page_distribution.open("http://techno.2gis.ru/")

    def test_distribution(self):
        self.page_distribution.distribution.email('jnjkbnmail@ndsdnh.ru')
        self.page_distribution.distribution.button()
        result = self.page_distribution.distribution.result()
        self.assertEqual(u'Мы добавили вас в рассылку',result,'fuck')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
