import allure

from Part_2.pages.page_registration_form import RegistrationFormMethods, SimpleRegistration
from Part_2.data.user import user_student


@allure.title("Successful fill form registration")
def test_send_form_part_2(browser_settings):
    user = user_student
    open_page_registrations = RegistrationFormMethods()
    simple_registrations = SimpleRegistration()
    open_page_registrations.open_page()  # открытие страницы регистрации
    simple_registrations.simple_registration(user)  # регистрация нового пользователя
    simple_registrations.assert_simple_registration()  # проверка, что регистрация прошла успешно
