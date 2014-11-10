from base_component import BaseComponent


class Unsubscribe(BaseComponent):
    selectors = {
        'self': '#module-1-7-1 > div > dd:nth-child(4)',
        'unsub': '//*[@id="module-1-7-1"]/div/dt[2]/span',
        'clickBtnUnsubscribe': '#module-1-7-1-2 > form > div > input',
        'email': '#subscribeconfirmation_email',
        'resultE': '#module-1-7-1-2 > form > ul > li.form__item._error > span'
    }

    def clickUnsub(self):
        self.driver.find_element_by_xpath(self.selectors['unsub']).click()

    def enterEmail(self, email):
        self.driver.find_element_by_css_selector(self.selectors['email']).click()
        self.driver.find_element_by_css_selector(self.selectors['email']).send_keys(email)

    def clickButton(self):
        self.driver.find_element_by_css_selector(self.selectors['clickBtnUnsubscribe']).click()

    def resultE(self):
        self.driver.find_element_by_css_selector(self.selectors['resultE'])
