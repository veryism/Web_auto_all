


from common.base_page import BasePage


class ProductListPage(BasePage):



    #点击搜索到的商品
    def click_product(self,product_link):
        self.click(f'//div[contains(text(),"{product_link}")]')
