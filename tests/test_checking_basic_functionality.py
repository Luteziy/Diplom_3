import allure
from page_objects.main_page import MainPage
from page_objects.food_page import FoodPage

class TestBasicFunction:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_constructor()
        assert 'Соберите бургер' in main_page.get_title_constructor()

    @allure.title('Переход по клику на "Лента заказов"') #++
    def test_go_to_lent_orders(self, driver):
        main_page = MainPage(driver)
        food_page = FoodPage(driver)
        main_page.click_account_button()
        main_page.click_lent_of_orders()
        assert food_page.get_text_of_lent_order_title() == 'Лента заказов'

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_check_click_ingredient_details_win_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient_fox()
        assert main_page.check_ingredients_details()

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    def test_opened_win_close_by_x_icon_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient_fox()
        main_page.close_ingredient_win()
        assert main_page.ingredient_win_not_open()

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredient_to_order_counter_of_ingredients_rise(self, driver):
        main_page = MainPage(driver)
        main_page.drag_drop_ingredient_to_order()
        assert main_page.get_count_of_ingredients() == '2'

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_logedin_user_can_make_order(self, driver, set_token):
        main_page = MainPage(driver)
        main_page.click_enter_account_main_page()
        main_page.drag_drop_ingredient_to_order()
        main_page.click_button_make_order()
        assert main_page.check_order_made()
