import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


capabilities = dict(
    platformName='Android',
    deviceName='Pixel 3 XL API27',
    appPackage='com.android.calculator2',
    appActivity='com.android.calculator2.Calculator',
    language='en',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723/wd/hub'

class TestAppium(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.driver.implicitly_wait(30)
    def tearDown(self) :
        if self.driver:
            self.driver.quit()

    def test_calculate_tap(self) :
        print('into test')




        print('test stop')



