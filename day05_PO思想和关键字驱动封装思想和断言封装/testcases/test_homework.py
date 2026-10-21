


"""

登录->搜索商品-选择商品-添加购物车~进入购物车页面-购物车结算-点击结算-订单提交--关注订单断言--进入我的订单页面

"""

from playwright.sync_api import Page,expect



from pageobjects.page_cart import CartPage
from pageobjects.page_login import LoginPage
from pageobjects.page_home import HomePage
from pageobjects.page_my_order import MyOrderPage
from pageobjects.page_pay_order import PayOrderPage
from pageobjects.page_product_list import ProductListPage
from pageobjects.page_submit_order import SubmitOrderPage
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

    #点击立即购买
    # productdata.click_product_buy_now()


    #点击添加到购物车
    productdata.click_product_add_cart()

    # 判断添加购物车弹窗
    expect(productdata.is_add_cart()).to_be_visible()

    #点击购物车
    home_page.heme_cart_click()


    #在购物车内勾选并结算
    CartPage(page).select_seetle_prod(searh_imput)
    #//a[contains(text(), '真皮圆筒包2022')]/parent::div/preceding-sibling::div[2]/input


    #点击提交订单
    SubmitOrderPage(page).click_submit()


    #点击微信支付
    PayOrderPage(page).click_wechat_pay("微信支付")
    #点击微信支付,并付款
    expect(productdata.is_wechat_pay_loc()).to_have_text("微信支付")
    #添加断言，判断支付页面title 是否为提交订单
    expect(productdata.is_submit_order()).to_have_text("微信扫一扫支付")

    #进入我的订单
    home_page.goto_my_order()

    #进行断言
    expect(MyOrderPage(page).is_my_order_name()).to_contain_text(searh_imput)
    expect(MyOrderPage(page).is_my_order_payment()).to_contain_text("待支付")
    expect(MyOrderPage(page).is_my_order_price()).to_contain_text("5855")
    expect(MyOrderPage(page).is_my_order_sun()).to_contain_text("1")


    page.wait_for_timeout(3000)