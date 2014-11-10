from base_component import BaseComponent

class Subscribe(BaseComponent):

    selectors = {
        'self': '#module-1-7-1 > div > dt.tabs__containerTitle._active > span',
        'town': '#s2id_subscribeconfirmation_cities > ul',
        'clickTown': '#select2-drop > ul > li:nth-child(32)',
        'email': '#subscribeconfirmation_email',
        'enableShareButton': '#module-1-7-1-1 > form > div > input',
    }

    def enterTown(self):
        self.driver.find_element_by_css_selector(self.selectors['town']).click()
        self.driver.find_element_by_css_selector(self.selectors['clickTown']).click()

    def enterEmail(self, email):
        self.driver.find_element_by_css_selector(self.selectors['email']).click()
        self.driver.find_element_by_css_selector(self.selectors['email']).send_keys(email)

    def enableShareButton(self):
        return self.driver.find_element_by_css_selector(self.selectors['enableShareButton']).is_enabled()
