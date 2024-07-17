from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    # Кнопка "Профиль"
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')

    # Кнопка "История заказов"
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выход"
    LOGOUT = (By.XPATH, '//button[@type = "button"]')

    # "В этом разделе вы можете изменить свои персональные данные"
    DESCRIPTION = (By.XPATH, '//p[contains(@class, "Account_text")]')

    # Загеристрироваться кнопка
    REGISTRATE_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]')