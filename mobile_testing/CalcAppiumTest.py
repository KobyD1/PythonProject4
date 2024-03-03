import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator',
    newCommandTimeout=120,
    language='en',
    locale='US'
)

appium_server_url_local = 'http://localhost:4723/wd/hub'

class TestAppium(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Remote(appium_server_url_local,capabilities)
        self.driver.implicitly_wait(10)
    def tearDown(self) :
        if self.driver:
            self.driver.quit()

    def test_calculate_click(self) :
        print('into test')
        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_2')
        digit1 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_1')
        digit5 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_5')

        multiple = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.calculator:id/op_mul')
        equlas = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.calculator:id/eq')

        digit1.click()
        digit2.click()
        multiple.click()
        digit5.click()
        equlas.click()
        result = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.calculator:id/result_final')

        summery = result.text
        print (f'the value is ',summery)

        time.sleep(3)


        print('test stop')

