



from playwright.sync_api import Page,expect
from pyexpat import expat_CAPI
from urllib3.util import timeout

from pageobjects import page_home
from pageobjects import page_login



def test_update_porf(page:Page):

    page.goto('http://mall.lemonban.com:3344/')

    # 实例化类

    #主页面类实例化
    home_page = page_home.HomePage(page)


    #点击登录 按钮
    home_page.click_login()
    #输入 账号密码
    page_login.LoginPage(page).aconunt_login(username="lemon_auto", password="lemon123456")

    # page.wait_for_timeout(3000)

    expect(home_page.is_welcome_tips_locator()).to_be_visible()

    expect(home_page.is_username_locator()).to_have_text("lemon_auto")


    # assert home_page.is_welcome_tips_visible() == True
    # assert home_page.is_login_id_visible() == "lemon_auto"