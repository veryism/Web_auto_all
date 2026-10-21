

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")

    innertext = page.locator("#chat-submit-button").inner_text()


    print(f"获取到的元素文本:{innertext}")

    classtext = page.locator("#chat-textarea").get_attribute("class")


    print(f"获取到的class 属性:{classtext}")





    page.locator("#chat-textarea").fill("柠檬班")

    inputvalue = page.locator("#chat-textarea").input_value()

    print(f"获取元素的属性:{inputvalue}")

    resp = page.locator("#chat-textarea").bounding_box()

    print(f"获取元素的坐标以及边界:{resp}")





    time.sleep(3)





