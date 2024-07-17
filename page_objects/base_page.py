import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_problem_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Найти элемент на странице')
    def find_element_waiting(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Прогрузка элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ввести данные в поле')
    def input_text(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Получить заголовок')
    def get_page_header(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(*locator))

    @allure.step('Отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Перетащить элемент')
    def drag_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(5).perform()

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Подождать закрытия элемента')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание изменения номера заказа')
    def waiting_number_changes(self, locator, value):
        return WebDriverWait(self.driver, 20).until_not(expected_conditions.text_to_be_present_in_element(locator, value))