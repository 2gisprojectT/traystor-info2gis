class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._extras = None
        self._pathfinding = None

    @property
    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def extras(self):
        from helpers.extras import Extras

        if self._extras is None:
            self._extras = Extras(self.driver, self.driver.find_element_by_css_selector(Extras.selectors['self']))
        return self._extras

    @property
    def pathfinding(self):
        from helpers.pathfinding import Pathfinding

        if self._pathfinding is None:
            self._pathfinding = Pathfinding(self.driver, self.driver.find_element_by_css_selector(Pathfinding.selectors['self']))
        return self._pathfinding

    def open(self, url):
        self.driver.get(url)

