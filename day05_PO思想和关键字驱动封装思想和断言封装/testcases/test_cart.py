


"""

登录->搜索商品-选择商品-添加购物车~进入购物车页面-添加购物车提示断言，在购物车内断言

"""

from playwright.sync_api import Page,expect

from pageobjects.page_cart import CartPage
from pageobjects.page_login import LoginPage
from pageobjects.page_home import HomePage

from pageobjects.page_product_list import ProductListPage

from pageobjects.page_product_deteils import ProductDateilsPage




def test_homework(page:Page):
    #打开页面
    page.goto("http://mall.lemonban.com:3344/")

    #home 操作页类
    home_page = HomePage(page)

    #登录操作类
    loginpage = LoginPage(page)


    #订单流程
    #点击登录
    home_page.click_login()

    #输入账号密码
    loginpage.aconunt_login("lemon_auto","lemon123456")

    expect(home_page.is_welcome_tips_locator()).to_be_visible()
    expect(home_page.is_username_locator()).to_have_text("lemon_auto")


    searh_imput = 'i7高配一体机电脑'
    #输入搜索商品
    home_page.home_search_imput(searh_imput)


    #点击搜索按钮
    home_page.heme_search_click()

    #点击搜索到的商品 进入详情页
    ProductListPage(page).click_product(searh_imput)

    productdata = ProductDateilsPage(page)

    # 商品详情页断言
    expect(page).to_have_title("商品详情")




    #点击添加到购物车
    productdata.click_product_add_cart()

    # 判断添加购物车弹窗
    expect(productdata.is_add_cart()).to_be_visible()

    #点击购物车
    home_page.heme_cart_click()

    expect(CartPage(page).is_product_naem(searh_imput)).to_contain_text(searh_imput)





