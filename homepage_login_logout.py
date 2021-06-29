import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def load_config(file):
    with open(file, 'r', encoding='UTF-8') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    return config


def input_text_value(browser, select, info):
    textbox = browser.find_element_by_xpath('//*[@name="' + select + '"]')
    textbox.send_keys(Keys.CONTROL + 'a')
    textbox.send_keys(Keys.BACK_SPACE)
    textbox.send_keys(info)


def main():
    config_file = __file__.split('/')[-1].split('.')[0] + '.yaml'
    config = load_config(config_file)
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--window-size=1420,1080')
    browser_options.add_argument('--headless')
    browser_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=browser_options)
    wait = WebDriverWait(browser, config['wait_seconds'])
    browser.get(config['url'])
    input_text_value(browser, 'userMobile', config['username'])
    input_text_value(browser, 'userPassword', config['password'])
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.logout-icon')))
    browser.find_element_by_xpath('//i[@class="anticon anticon-logout"]').click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
    browser.close()


if __name__ == '__main__':
    main()
