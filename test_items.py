from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_add_to_basket_button_exists(driver: WebDriver):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    driver.get(link)
    # Задержку добавлять здесь
    # time.sleep(30)
    button = driver.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button.is_displayed()
