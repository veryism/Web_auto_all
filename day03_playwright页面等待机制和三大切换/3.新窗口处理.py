import time

from playwright.sync_api import sync_playwright


# 多个窗口的函数封装

def switch_windwos(tatget_title,context):

    for sheets in context.pages:

        if  tatget_title in sheets.title():

            sheets.bring_to_front()
            return sheets
    raise Exception(f"找不到指定的窗口{tatget_title}")







with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.baidu.com/")



    #新窗口处理 ，如果不进行处理默认还是在第一个窗口，所以新的 窗口需要添加一个处理方式，可以使用with 来进行处理
    #监听窗框，使用context.expect_page()函数监测打开的窗口，这个操作方法和文件按上传的方式 一样的

# =================== 案例一 单窗口 ===================
#     with context.expect_page() as new_page_info:
#         #打开窗口
#         page.locator('//a[contains(text(),"新闻")]').click()
#
#     #获取新窗口的对象
#     new_page = new_page_info.value
#
#     # 使用定义的函数来进行操作
#     new_page.locator('#ww').fill("柠檬班")
# =================== 案例一 单窗口 ===================


# =================== 案例二 多窗口 ===================

    page.locator('//a[contains(text(),"新闻")]').click()
    page.locator('//a[contains(text(),"hao123")]').click()
    page.locator('//a[@href  = "http://map.baidu.com"]').click()
    page.locator('//a[@href = "http://tieba.baidu.com/"]').click()

    page.wait_for_timeout(3000)


    #进入到某一个窗口进行操作
    # for sheets in context.pages:
    #
    #     print("获取文件的title:",sheets.title())
    #
    #
    #     if  "hao123" in sheets.title():
    #
    #         sheets.bring_to_front()
    #
    #         sheets.locator('//input[@class="textInput input-hook"]').fill("柠檬班")
    #
    #         time.sleep(1)





    #进入到某一个窗口进行操作，封装成了函数

    # 内置for 循环，拿到所有的title 做出判断 ，然后返回回来
    sheets = switch_windwos("hao123",context)
    sheets.locator('//input[@class="textInput input-hook"]').fill("柠檬班")
    time.sleep(1)

    page.wait_for_timeout(5000)