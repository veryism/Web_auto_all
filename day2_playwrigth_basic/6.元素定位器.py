

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")

    loc = page.locator(".mnav.c-font-normal.c-color-t")


    print(loc.count())
    print(loc.all_inner_texts())


    #根据class 点击第一个
    # print(loc.first.click())

    # 根据class 点击最后一个
    # print(loc.last.click())

    # 根据class 点击第三个,索引的位置
    print(loc.nth(0).click())





    time.sleep(3)





