from selenium import webdriver
import time


def login_lagou():

    browser = webdriver.Chrome()
    browser.get('https://passport.lagou.com/login/login.html')
    time.sleep(4)

    input_name = browser.find_element_by_css_selector('body > section > div.left_area.fl > div:nth-child(2) > form > div:nth-child(1) > input')
    input_name.send_keys('********')
    time.sleep(1)
    input_passwork =browser.find_element_by_css_selector('body > section > div.left_area.fl > div:nth-child(2) > form > div:nth-child(2) > input')
    input_passwork.send_keys('******')

    button = browser.find_element_by_css_selector('body > section > div.left_area.fl > div:nth-child(2) > form > div.input_item.btn_group.clearfix.sense_login_password > input')
    time.sleep(1)
    button.click()

    cookie_dic = {}
    cookies = browser.get_cookies()
    for cookie in cookies:
        cookie_dic[cookie['name']] = cookie['value']

    browser.quit()
    print(cookie_dic)
    return cookie_dic


if __name__ == '__main__':
    login_lagou()