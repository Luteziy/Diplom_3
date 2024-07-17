import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from data import Data, Url
from helpers import create_random_email, create_random_password, create_random_name


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    driver.get(Data.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
@allure.title('Генерация рандомного юзера')
def create_and_delete_new_user():
    email = create_random_email(),
    password = create_random_password(),
    name = create_random_name()
    return email, password, name

@pytest.fixture
@allure.title('Создание и удаление юзера')
def create_and_delete_new_user():
    user = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Url.Url_create_user, data=user)
    response_body = response.json()

    yield user, response_body

    token = response_body['accessToken']
    requests.delete(Url.Url_delete_user, headers={'Authorization': token})

@pytest.fixture
@allure.title('Создаем юзера и его заказ, потом удаляем')
def create_user_and_order_then_delete(create_and_delete_new_user):
    access_token = create_and_delete_new_user[1]['accessToken']
    headers = {'Authorization': access_token}
    order = {'ingredients': [
        '61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa71',
        '61c0c5a71d1f82001bdaaa77', '61c0c5a71d1f82001bdaaa7a'
    ]}
    response_body = requests.post(Url.Url_create_order, data=order, headers=headers)

    yield access_token, response_body
    requests.delete(Url.Url_delete_user, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Токен созданного юзера')
def set_token(driver, create_and_delete_new_user):
    driver.get(Data.MAIN_PAGE_URL)
    user = create_and_delete_new_user[1]
    access_token = user.get('accessToken')
    refresh_token = user.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')