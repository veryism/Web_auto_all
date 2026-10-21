

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    #建立打开浏览器
    browser = playwright.chromium.launch(headless=False)

    #浏览器链接
    context  = browser.new_context()

    #建立浏览器sheet页
    page = context.new_page()

    page.goto("http://mall.lemonban.com:3344")

    #给指定的操作设置超时时间
    # page.locator('//a[text()="登录"]').click(timeout=5000)

    # 设置全局的超时时间
    page.set_default_timeout(6000)
    page.locator('//a[text()="登录xxxx"]').click()



    time.sleep(5)





