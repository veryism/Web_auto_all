

from common.base_page import BasePage
from loguru import logger

class CartPage(BasePage):

    Settlement = '//a[@class="btn"]'



    #选择并结算对应的商品
    def select_seetle_prod(self,prod_name):

        logger.info(f"点击购物车内商品{prod_name}勾选框,并结算")
        self.click(f'//a[contains(text(), "{prod_name}")]/parent::div/preceding-sibling::div[2]/input')

        self.click(self.Settlement)
        self.page.wait_for_timeout(2000)



    def is_product_naem(self,prod_name):
        name_locator = self.page.locator(f'//a [contains(text(),"{prod_name}")]')
        logger.info(f"断言购物车商品元素：{name_locator} 商品名称：{prod_name}")
        return name_locator





