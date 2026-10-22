

from loguru import logger
from playwright.sync_api import Page


#该类是所有公共类的父类
class BasePage:


    def __init__(self,page:Page):
        self.page = page



    # 公用点击操作
    def click(self,locator_click):
        logger.info(f"执行点击：{locator_click}")
        self.page.locator(locator_click).click()


    def get_by_text_click(self,get_text_click):
        self.page.get_by_text(get_text_click).click()



    #公共输入操作
    def input_type(self,locator_input,data):
        logger.info(f"执行输入操作：{locator_input}，输入内容：{data}")
        self.page.locator(locator_input).fill(data)







    #公共方法鼠标悬停
    def mouse_hover(self,locator_hover):
        logger.info(f"鼠标悬停：{locator_hover}")
        self.page.locator(locator_hover).hover()


    #公用方法，文件上传

    def upload_file(self,locator_file,filename):
        logger.info(f"文件上传操作：{locator_file}，上传文件：{filename}")
        # 打开一个监听窗口
        with self.page.expect_file_chooser() as file_chooser:

            # 点击文件上传页面，用上述的方法进行监听
            self.click(locator_file)
            logger.info(f"文件上传监听窗口:{locator_file}")

        file_chooser.value.set_files(filename)
        logger.info(f"文件上传完成:{filename}")


    #获取元素的文本
    def get_ele_text(self,locator_input):

        ele_text = self.page.locator(locator_input).text_content()
        logger.info(f"获取元素文本：{ele_text}")
        return ele_text


        #检查 元素是否可见
    def is_visible(self,locator_visible):
        visible_text = self.page.locator(locator_visible).is_visible()
        logger.info(f"检查元素是否可见:{visible_text},结果：{visible_text}")
        return visible_text