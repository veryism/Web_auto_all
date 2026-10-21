

class CenterPage:
    def __init__(self,page):
        self.page = page



    def hove_center_profile(self):

        # self.page.locator('//div[@class="portrait"]').hover()

        self.page.locator('//div[@class="portrait-box"]').hover()

    def click_profile(self):
        self.page.locator('//div[@class="edit"]').click()

        pass