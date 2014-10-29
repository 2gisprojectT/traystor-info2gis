from helpers.base_component import BaseComponent


class Extras(BaseComponent):

    selectors = {
        'self': '.extras__group',
        'clickBtn': '.extras__btn.extras__share',
        'getLink': '.share__popupUrlInput'
    }

    def clk(self):
        self.driver.find_element_by_css_selector(self.selectors['clickBtn']).click()

    def lnk(self):
        self.driver.find_element_by_css_selector(self.selectors['getLink']).get_attribute('value')
