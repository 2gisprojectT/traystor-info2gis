class PageFeedback():
    def __init__(self, driver):
        self.driver = driver
        self._feedback = None

    @property
    def feedback(self):
        from helpers.feedback import Feedback

        if self._feedback is None:
            self._feedback = Feedback(self.driver, self.driver.find_element_by_css_selector(Feedback.selectors['self']))
        return self._feedback

    def open(self, url):
        self.driver.get(url)

