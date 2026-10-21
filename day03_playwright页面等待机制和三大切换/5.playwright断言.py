

from playwright.sync_api import sync_playwright,expect



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.baidu.com/")


    # #创建一个监视器，用来监听窗口语句
    # with context.expect_page() as new_page_info:
    #     page.locator('//a[contains(text(),"新闻")]').click()
    #
    # # #获取新的窗口
    # new_page = new_page_info.value
    #
    # #这个是用来断言的，断言打开的新窗口，根据 title 来进行断言
    # expect(new_page).to_have_title("百度新闻——海量中文资讯平台")
    #
    # #在新窗口上的搜索框输入柠檬班
    # new_page.locator("#ww").fill("柠檬班")
    #
    # page.wait_for_timeout(3000)






    with context.expect_page() as new_page_info:
        page.locator('//a[contains(text(),"新闻")]').click()


    new_page = new_page_info.value
    # ==========================检查页面信息==========================
    expect(new_page).to_have_title("百度新闻——海量中文资讯平台")
    expect(new_page).to_have_url("https://news.baidu.com/")
    # ==========================检查页面信息==========================

    #1.检查元素的属性
    expect(new_page.locator("#ww")).to_have_attribute("name","word")

    #2.检查元素属性的id
    expect(new_page.locator("#ww")).to_have_id("ww")

    #3.检查元素的数量
    expect(new_page.locator("#s_btn_wr")).to_have_count(1)

    #4. 检查元素的文本
    expect(new_page.locator('//a[@href="//help.baidu.com" ]')).to_have_text("帮助")



    new_page.locator("#ww").fill("柠檬班")

    page.wait_for_timeout(3000)








