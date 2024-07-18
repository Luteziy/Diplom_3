import allure
from locators.order_history_locators import OrderHistoryLocators
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class OrderHistoryPage(BasePage):

    @allure.step('Прогрузка данных карточки заказа')
    def wait_visibility_card_order(self):
        self.wait_visibility_of_element(OrderHistoryLocators.CARD_ORDER)

    @allure.step('Текст карточки заказа')
    def get_text_from_card_order(self):
        return self.get_text_from_element(OrderHistoryLocators.CARD_ORDER_NAME)

    @allure.step('Получить № заказа')
    def get_card_order_number(self):
        return self.get_text_from_element(OrderHistoryLocators.CARD_ORDER_NUM)

    @allure.step('Получить текст "Лента заказов"')
    def get_text_of_lent_order_title(self):
        return self.get_text_from_element(MainPageLocators.LENT_OF_ORDERS_TEXT)