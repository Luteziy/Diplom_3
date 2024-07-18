import allure
from page_objects.main_page import MainPage
from page_objects.personal_account_page import PersonalAccountPage
from page_objects.order_history_page import OrderHistoryPage


class TestPersonalAccout:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_crossing_to_personal_account_page(self, driver, set_token):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_account_button()
        personal_account_page.wait_visibility_of_description()
        assert personal_account_page.check_displaying_of_description()

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_crossing_to_order_history_page(self, driver, set_token, create_user_and_order_then_delete):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_enter_personal_account()
        personal_account_page.wait_visibility_of_description()
        personal_account_page.ckick_order_history_button_fox()
        order_history_page.wait_visibility_card_order()
        assert 'бургер' in order_history_page.get_text_from_card_order()

    @allure.title('Выход при клике на кнопку "Выход"')
    def test_logout_from_personal_account(self, driver, set_token):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_account_button()
        personal_account_page.wait_visibility_of_description()
        personal_account_page.click_on_logout_button()
        personal_account_page.wait_visibility_of_registrate_button()
        assert personal_account_page.check_displaying_registrate_button()
