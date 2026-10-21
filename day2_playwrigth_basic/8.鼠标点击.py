

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    page.goto("http://www.baidu.com")



    resp = page.locator('//a[@data-name="tjnews"]').bounding_box()

    print(resp)




    page.mouse.click(24,19)



    time.sleep(3)





