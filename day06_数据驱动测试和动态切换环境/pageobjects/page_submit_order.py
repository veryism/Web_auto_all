


from common.base_page import BasePage
from loguru import logger




#提交订单类
class  SubmitOrderPage(BasePage):

    submit = '//a[text() = "提交订单"]'

    #点击提交订单
    def click_submit(self):
        logger.info("点击提交订单")

        self.click(self.submit)
        self.page.wait_for_timeout(2000)
