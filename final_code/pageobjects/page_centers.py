

from common.base_page import BasePage

from loguru import logger

class CenterPage(BasePage):




    #页面元素定位
    hove_center = '//div[@class="portrait-box"]'
    profile_edit = '//div[@class="edit"]' #悬浮后点击头像，跳转到修改头像页面




    def hove_center_profile(self):
        logger.info("===============执行鼠标悬停===============")
        self.mouse_hover(self.hove_center)



    def click_profile(self):

        # self.page.locator(self.profile_edit).click()
        logger.info("===============执行鼠标点击===============")
        self.click(self.profile_edit)


