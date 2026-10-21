import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #打开网站链接
    page.goto("http://shop.lemonban.com:3344/")

    #点击登录按钮
    page.locator('//a[text()="登录"]').click()

    #输入账号密码
    page.locator('//input[@placeholder="请输入手机号/用户名"]').fill("lemon_auto")
    page.locator('//input[@placeholder="请输入密码"]').fill("lemon123456")

    #点击登录按钮
    time.sleep(1)
    page.locator('//a[text()="登录" and @class="login-button"]').click()

    #点击个人中心
    time.sleep(1)
    page.locator('//span[@data-route="userCenter"]').click()



    #在指定窗口进行悬浮等待
    time.sleep(1)
    page.locator('//div[@class="portrait-box"]').hover()


    #悬浮后有指定元素后进行点击
    time.sleep(1)
    page.locator('//div[@class="edit"]').click()


    #创建一个监测,用来检查是否点击文件上传
    with page.expect_file_chooser() as file_chooser:

        #点击文件 上传按钮
        time.sleep(1)
        page.locator('//testdatas[@class="pic avatar"]').click()

    #监测到打开文件上传,选择文件进行上传
    file_chooser.value.set_files("yuansu.png")

    #点击保存信息
    time.sleep(1)
    page.locator('//a[@class="btn"]').click()




    time.sleep(3)




