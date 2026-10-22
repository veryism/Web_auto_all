

from common.base_page import BasePage
from loguru import logger

class HomePage(BasePage):


    #页面元素定位
    login_link = '//a[text()="登录"]'
    login_register = '//a[text()="注册"]'
    user_center = '//span[text()="个人中心"]'
    home_cart = '//span[@data-route="cart"]'
    home_myorder = '//span[@data-route="order"]'

    home_search_imput_box = '//div[@class="search-input-box"]/input'


    home_search_click = '//div[@class="search-msg"]/input'


    is_home_text = '//span[text() = "欢迎来到柠檬班"]'
    is_home_username_text = '//a[@class = "link-name"]'

    def click_login(self):
        logger.info("===============执行鼠标点击===============")
        self.click(self.login_link)


    def click_register(self):
        logger.info("===============执行鼠标点击===============")
        self.click(self.login_register)


#//span[text()="个人中心"]
    def click_center(self):
        logger.info("===============执行鼠标点击===============")
        self.click(self.user_center)

    def goto_my_order(self):
        self.click(self.home_myorder)


    #搜索 输入框输入商品
    def home_search_imput(self,imput_box_text):
        self.input_type(self.home_search_imput_box,imput_box_text)

    # 输入框输入商品后点击搜索
    def heme_search_click(self):
        self.click(self.home_search_click)

    #点击购物车
    def heme_cart_click(self):
        self.click(self.home_cart)




    #元素定位对象 locatar
    def is_welcome_tips_locator(self):

        welcome_tips = self.page.locator(self.is_home_text)

        logger.info(f"元素定位：{welcome_tips}")
        return welcome_tips

    # 元素定位对象 locatar
    def is_username_locator(self):
        username = self.page.locator(self.is_home_username_text)
        logger.info(f"元素定位：{username}")
        return username






    # def is_welcome_tips_visible(self):
    #    return self.is_visible(self.is_home_text)
    #
    #
    # def is_login_id_visible(self):
    #     return self.get_ele_text(self.is_home_id_text)
