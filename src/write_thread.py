import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from . import utils


def write_to_5ch(url: str, message='ほっしゅほっしゅほっしゅ', name='VIPdeFF14ちょうかしこい保守ツール君'):
    now = datetime.datetime.now()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    try:
        wait = WebDriverWait(driver, 15)
        driver.get(url)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@class="formbox"]')))
        driver.find_element_by_name('FROM').send_keys(name)
        driver.find_element_by_tag_name("textarea").send_keys(message)
        time.sleep(3)
        '''
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="submitbtn btn"]'))).click()
        '''
        element = driver.find_element_by_xpath('//input[@class="submitbtn btn"]')
        driver.execute_script('arguments[0].click();', element)

        wait.until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="formbox"]')))
        if driver.find_elements_by_xpath(
                '//input[@type="submit" and @value="上記全てを承諾して書き込む"]'):
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//input[@type="submit" and @value="上記全てを承諾して書き込む"]'))).click()
            print(f'{now} :書き込みました。')
    except Exception as e:
        utils.notify_desktop('エラー発生', str(e))
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(f'{now} :エラー発生')
        print(e)
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    driver.quit()


if __name__ == '__main__':
    url = 'https://mi.5ch.net/test/read.cgi/news4vip/1643963150/'
    write_to_5ch(url)
