from selenium.webdriver.common.by import By

class MainPageLocators:

    # Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, './/*[@href = "/account"]')

    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # Конпка гл страницы
    MAIN_PAGE = (By.XPATH, '//li/a[@href = "/"]')

    #_______________________________________________________________________

    # Email
    EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Пароль
    #PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")

    # Надпись "Вход"
    #ENTER = (By.XPATH, ".// h2[text() = 'Вход']")


    #________________________________---------------------------------------------

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Текст "Конструктор" (на кнопке)
    TITLE_CONSTRUCTOR_BUTTON = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Раздел "Булки" в конструкторе
    BREAD = (By.XPATH, '//span[text() = "Булки"]')

    # Раздел "Соусы" в конструкторе
    SOUSE = (By.XPATH, '//span[text() = "Соусы"]')

    # Раздел "Начинки" в конструкторе
    FILLINGS = (By.XPATH, '//span[text() = "Начинки"]')

    # Кнопка "Лента заказов"
    LENT_OF_ORDERS_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Текст "Лента заказов"
    LENT_OF_ORDERS_TEXT = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')

    # Подтверждение оформленного заказа
    ORDER_DONE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')


    # _____________________________________________

    # Ингредиент
    BURGER_TEXT = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    # Бургер (картинка)
    BURGER_PIC = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Соус

    # Детали ингредиента
    INGREDIENTS_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Куда перетаскиваются игнредиенты
    PREORDER = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Счетчик ингредиенттов
    INGREDIENTS_COUNTER = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')

    #____________________________________________________________________

    # Крестик - закрыть окно созданного заказа
    X_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]')

    # Крестик - закрыть окно ингредиента
    X_CLOSE_INGREDIENT_BUTTON = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')
    # Номер заказа
    ORDER_NUMBER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')