import time

from playwright.sync_api import sync_playwright




with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.set_default_timeout(8000)
    page.goto("https://mail.qq.com/")

# --------------------- 单层iframe --------------------------
#     frame =  page.frame_locator("#login_frame")
#
#     frame.locator('#switcher_plogin').click()
#
#     frame.locator('#u').fill("859992953@qq.com")
#     frame.locator('#p').fill("wang970202")
#
#     time.sleep(5)
#
#     frame.locator('//a[@class="login_button"]').click()

# --------------------- 单层iframe --------------------------


# --------------------- 多层iframe --------------------------
    frame =  page.frame_locator('//iframe[@allow="local-network-access" and @title="QQ登录"]').frame_locator("#ptlogin_iframe")

    frame.locator('#switcher_plogin').click()
    
    frame.locator('#u').fill("859992953@qq.com")
    frame.locator('#p').fill("wang970202")

    time.sleep(5)

    frame.locator('//a[@class="login_button"]').click()

# --------------------- 多层iframe --------------------------

    time.sleep(5)

