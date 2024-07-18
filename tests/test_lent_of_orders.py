import allure
from page_objects.food_page import FoodPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.personal_account_page import PersonalAccountPage

class TestLentOrders:

    @allure.title('Проверь: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_details_win(self, driver):
        main_page = MainPage(driver)
        food_page = FoodPage(driver)
        main_page.click_lent_of_orders_fox()
        food_page.click_on_order()
        assert 'бургер' in food_page.get_text_from_card_order()

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_history_orders_equals_lent_orders(self, driver, set_token, create_user_and_order_then_delete):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        food_page = FoodPage(driver)
        main_page.click_enter_personal_account()
        personal_account_page.wait_visibility_of_description()
        personal_account_page.ckick_order_history_button_fox()
        order_id = order_history_page.get_card_order_number()
        main_page.click_lent_of_orders()
        assert food_page.check_order_number_in_lent(order_id)

    @allure.title('Проверка: при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_create_new_order_order_counter_all_time_rise(self, driver, set_token):
        main_page = MainPage(driver)
        food_page = FoodPage(driver)
        main_page.click_lent_of_orders_fox()
        order_1 = food_page.get_order_counter_for_all_time()
        main_page.click_constructor()
        main_page.click_enter_account_main_page()
        main_page.drag_drop_ingredient_to_order()
        main_page.click_button_make_order()
        main_page.click_on_button_close_order_fox()
        main_page.click_lent_of_orders_fox()
        order_2 = food_page.get_order_counter_for_all_time()
        assert order_1 < order_2


    @allure.title('Проверка: при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_create_new_order_counter_today_rise(self, driver, set_token):
        main_page = MainPage(driver)
        food_page = FoodPage(driver)
        main_page.click_lent_of_orders_fox()
        order_1 = food_page.get_order_counter_for_today()
        main_page.click_constructor()
        main_page.click_enter_account_main_page()
        main_page.drag_drop_ingredient_to_order()
        main_page.click_button_make_order()
        main_page.click_on_button_close_order()
        main_page.click_lent_of_orders_fox()
        order_2 = food_page.get_order_counter_for_today()
        assert order_1 < order_2

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе "В работе"')
    def test_create_new_order_number_appear_in_progress(self, driver, set_token):
        main_page = MainPage(driver)
        food_page = FoodPage(driver)
        main_page.click_enter_account_main_page()
        main_page.drag_drop_ingredient_to_order()
        main_page.click_button_make_order()
        new_order = main_page.get_created_new_order_number()
        main_page.click_on_button_close_order_fox()
        main_page.click_lent_of_orders_fox()
        assert food_page.get_last_order_number_in_progress() == '0'+new_order