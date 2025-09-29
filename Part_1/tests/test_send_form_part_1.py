from selene import have
from Part_1.pages.page_registration import RegistrationForm


def test_send_form_part_1(browser_settings):
    page_registrations = RegistrationForm()
    page_registrations.open_page()
    page_registrations.filling_name_and_last_name(text_name='Роман', text_last_name='Гороховик')
    page_registrations.filling_email(text='roman_qa@gmail.com')
    page_registrations.choice_gender()
    page_registrations.filling_mobile_number(mobile_number='9963334558')
    page_registrations.filling_date_picker()
    page_registrations.choice_subjects(text_subject='math')
    page_registrations.choice_hobbies()
    page_registrations.add_picture()
    page_registrations.filling_current_adress(text='Кемерово, ул. Советсткая, д.6')
    page_registrations.choice_state()
    page_registrations.choice_city()
    page_registrations.click_submit()
    page_registrations.get_modal_window().should(have.text('Thanks for submitting the form'))
    page_registrations.get_info_after_sending().should(have.texts('Student Name Роман Гороховик\n'
                                                                  'Student Email roman_qa@gmail.com\n'
                                                                  'Gender Male\nMobile 9963334558\n'
                                                                  'Date of Birth 01 October,1996\n'
                                                                  'Subjects Maths\n'
                                                                  'Hobbies Sports\n'
                                                                  'Picture qa-guru.jpg\n'
                                                                  'Address Кемерово, ул. Советсткая, д.6\n'
                                                                  'State and City NCR Delhi'))
