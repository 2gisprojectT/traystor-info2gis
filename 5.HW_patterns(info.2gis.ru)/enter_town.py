from base_component import BaseComponent

class EnterTown(BaseComponent):
    selectors = {
        'self' :'#module-1-6 > div',
        'clickInput': '#module-1-6-2 > div.cityselect__title',
        'input': '#module-1-6-2 > div.cityselector._visible > div > div.cityselector__search > div.cityselector__searchContent > input',
        'result': '#module-1-6-2 > div.cityselector._visible > div > div.cityselector__searchResult > div > div > div > div > a > span'
    }

    def inputTown(self, inputTown):
        self.driver.find_element_by_css_selector(self.selectors['clickInput']).click()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(inputTown)

    def result(self):
        return self.driver.find_element_by_css_selector(self.selectors['result']).text
