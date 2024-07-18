import allure
from page_objects.base_page import BasePage
from locators.food_locators import FoodLocators

class FoodPage(BasePage):
    @allure.step('Получить текст "Лента заказов"')
    def get_text_of_lent_order_title(self):
        return self.get_text_from_element(FoodLocators.LENT_OF_ORDERS_TEXT)

    @allure.step('Клик по заказу')
    def click_on_order(self):
        self.wait_visibility_of_element(FoodLocators.CARD_ORDER_IN_LENT)
        self.click_on_element(FoodLocators.CARD_ORDER_IN_LENT)

    @allure.step('Получить название выбранной карточки заказа')
    def get_text_from_card_order(self):
        return self.get_text_from_element(FoodLocators.MODAL_ORDER_BOX_TITLE)


    @allure.step('Количество выполненных заказов за все время')
    def get_order_counter_for_all_time(self):
        count = self.find_element_waiting(FoodLocators.ORDER_COUNTER_ALL_TIME).text
        return count


    @allure.step('Количество заказов за сегодня')
    def get_order_counter_for_today(self):
        self.find_element_waiting(FoodLocators.ORDER_COUNTER_TODAY)
        return self.get_text_from_element(FoodLocators.ORDER_COUNTER_TODAY)

    @allure.step('Проверить номер заказа в ленте заказов')
    def check_order_number_in_lent(self, order_id):
        locator = FoodLocators.ID_ORDER
        id_locator = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_waiting(id_locator)
        return self.check_displaying_of_element(id_locator)
    @allure.step('Получить номер заказа "В работе"')
    def get_last_order_number_in_progress(self):
        return self.get_text_from_element(FoodLocators.NUM_ORDER_IN_PROGRESS)