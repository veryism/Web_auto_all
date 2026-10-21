

import time

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("file:///C:/WGY_Python/web_auto/day03_playwright%E9%A1%B5%E9%9D%A2%E7%AD%89%E5%BE%85%E6%9C%BA%E5%88%B6%E5%92%8C%E4%B8%89%E5%A4%A7%E5%88%87%E6%8D%A2/alert.html")

    page.wait_for_timeout(3000)

    def handledlg(dialog):

        page.wait_for_timeout(2000)

        #打印弹窗文本信息
        print(f"弹窗文本信息：{dialog.message}")
        dialog.dismiss() #关闭弹窗

    #注册定义好的函数
    page.on("dialog", handledlg)

    #打开弹窗，playwright 会默认关闭这个弹窗
    page.locator("#abtn").click()

    #如果需要这个弹窗的返回值，需要注册函数
        #注册函数，需要自己定义一个，defhandeldlg(dialog) 传入dialog 作为参数，而且还是要在点击函数之前进行去定义


    page.wait_for_timeout(3000)


