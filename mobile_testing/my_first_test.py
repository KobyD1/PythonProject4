import unittest

import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy



appium_server_url_local = 'http://localhost:4723/wd/hub'

capabilities = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appActivity='com.android.deskclock.DeskClock',
    appPackage='com.google.android.deskclock',
    newCommandTimeout=120,
    language='en',
    locale='US'
)

class myFirstTest(unittest.TestCase):
    print ("Start test")


    def setUp(self) -> None:

        self.driver = webdriver.Remote(appium_server_url_local,capabilities)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test1(self):
        print ("into test1")
        time_element = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.deskclock:id/digital_clock')



