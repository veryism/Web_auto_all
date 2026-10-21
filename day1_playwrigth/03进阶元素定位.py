





import time

# 导包
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    # 打开浏览器
    barwser = playwright.chromium.launch(headless=False)

    # 开启上下文，链接的上下文
    content = barwser.new_context()

    # 创建一个链接的页面
    page = content.new_page()

    # 打开页面
    page.goto("http://shop.lemonban.com:3344/")



    # css 元素定位
    # 1. id 选择定位
    # page.locator(
    #     "#chat-textarea"
    # ).fill("柠檬班")

    # 2. class  元素定位
    # page.locator(
    #     ".chat-input-textarea.chat-input-scroll-style").fill("123")


    # 3.任意选择元素定位
    # 前置调前
    page.get_by_text("登录",exact=True).click()

    # page.locator('input[placeholder="请输入手机号/用户名"]').fill("lemon_auto")
    # page.locator('input[placeholder="请输入密码"]').fill("lemon123456")
    # page.locator('.login-button').click()



    time.sleep(3)
