import time

from pageobjects import LoginPage
from pageobjects import HomePage


def test_login(page):


    page.goto("http://shop.lemonban.com:3344/")


    HomePage(page).goto_login()



    #实例化这个类--得到页面类 的对象，可以用对象调用里面的方法
    LoginPage(page).acconunt_login("lemon_auto","lemon123456")


    time.sleep(3)