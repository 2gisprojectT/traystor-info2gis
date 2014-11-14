class PageSubscribeAndUnsubscribe():
    def __init__(self, driver):
        self.driver = driver
        self._subscribe = None
        self._unsubscribe = None

    @property
    def subscribe(self):
        from helpers.subscribe import Subscribe

        if self._subscribe is None:
            self._subscribe = Subscribe(self.driver, self.driver.find_element_by_css_selector(Subscribe.selectors['self']))
        return self._subscribe

    @property
    def unsubscribe(self):
        from helpers.unsubscribe import Unsubscribe

        if self._unsubscribe is None:
            self._unsubscribe = Unsubscribe(self.driver, self.driver.find_element_by_css_selector(Unsubscribe.selectors['self']))
        return self._unsubscribe

    def open(self, url):
        self.driver.get(url)