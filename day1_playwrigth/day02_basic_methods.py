

#导包
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    #打开浏览器
    barwser = playwright.chromium.launch(headless=False)

    #开启上下文，链接的上下文
    content = barwser.new_context()

    #创建一个链接的页面
    page = content.new_page()

    #打开页面
    page.goto("https://www.baidu.com")

    #打开页面后的延迟，类似sleep
    page.wait_for_timeout(5000)


    
    #获取页面标题，后续可以通过页面标题进行断言
    print(page.title())

    #获取页面源码-检查某个元素的代码是否在页面源码中
    print(page.content())


    #页面 截图
    # page.screenshot(path="")

    #刷新页面
    page.reload()

    #上一页
    page.go_back()

    #下一页
    page.go_forward()

