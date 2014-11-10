from base_component import BaseComponent

class Feedback(BaseComponent):

    selectors = {
        'self': '#module-1 > section.page__section._content._divided > section',
        'name': '#feedback_author_name',
        'email': '#feedback_author_email',
        'post': '#feedback_post',
        'resultName': '#module-1-8-2 > form > ul > li:nth-child(1) > span',
        'resultEmail': '#module-1-8-2 > form > ul > li:nth-child(3) > span',
        'resultPost': '#module-1-8-2 > form > ul > li:nth-child(5) > span'
    }

    def name(self, name):
        self.driver.find_element_by_css_selector(self.selectors['name']).send_keys(name)

    def email(self, email):
        self.driver.find_element_by_css_selector(self.selectors['email']).send_keys(email)

    def post(self, post):
        self.driver.find_element_by_css_selector(self.selectors['post']).send_keys(post)

    def resultName(self):
        return self.driver.find_element_by_css_selector(self.selectors['resultName']).text

    def resultEmail(self):
        return self.driver.find_element_by_css_selector(self.selectors['resultEmail']).text

    def resultPost(self):
        return self.driver.find_element_by_css_selector(self.selectors['resultPost']).text