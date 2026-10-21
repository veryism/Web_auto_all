


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
    page.goto("https://www.ketangpai.com/")

    time.sleep(3)

    #元素定位通过角色role定位
    # page.get_by_role("button",name="百度一下").click()

    #通过元素文本来进行元素定位
    # page.get_by_text("百度一下",exact=True).click()

    #点击登录按钮
    page.get_by_role("button",name="登录").click()

    #通过元素的 palacehoider 来进行元素获取，一般存在输入框来使用这个方法
    page.get_by_placeholder("请输入邮箱/手机号/账号").fill("lemon")

    # 打开页面后的延迟，类似sleep
    page.wait_for_timeout(5000)


