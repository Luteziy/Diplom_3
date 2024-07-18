from selenium.webdriver.common.by import By

class OrderHistoryLocators:

    # Карточка заказа
    CARD_ORDER = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')

    # Название карточки
    CARD_ORDER_NAME = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')

    # Номер заказа
    CARD_ORDER_NUM = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]''/p[contains(@class, "text_type_digits-default")])[1]')