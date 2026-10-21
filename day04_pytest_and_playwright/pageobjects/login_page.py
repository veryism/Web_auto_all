import time


#登录页面类


class LoginPage:


    # 构造初始化
    def __init__(self,page):
        self.page = page

    #页面 元素定位和操作

    def acconunt_login(self,username,password):

        # username  = lemon_auto   password = lemon123456

        self.page.locator('//input[@placeholder="请输入手机号/用户名"]').fill(username)
        self.page.locator('//input[@placeholder="请输入密码"]').fill(password)

        self.page.locator('//a[text()="登录" and @class="login-button"]').click()



    def phone_login(self,phone,code):
        # phone  = 手机号    password = 密码
        self.page.locator('//input[@placeholder="请输入登录手机号"]').fill(phone)
        self.page.locator('//a[text()="获取验证码"]').click()

        self.page.locator('//input[@placeholder="请输入验证码"]').fill(code)

        self.page.locator('//a[text()="登录" and @class="login-button"]').click()


    # def forgot_password(self,page,username,password):

