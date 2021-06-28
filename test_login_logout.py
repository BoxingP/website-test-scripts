import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def load_yaml_file(file):
    with open(file, 'r', encoding='UTF-8') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    return config


def input_text_value(browser, select, info):
    textbox = browser.find_element_by_xpath('//*[@name="' + select + '"]')
    textbox.send_keys(Keys.CONTROL + 'a')
    textbox.send_keys(Keys.BACK_SPACE)
    textbox.send_keys(info)


def main():
    login_credential = load_yaml_file('./login_credential.yaml')
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 420)
    browser.get(login_credential['url'])
    input_text_value(browser, 'userMobile', login_credential['username'])
    input_text_value(browser, 'userPassword', login_credential['password'])
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.logout-icon')))
    browser.find_element_by_xpath('//i[@class="anticon anticon-logout"]').click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
    browser.close()


if __name__ == '__main__':
    main()
