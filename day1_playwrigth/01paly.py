from playwright.sync_api import sync_playwright
#
# #启动
# p = sync_playwright().start()
#
# #启动浏览器
# browser = p.chromium.launch(headless=False)
#
# #context 新建一个上下文的链接
# context = browser.new_context()
# page =  browser.new_page()
#
# page.goto('https://www.baidu.com')
#
#
# page.close()
# browser.close()
#

# with sync_playwright() as playwright:
#
#
#
#
#     #启动浏览器
#     braowser = playwright.chromium.launch(channel="msedge",headless=False)
#
#     #创建网站上下文
#     context = braowser.new_context()
#
#     #打开sheet 页面
#     page = context.new_page()
#
#     page.goto("https://baidu.com")


#模拟移动端

with sync_playwright() as playwright:

    #模拟手机信息
    Android =  playwright.devices["Galaxy S8"]

    # 打开浏览器
    browser_android = playwright.chromium.launch(headless=False)

    context = browser_android.new_context()
    
    #打开sheet 页面，并创建浏览器传入android 手机信息
    page = browser_android.new_page(**Android)
    page.goto("https://www.baidu.com")




#查看支持那些手机型号
# with sync_playwright() as playwright:
#     print(playwright.devices.keys())






