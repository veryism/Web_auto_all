
from common.base_page import BasePage

class UpdateProfile(BasePage):




    #页面元素定位

    #打开点击后上传图片窗口元素定位
    update_profile = '//div[@class="el-upload el-upload--text"]'
    save_profile = '//a[text()="保存账户信息"]'

    # 页面元素定位
    is_change_success_file = '//p[text() =  "修改成功!"]'




    def is_change_success_tips_locator(self):
        return self.page.locator(self.is_change_success_file)




    def click_update_profile(self,filename):


        self.upload_file(self.update_profile,filename)

        # #打开一个监听窗口
        # with self.page.expect_file_chooser() as file_chooser:
        #
        #     #点击文件上传页面，用上述的方法进行监听
        #     self.click(self.update_profile)
        #
        # file_chooser.value.set_files(filename)

    def click_save_profile(self):

        self.click(self.save_profile)

