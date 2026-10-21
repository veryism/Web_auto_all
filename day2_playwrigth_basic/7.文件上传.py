

import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    #第一种方法 input 文件上传方法
    # page.goto("file:///C:/WGY_Python/web_auto/day2_playwrigth_basic/fileupload.html")
    #
    # page.locator("#fu").set_input_files("yuansu.png")

    # 第二种方法非 input 文件上传方法

    page.set_default_timeout(90000)

    page.goto("https://caesium.app")



    #监听下面的操作是否打开了 文件上传窗口
    with page.expect_file_chooser() as file_chooser:

        page.locator('//button[text()=" 浏览……"]').click()

    #监听到了就可以直接上传文件
    file_chooser.value.set_files("yuansu.png")





    time.sleep(3)





