


class UpdateProfile:

    def __init__(self,page):

        self.page = page


    def click_update_profile(self,filename):

        #打开一个监听窗口
        with self.page.expect_file_chooser() as file_chooser:

            #点击文件上传页面，用上述的方法进行监听
            self.page.locator('//div[@class="el-upload el-upload--text"]').click()

        file_chooser.value.set_files(filename)

    def click_save_profile(self):
        self.page.locator('//a[text()="保存账户信息"]').click()

