

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")


    page.locator("#chat-textarea").fill("柠檬班")

    time.sleep(3)
    page.locator("#chat-submit-button").click()

    page.get_by_text("用户反馈",exact=True).scroll_into_view_if_needed()
    time.sleep(3)

    page.screenshot(path="baidu_shot.png",full_page=True)



