

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    page.goto("http://www.baidu.com")

    page.locator("#chat-textarea").fill("柠檬班")

    time.sleep(2)
    #全选
    page.locator("#chat-textarea").press("Control+A")

    time.sleep(2)
    page.locator("#chat-textarea").press("Control+C")

    time.sleep(2)
    page.locator("#chat-textarea").press("Control+V")

    time.sleep(2)
    page.locator("#chat-textarea").press("Control+V")

    time.sleep(2)
    page.locator("#chat-submit-button").press("Enter")






    time.sleep(3)





