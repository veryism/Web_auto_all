


from playwright.sync_api import Page,expect


from common.handle_path import image_path
from pageobjects import page_home
from pageobjects import page_login
from pageobjects import page_centers
from pageobjects import page_update_profile


def test_update_porf(page:Page):

    page.goto('http://mall.lemonban.com:3344/')

    # 实例化类

    #主页面类实例化
    home_page = page_home.HomePage(page)

    #个人中心实例化类
    center_page = page_centers.CenterPage(page)

    #上传文件 类实例化
    update_file_page = page_update_profile.UpdateProfile(page)




    #点击登录 按钮
    home_page.click_login()
    #输入 账号密码
    page_login.LoginPage(page).aconunt_login(username="lemon_auto", password="lemon123456")

    #点击个人中心
    home_page.click_center()

    #需要悬停，然后再次点击按钮
    #悬停
    center_page.hove_center_profile()
    #点击修改头像
    center_page.click_profile()



    #点击上传图片，需要创建一个监听窗口
    update_file_page.click_update_profile(image_path)

    page.wait_for_timeout(3000)

    #上传完成 点击保存
    update_file_page.click_save_profile()

    expect(update_file_page.is_change_success_tips_locator()).to_be_visible()









