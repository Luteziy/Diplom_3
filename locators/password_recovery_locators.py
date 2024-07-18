from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD = (By.XPATH, '//a[text() = "Восстановить пароль"]')

    # Имя
    NAME = (By.XPATH, './/input[@name="name"]')  # Имя

    # Email
    EMAIL = (By.CLASS_NAME, 'input__textfield')  # Email

    # Пароль
    PASSWORD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')  # Пароль

    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')

    # Значок "показать пароль"
    ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Пароль не видно
    PASSWORD_NOT_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, ''"input_status_active")]')

    # Пароль видно
    PASSWORD_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, ''"input_status_active")]')

    # Надпись "Вход"
    enter_text = (By.XPATH, ".// h2[text() = 'Вход']")