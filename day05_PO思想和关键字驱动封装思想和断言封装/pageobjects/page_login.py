

from common.base_page import BasePage
from loguru import logger

class LoginPage(BasePage):


    #=====页面元素定位=====
    username_input = '//input[@placeholder="请输入手机号/用户名"]'
    userpassword_input = '//input[@placeholder="请输入密码"]'

    login_button = '//a[@class="login-button"]' #登录按钮





    def  aconunt_login(self,username,password):

        logger.info("===============账号密码登录===============")

        # self.page.locator(self.username_input).fill(username)
        self.input_type(self.username_input,username)

        # self.page.locator(self.userpassword_input).fill(password)
        self.input_type(self.userpassword_input, password)


        # self.page.locator(self.login_button).click()
        self.click(self.login_button)

        self.page.wait_for_timeout(2000)



