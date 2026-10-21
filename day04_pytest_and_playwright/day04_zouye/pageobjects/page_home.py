



class HomePage:
    def __init__(self,page):
        self.page = page


    def click_login(self):
        self.page.locator('//a[text()="登录"]').click()



    def click_register(self):
        self.page.locator('//a[text()="注册"]')


#//span[text()="个人中心"]

    def click_center(self):
        self.page.locator('//span[text()="个人中心"]').click()
