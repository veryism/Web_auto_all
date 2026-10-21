




class HomePage:

    # 构造初始化
    def __init__(self,page):
        self.page = page


    def goto_login(self):
        self.page.locator('//a[text()="登录"]').click()