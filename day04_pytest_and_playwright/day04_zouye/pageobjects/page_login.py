


class LoginPage:



    def __init__(self,page):
        self.page = page




    def  aconunt_login(self,username,password):

        self.page.locator('//input[@placeholder="请输入手机号/用户名"]').fill(username)
        self.page.locator('//input[@placeholder="请输入密码"]').fill(password)




        self.page.locator('//a[@class="login-button"]').click()
