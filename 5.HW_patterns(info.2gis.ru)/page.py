class Page():
    def __init__(self, driver):
        self.driver = driver
        self._subscribe = None
        self._unsubscribe = None
        self._feedback = None
        self._enter_town = None
        self._distribution = None

    @property
    def subscribe(self):
        from subscribe import Subscribe

        if self._subscribe is None:
            self._subscribe = Subscribe(self.driver, self.driver.find_element_by_css_selector(Subscribe.selectors['self']))
        return self._subscribe

    @property
    def unsubscribe(self):
        from unsubscribe import Unsubscribe

        if self._unsubscribe is None:
            self._unsubscribe = Unsubscribe(self.driver, self.driver.find_element_by_css_selector(Unsubscribe.selectors['self']))
        return self._unsubscribe

    @property
    def feedback(self):
        from feedback import Feedback

        if self._feedback is None:
            self._feedback = Feedback(self.driver, self.driver.find_element_by_css_selector(Feedback.selectors['self']))
        return self._feedback

    @property
    def enter_town(self):
        from enter_town import EnterTown

        if self._enter_town is None:
            self._enter_town = EnterTown(self.driver, self.driver.find_element_by_css_selector(EnterTown.selectors['self']))
        return self._enter_town

    @property
    def distribution(self):
        from distribution import Distribution

        if self._distribution is None:
            self._distribution = Distribution(self.driver, self.driver.find_element_by_css_selector(Distribution.selectors['self']))
        return self._distribution

    def open(self, url):
        self.driver.get(url)

