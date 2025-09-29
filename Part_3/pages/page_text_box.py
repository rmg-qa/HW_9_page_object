from Part_3.data.url_text_box import URL_TEXT_BOX
from selene import browser, have
from Part_3.locators.locators_page_text_box import LocatorsSimpleRegistrationsTextBox


class SimpleRegistrationsTextBox:

    def simple_registrations_text_box(self, user):
        browser.open(URL_TEXT_BOX)
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_FULL_NAME).type(user.full_name)
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_EMAIL).type(user.email)
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_CURRENT_ADDRESS).type(user.current_address)
        browser.element(LocatorsSimpleRegistrationsTextBox.INPUT_PERMANENT_ADDRESS).type(user.permanent_address)
        browser.element(LocatorsSimpleRegistrationsTextBox.SUBMIT_BUTTON).click()

    def assert_simple_registrations_text_box(self):
        browser.all(LocatorsSimpleRegistrationsTextBox.RESEULT_REGISTRATIONS).should(have.texts(
            'Name:Роман Гороховик\n'
            'Email:roman_qa@gmail.com\n'
            'Current Address :Кемерово, ул. Советсткая, д.6\n'
            'Permananet Address :г. Анжеро-Судженск, пгт. Рудничный, ул. металлургов 5-32'))
