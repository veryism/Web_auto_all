

import time


from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    #创建浏览器
    browser = playwright.chromium.launch(headless=False)
    #创建浏览器链接
    context = browser.new_context()
    #创建浏览器的 sheet 页
    page = context.new_page()
    #打开浏览器输入链接
    page.goto("https://www.baidu.com")

    #输入+清除操作
    # page.locator("#chat-textarea").fill("柠檬班")
    # time.sleep(3)
    #
    # page.locator("#chat-textarea").clear()
    #
    # time.sleep(3)

    #鼠标的双击
    # page.locator("#chat-textarea").fill("柠檬班")
    #
    # page.locator("#chat-textarea").dblclick()

    #鼠标的右键
    # page.locator("#chat-textarea").click(button="right")
    # time.sleep(3)

    # #判断可见性,隐藏，悬停
    #
    # #判断窗口是否隐藏
    # resp = page.get_by_text("高级搜索", exact=True).is_hidden()
    # print(resp)
    #
    # #高亮显示
    # # page.hide_highlight("#s-usersetting-top")
    #
    # #  没有悬停判断这个字段是否存在
    # resp = page.get_by_text("高级搜索",exact=True).is_visible()
    # print(resp)
    #
    # #悬停
    # page.locator("#s-usersetting-top").hover()
    # time.sleep(2)
    # # 悬停后点击判断高级搜索是否存在
    # resp = page.get_by_text("高级搜索",exact=True).is_visible()
    # print(resp)

    #高亮显示及


    page.locator("#s-usersetting-top").highlight()
    time.sleep(3)

