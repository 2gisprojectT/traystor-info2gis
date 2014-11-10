from base_component import BaseComponent

class Distribution(BaseComponent):
    selectors = {
        'self' :'body > section > div.page__section._animated > div.slider.slidesjs-ready > div > div > div.slider__listItem.slidesjs-slide._active > div > div.slider__content',
        'email': 'body > section > div.page__section._animated > div.slider.slidesjs-ready > div > div > div.slider__listItem.slidesjs-slide._active > div > div.slider__content > div > div > form > fieldset > div.subscribeForm__formRow > input',
        'button': 'body > section > div.page__section._animated > div.slider.slidesjs-ready > div > div > div.slider__listItem.slidesjs-slide._active > div > div.slider__content > div > div > form > fieldset > div.subscribeForm__formRow > button',
        'result': 'body > section > div.page__section._animated > div.slider.slidesjs-ready > div > div > div.slider__listItem.slidesjs-slide._active > div > div.slider__content > div > div > form > fieldset > div.subscribeForm__formSuccess > span'
    }

    def email(self, email):
        self.driver.find_element_by_css_selector(self.selectors['email']).send_keys(email)

    def button(self):
        self.driver.find_element_by_css_selector(self.selectors['button']).click()

    def result(self):
        return self.driver.find_element_by_css_selector(self.selectors['result']).text