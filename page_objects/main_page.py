import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage
from helpers import create_random_email, create_random_password, create_random_name
from data import Data

class MainPage(BasePage):

    @allure.step('Клик на кнопку Личный кабинет, для мозилы, так как с простым кликом не работает')
    def click_account_button(self):
        self.click_problem_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Войти в аккаунт" на гл странице, для мозилы')
    def click_enter_account_main_page(self):
        self.click_problem_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке "Войти в аккаунт" на главной странице')
    def click_enter_account_main_page_chrome(self):
        self.wait_visibility_of_element(MainPageLocators.LOGIN_BUTTON)
        self.check_element_is_clickable(MainPageLocators.LOGIN_BUTTON)
        self.click_on_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет" на главной странице')
    def click_enter_personal_account(self):
        self.wait_visibility_of_element(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_clickable(MainPageLocators.ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Ввод почты')
    def email_input_to_login(self):
        self.wait_visibility_of_element(MainPageLocators.EMAIL)
        email = create_random_email()
        self.input_text(MainPageLocators.EMAIL, email)

    @allure.step('Получить заголовок "Конструктора"')
    def get_title_constructor(self):
        return self.get_text_from_element(MainPageLocators.TITLE_CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_lent_of_orders(self):
        self.wait_visibility_of_element(MainPageLocators.LENT_OF_ORDERS_BUTTON)
        self.check_element_is_clickable(MainPageLocators.LENT_OF_ORDERS_BUTTON)
        self.click_on_element(MainPageLocators.LENT_OF_ORDERS_BUTTON)

    @allure.step('Клик по ленте заказов для Мозилы')
    def click_lent_of_orders_fox(self):
        self.click_problem_element(MainPageLocators.LENT_OF_ORDERS_BUTTON)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.BURGER_PIC)
        self.click_on_element(MainPageLocators.BURGER_PIC)

    @allure.step('Клик по ингредиенту для мозилы')
    def click_on_ingredient_fox(self):
        self.click_problem_element(MainPageLocators.BURGER_PIC)


    @allure.step('Проверит появления окна "Детали ингредиента')
    def check_ingredients_details(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENTS_DETAILS)
        return self.check_displaying_of_element(MainPageLocators.INGREDIENTS_DETAILS)

    @allure.step('Клик по крестику закрыть окно ингредиента')
    def close_ingredient_win(self):
        self.wait_visibility_of_element(MainPageLocators.X_CLOSE_INGREDIENT_BUTTON)
        self.click_on_element(MainPageLocators.X_CLOSE_INGREDIENT_BUTTON)

    @allure.step('Окно детали ингредиента не открыто')
    def ingredient_win_not_open(self):
        self.wait_for_closing_of_element(MainPageLocators.INGREDIENTS_DETAILS)
        if not self.check_displaying_of_element(MainPageLocators.INGREDIENTS_DETAILS):
            return True

    @allure.step('Перетащить ингредиент')
    def drag_drop_ingredient_to_order(self):
        bread = self.find_element_waiting(MainPageLocators.BURGER_PIC)
        to_order = self.find_element_waiting(MainPageLocators.PREORDER)
        self.drag_element(bread, to_order)

    @allure.step('Получить число ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_button_make_order(self):
        self.wait_visibility_of_element(MainPageLocators.MAKE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка: создался заказ')
    def check_order_made(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_DONE)
        return self.check_displaying_of_element(MainPageLocators.ORDER_DONE)

    @allure.step('Получить номер созданного заказа')
    def get_created_new_order_number(self):
        self.waiting_number_changes(MainPageLocators.ORDER_NUMBER, '99999')
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Клик - закрыть окно заказа')
    def click_on_button_close_order(self):
        self.check_element_is_clickable(MainPageLocators.X_CLOSE_BUTTON)
        self.wait_visibility_of_element(MainPageLocators.X_CLOSE_BUTTON)
        self.find_element_waiting(MainPageLocators.X_CLOSE_BUTTON)
        self.click_on_element(MainPageLocators.X_CLOSE_BUTTON)

    @allure.step('Клик - закрыть окно заказа Mozila')
    def click_on_button_close_order_fox(self):
        self.click_problem_element((MainPageLocators.X_CLOSE_BUTTON))

    @allure.step('Переход на гл страницу')
    def go_to_main_page(self):
        self.click_on_element(MainPageLocators.MAIN_PAGE)