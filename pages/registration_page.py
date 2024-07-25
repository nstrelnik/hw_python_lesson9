from selene import browser, have, command
import resources.resource
from data.users import User


class RegistrationFormPage:

    def open(self):
        browser.open("/automation-practice-form")

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

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()
        return self

    def fill_user_subject(self, value):
        browser.element('#subjectsInput').type(value).press_tab()
        return self

    def fill_user_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def fill_user_picture(self, file_name):
        browser.element('#uploadPicture').set_value(resources.resource.path(file_name))
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

    def registration(self, user: User):
        (
            self.fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_user_email(user.email)
            .fill_user_gender(user.gender)
            .fill_user_number(user.mobile)
            .fill_date_of_birth(user.date_of_birth_day, user.date_of_birth_month, user.date_of_birth_year)
            .fill_user_subject(user.subjects)
            .fill_user_hobby(user.hobbies)
            .fill_user_picture(user.picture)
            .fill_user_current_address(user.current_address)
            .fill_user_state(user.state)
            .fill_user_city(user.city)
        )

    def registered_user_with(self, user: User):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.mobile,
                f"{user.date_of_birth_year} {user.date_of_birth_month},{user.date_of_birth_day}",
                user.subjects,
                user.hobbies,
                user.picture,
                user.current_address,
                f"{user.state} {user.city}"
            )
        )
