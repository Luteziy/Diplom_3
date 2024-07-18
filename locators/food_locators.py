from selenium.webdriver.common.by import By

class FoodLocators:


    # Текст заголовка "Лента заказов"
    LENT_OF_ORDERS_TEXT = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Раздел карточек заказа
    ORDER_CARD_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Карточка заказа(а ленте заказов)
    CARD_ORDER_IN_LENT = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Окно "Детали заказа"
    MODAL_ORDER_BOX = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')

    # Заголовок окна "Детали заказа"
    MODAL_ORDER_BOX_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Номер для поиска заказа
    ID_ORDER = (By.XPATH, './/*[text()="{order_id}"]')

    # Выполнено за все время
    ORDER_COUNTER_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Выполнено за сегодня
    ORDER_COUNTER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Последний номер заказа "В работе"
    NUM_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')