import allure
from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswordRecoveryPage

class TestPasswordRecovery:
    @allure.title('Переходим на страницу восстановления пароля')
    def test_go_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_account_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recover_password()
        assert password_recovery_page.check_visibility_of_field_recover_email

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_recover_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_account_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recover_password()
        password_recovery_page.email_input()
        password_recovery_page.click_on_recover_button()
        assert password_recovery_page.check_visibility_of_field_password()

    @allure.title('Проверка видимости пароля при клике на иконку сокрытия/открытия пароля')
    def test_click_on_visible_not_visible_icon_password_visible(self, driver):
        main_page = MainPage(driver)
        main_page.click_account_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recover_password()
        password_recovery_page.email_input()
        password_recovery_page.click_on_recover_button()
        password_recovery_page.password_input()
        password_recovery_page.click_on_visible_not_visible_icon()
        assert password_recovery_page.check_password_is_visible()

    @allure.title('Проверка невидимости пароля при повторном клике на иконку сокрытия/открытия пароля')
    def test_click_on_visible_not_visible_icon_password_visible(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account_main_page()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recover_password()
        password_recovery_page.email_input()
        password_recovery_page.click_on_recover_button()
        password_recovery_page.password_input()
        password_recovery_page.click_on_eye_button()
        password_recovery_page.click_on_eye_button()
        assert password_recovery_page.check_password_is_not_visible