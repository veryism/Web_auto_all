


from common.base_page import BasePage
from loguru import logger




#提交订单类
class  PayOrderPage(BasePage):
    wechat_pay = '//span[text() = "微信支付"]'
    alipay_pay = '//span[text()="支付宝"]'
    paypal = '//testdatas[@class="paypal-text"]'

    pay_now = '//a[text() = "立即付款"]'

    #点击微信支付
    def click_wechat_pay(self,pay_method):

        if pay_method =="支付宝":
            self.click(self.pay_now)

        elif pay_method=="微信支付":

            self.click(self.wechat_pay)
            self.click(self.pay_now)

        elif pay_method.lower() =="paypal":
            self.click(self.paypal)
            self.click(self.pay_now)

        else:
            logger.error("输入的支付方式不合法")


