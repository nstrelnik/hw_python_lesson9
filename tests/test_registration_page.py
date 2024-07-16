from pages.registration_page import RegistrationFormPage


def test_student_registration_form():
    registration_page = RegistrationFormPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Masha')
        .fill_last_name('Www')
        .fill_user_email('test@gmail.com')
        .fill_user_gender('Female')
        .fill_user_number('1234456789')
        .fill_day_of_birth('1999', 'May', '11')
        .fill_user_subject('Maths')
        .fill_user_hobby('Sports')
        .fill_user_picture('picture.jpg')
        .fill_user_current_address('Quitzon Common, South Kraigville')
        .fill_user_state('NCR')
        .fill_user_city('Delhi')
        .click_submit()
    )
    registration_page.registered_user_with('Masha Www', 'test@gmail.com', 'Female', '1234456789', '11 May,1999',
                                             'Maths', 'Sports', 'picture.jpg',
                                             'Quitzon Common, South Kraigville', 'NCR Delhi')