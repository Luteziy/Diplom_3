from page_objects.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from helpers import create_random_email, create_random_password
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def click_recover_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.RECOVER_PASSWORD)
        self.click_on_element(PasswordRecoveryLocators.RECOVER_PASSWORD)

    @allure.step('Ожидание видимости поля "email" в окне "Восстановление пароля"')
    def check_visibility_of_field_recover_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.EMAIL)

    @allure.step('Ввод почты для восстановления пароля')
    def email_input(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.EMAIL)
        email = create_random_email()
        self.input_text(PasswordRecoveryLocators.EMAIL, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_recover_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.RECOVER_BUTTON)
        self.click_on_element(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.step('Ожидание видимости поля "пароль" в окне "Восстановление пароля"(ввести пароль и код из письма)')
    def check_visibility_of_field_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD)
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD)

    @allure.step('Ввести пароль')
    def password_input(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD)
        password = create_random_password()
        self.input_text(PasswordRecoveryLocators.PASSWORD, password)

    @allure.step('Клик по иконке показать/скрыть пароль')
    def click_on_visible_not_visible_icon(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.ICON)
        self.click_on_element(PasswordRecoveryLocators.ICON)

    @allure.step('Клик по иконке показать/скрыть пароль, mozila')
    def click_on_eye_button(self):
        self.click_problem_element((PasswordRecoveryLocators.ICON))

    @allure.step('Пароль отображается')
    def check_password_is_visible(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_VISIBLE)

    @allure.step('Пароль не отображается')
    def check_password_is_not_visible(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_NOT_VISIBLE)