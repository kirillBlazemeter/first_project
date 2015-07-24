from selenium import webdriver
import allure

@allure.step('test go')
def test():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get('https://a.blazemeter.com/app/')
    assert 'BlazeMeter' in browser.title
    email = browser.find_element_by_name('email')  # Find the email field
    email.send_keys('kirill@blazemeter.com')

    password = browser.find_element_by_name('password')  # Find the pass field
    password.send_keys('12345678')

    submit = browser.find_element_by_xpath("//button[@title='Sign in']")  # Find the submit button
    submit.click()
    assert 'BlazeMeter' in browser.title

    browser.quit()
