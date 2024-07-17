import allure
from page_objects.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators

class PersonalAccountPage(BasePage):
    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_accoutn_button(self):
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step('Клик по кнопке "История заказов" мозила')
    def ckick_order_history_button_fox(self):
        self.click_problem_element(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step('Клик по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(PersonalAccountLocators.LOGOUT)

    @allure.step('Ожидание прогрузки теста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(PersonalAccountLocators.DESCRIPTION)

    @allure.step('Отображения текста описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(PersonalAccountLocators.DESCRIPTION)

    @allure.step('Прогрузка кнопки "Зарегистрироваться"')
    def wait_visibility_of_registrate_button(self):
        self.wait_visibility_of_element(PersonalAccountLocators.REGISTRATE_BUTTON)

    @allure.step('Отображение кнопки "Зарегистрироваться"')
    def check_displaying_registrate_button(self):
        return self.check_displaying_of_element(PersonalAccountLocators.REGISTRATE_BUTTON)