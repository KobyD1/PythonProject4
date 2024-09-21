import time
from selenium.webdriver.common.by import By



class BitBucketLoginPage(object):


    def __init__(self, driver):
        self.driver = driver
        self.user_name = "username"
        self.continue_button = "login-submit"
        self.continue_with_google = "social-login-submit"
        self.password = "password"
    def login_with_user_password(self,user,password):
        print(f'Login with user name methodology  , user  name =  {user} ')

        user_name_button =  self.driver.find_element(By.ID,self.user_name)
        user_name_button.click()
        user_name_button.send_keys(user)

        continue_button =  self.driver.find_element(By.ID,self.continue_button)
        continue_button.click()
        password_button =  self.driver.find_element(By.ID,self.password)
        password_button.click()
        password_button.send_keys(password)
        continue_button.click()
        print(f'Login success')




