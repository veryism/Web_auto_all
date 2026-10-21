from playwright.sync_api import sync_playwright


#这个是用来保存cookie 的
# stotage  = context.storage_state(path="state.json")

#保存后拿出来使用的
# context = browser.new_context(stotage_state = "state.json")




#显示启动

# def test_login():
#     with sync_playwright() as playwright:
#         broweser = playwright.chromium.launch(headless=False)
#         context = broweser.new_context()
#
#         page = context.new_page()
#
#         page.goto("https://www.baidu.com")
#         page.locator("#s-top-loginbtn").click()
#         page.locator("#TANGRAM__PSP_11__userName").fill("15836266602")
#         page.locator("#TANGRAM__PSP_11__password").fill("wang970202.")
#
#         page.wait_for_timeout(2000)
#         page.locator("#TANGRAM__PSP_11__isAgree").set_checked(True)
#
#         page.wait_for_timeout(2000)
#         page.locator("#TANGRAM__PSP_11__submit").click()
#         page.wait_for_timeout(3000)
#         #保存登录状态的数据到本地
#         page.pause()
#         #跑自动化的时候可以暂停
#         stotage = context.storage_state(path="state.json")
#
#         print(stotage)

def test_login():
    with sync_playwright() as playwright:
        broweser = playwright.chromium.launch(headless=False)
        context = broweser.new_context(storage_state="state.json")

        page = context.new_page()

        page.goto("https://www.baidu.com")

        page.wait_for_timeout(3000)


