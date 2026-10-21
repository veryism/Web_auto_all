


from common.base_page import BasePage
from loguru import logger




#提交订单类
class  MyOrderPage(BasePage):

    my_order_name = '//a[@class="name"]'

    my_order_payment = '//div[@class="status"]/div'

    my_order_price = '//div[contains(text(),"在线支付")]//span'

    my_order_num = '//div[@class="goods-number"]'

    #检查我的订单商品名称
    def is_my_order_name(self):
        return self.page.locator(self.my_order_name).first

    # 检查我的订单商品支付状态
    def is_my_order_payment(self):
        return self.page.locator(self.my_order_payment).first

    def is_my_order_price(self):
        return self.page.locator(self.my_order_price).first

    def is_my_order_sun(self):
        return self.page.locator(self.my_order_num).first