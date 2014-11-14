class PageDistribution():
    def __init__(self, driver):
        self.driver = driver
        self._distribution = None

    @property
    def distribution(self):
        from helpers.distribution import Distribution

        if self._distribution is None:
            self._distribution = Distribution(self.driver, self.driver.find_element_by_css_selector(Distribution.selectors['self']))
        return self._distribution

    def open(self, url):
        self.driver.get(url)

