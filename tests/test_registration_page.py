from data.users import User
from pages.registration_page import RegistrationFormPage


def test_user_can_send_form():
    registration_page = RegistrationFormPage()
    user = User('Anastasiia',
                'Strelnik',
                'test@gmail.com',
                'Female',
                '9216666666',
                '29', 'March', '2001',
                'Maths',
                'Sports',
                'picture.jpg',
                'Kaliningrad',
                'NCR',
                'Delhi'
                )
    registration_page.open()
    registration_page.registration(user)
    registration_page.click_submit()
    registration_page.registered_user_with(user)