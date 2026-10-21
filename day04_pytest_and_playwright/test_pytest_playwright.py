
from playwright.sync_api import sync_playwright



#显示启动
# def test_login():
#     with sync_playwright() as playwright:
#
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("http://shop.lemonban.com")


#隐式启动
def test_login(page):
    page.goto("http://shop.lemonban.com/")


    print(page.title)