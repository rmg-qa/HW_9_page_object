import os

from selene import browser


class RegistrationForm:

    def open_page(self):  # открытие браузера
        browser.open('https://demoqa.com/automation-practice-form')

    def filling_name_and_last_name(self, text_name, text_last_name):  # заполнение полей "Имя", "Фамилия"
        browser.element('[placeholder="First Name"]').type(text_name)
        browser.element('[placeholder="Last Name"]').type(text_last_name)

    def filling_email(self, text):  # заполение поля email
        browser.element('[id="userEmail"]').type(text)

    def choice_gender(self):  # выбор пола
        browser.element('[for="gender-radio-1"]').click()

    def filling_mobile_number(self, mobile_number):  # заполнение поля "мобильный телефон"
        browser.element('[id="userNumber"]').type(mobile_number)

    def filling_date_picker(self):  # заполнение датапикера
        browser.element('[id="dateOfBirthInput"]').click()  # клик по полю
        browser.element('[class="react-datepicker__month-select"]').click()  # клик по селектору "месяц"
        browser.element('.//option[@value="9"]').click()  # клик по значению выпадающего списка месяцев
        browser.element('[class="react-datepicker__year-select"]').click()  # клик по селектору "год"
        browser.element('[value="1996"]').click()  # клик по значению селектора "год"
        browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()  # клик по дате

    def choice_subjects(self, text_subject):  # выбор поля "Субъект"
        browser.element('[id="subjectsInput"]').type(text_subject)
        browser.element('.//div[@id="react-select-2-option-0"]').click()

    def choice_hobbies(self):  # выбор хобби
        browser.element('[for="hobbies-checkbox-1"]').click()

    def add_picture(self):  # добавлене изображения
        browser.element('.//input[@class="form-control-file"]').type(os.path.abspath('Part_1/resources/qa-guru.jpg'))

    def filling_current_adress(self, text):  # заполнение текущего адреса
        browser.element('[id="currentAddress"]').type(text)

    def choice_state(self):  # выбор Штата
        browser.element('[id="state"]').click()
        browser.element('[id="react-select-3-option-0"]').click()

    def choice_city(self):  # Выбор города
        browser.element('[id="city"]').click()
        browser.element('[id="react-select-4-option-0"]').click()

    def click_submit(self):  # клик по кнопке "Отправить"
        browser.element('[id="submit"]').click()

    def get_modal_window(self):  # проверка получения модального окна
        return browser.element('[class="modal-title h4"]')

    def get_info_after_sending(self):  # получение полной информации о пользователе после отправки формы
        return browser.all("tbody")
