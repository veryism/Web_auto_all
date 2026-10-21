

import time
from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    # page.goto("https://www.baidu.com")
    # time.sleep(3)
    #
    # resp  = page.locator("#s-usersetting-top").is_visible()
    # if resp:
    #     page.locator("#s-usersetting-top").hover()
    #
    #     page.locator('//span[text()="高级搜索"]').click()
    #
    #     page.locator("#q5_1").set_checked(True)
    #     time.sleep(3)

    page.goto("https://www.ketangpai.cn/#/login")

    page.wait_for_timeout(2000)
    page.locator('//span[@class="el-checkbox__inner"]').set_checked(True)

    page.wait_for_timeout(2000)
    page.locator('//span[@class="el-checkbox__inner"]').set_checked(False)

    page.wait_for_timeout(2000)
    page.locator('//span[@class="el-checkbox__inner"]').check()

    page.wait_for_timeout(2000)
    page.locator('//span[@class="el-checkbox__inner"]').uncheck()





