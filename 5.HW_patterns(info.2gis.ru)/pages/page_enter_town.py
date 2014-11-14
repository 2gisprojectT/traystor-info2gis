class PageEnterTown():
    def __init__(self, driver):
        self.driver = driver
        self._enter_town = None

    @property
    def enter_town(self):
        from helpers.enter_town import EnterTown

        if self._enter_town is None:
            self._enter_town = EnterTown(self.driver, self.driver.find_element_by_css_selector(EnterTown.selectors['self']))
        return self._enter_town

    def open(self, url):
        self.driver.get(url)

