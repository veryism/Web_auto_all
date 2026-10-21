
import time


from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()


    # select 标签的处理方法
    # page.goto("file:///C:/WGY_Python/web_auto/day2_playwrigth_basic/select.html")
    #
    # page.locator("#m-select").select_option("6")


    # 非 select 标签的处理方法

    page.goto("https://www.baidu.com/")


    page.locator("#s-usersetting-top").hover()

    page.locator('//span[text()="高级搜索"]').click()

    time.sleep(3)


    page.locator('//span[@class="c-select-selected-value" and  text()="时间不限"]').click()


    time.sleep(3)

    page.locator('//p[@class="c-select-item" and text()="一年内"]').click()










    time.sleep(3)
