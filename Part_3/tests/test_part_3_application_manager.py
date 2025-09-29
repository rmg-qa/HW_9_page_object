from Part_3.pages.application import app
from Part_3.data.user import user_student


def test_send_form_part_3(browser_settings):
    user = user_student
    app.simple_registration.simple_registrations_text_box(user)  # регистрация нового пользователя
    app.simple_registration.assert_simple_registrations_text_box()  # проверка, что регистрация прошла успешно
