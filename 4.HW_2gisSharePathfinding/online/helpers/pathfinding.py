from helpers.base_component import BaseComponent

class Pathfinding(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'way': '#module-1-1 > div.searchBar__tabs > div.searchBar__tab.searchBar__rsTab',
        'from': '#module-1-1-2 > div > input',
        'to': '#module-1-1-3 > div > input',
        'findWay': '#module-1-1 > div.searchBar__forms > form > button.searchBar__submit._rs',
        'result': '#module-1-9-1-1 > div > section.routeResults__route._current > div > div > ul > li:nth-child(4) > ul > li'
    }

    def clkWay(self):
        self.driver.find_element_by_css_selector(self.selectors['way']).click()

    def enterPath(self, query, query1):
        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['to']).send_keys(query1)

    def findWay(self):
        self.driver.find_element_by_css_selector(self.selectors['findWay']).click()

    def result(self):
        self.driver.find_element_by_css_selector(self.selectors['result'])
