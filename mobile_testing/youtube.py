import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys

capabilities = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appPackage='com.google.android.youtube',
    appActivity='com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity',
    language='en',
    locale='US'
)
appium_server_url_local = 'http://localhost:4723/wd/hub'

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
        permittion = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_deny_button')
        permittion.click()
        search = self.driver.find_element(by = AppiumBy.XPATH,value='//android.widget.ImageView[@content-desc="Search"]')
        search.click()
        search_menu = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.youtube:id/search_edit_text')
        search_menu.click()
        search_menu.send_keys("Eurovision 2023")
        search_menu.send_keys(Keys.ENTER)
        # self.driver.press_keycode(66)
        a = 1

