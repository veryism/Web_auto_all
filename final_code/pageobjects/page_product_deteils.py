


from common.base_page import BasePage
from loguru import logger




#商品详情页类
class  ProductDateilsPage(BasePage):


    buy_now = '//a[text() = "立即购买"]'
    add_cart = '//a[@class="add-cart"]'
    add_cart_text_tips =  '//p[text()="成功加入购物车"]'






    is_price = '(//div[@class="unit-price"])[2]'
    is_wechat_pay = '//span[text()="微信支付"]'
    is_sabmit_pay = '//div[text() = "微信扫一扫支付"]'



    #点击立即购买
    def click_product_buy_now(self):
        self.click(self.buy_now)



    def click_product_add_cart(self):
        self.click(self.add_cart)





    #商品价格断言
    def is_price_loc(self):
        price = self.page.locator(self.is_price)
        logger.info(f"商品价格元素定位返回：{price}")
        return price

    def is_wechat_pay_loc(self):
        wechat_play_loc = self.page.locator(self.is_wechat_pay)
        logger.info(f"判断支付微信按钮是否可见：{wechat_play_loc}")
        return wechat_play_loc

    def is_submit_order(self):

        sabmit_order =  self.page.locator(self.is_sabmit_pay)

        logger.info(f"判断跳转到微信扫码二维码页面：{sabmit_order}")

        return sabmit_order

    def is_add_cart(self):
        add_cart_text_tips = self.page.locator(self.add_cart_text_tips)
        logger.info(f"添加购物车弹窗提示：{add_cart_text_tips}")
        return add_cart_text_tips