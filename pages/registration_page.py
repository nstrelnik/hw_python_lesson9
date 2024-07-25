from selene import browser, have, command
from utils import resource


class RegistrationFormPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command=command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_user_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_user_subject(self, value):
        browser.element('#subjectsInput').type(value).press_tab()
        return self

    def fill_user_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def fill_user_picture(self, file_name):
        browser.element('#uploadPicture').set_value(resource.path(file_name))
        return self

    def fill_user_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_user_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def fill_user_city(self, value):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def click_submit(self):
        browser.element('#submit').click()
        return self

    def registered_user_with(self, full_name, email, gender, phone, date_of_birth, subject, hobby, photo, address, state):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobby,
                photo,
                address,
                state
            )
        )
        return self
