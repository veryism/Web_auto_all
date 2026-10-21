

'''

编写自动化脚本完成商城项目登录->搜索商品->浏览商品->下单功能脚本,并添加断言[expect]，提交py文件。

http://mall.lemonban.com:3344/ lemon_python 12345678

注意:找不到元素的时候，加上强制等待，比如登录后页面定位元素
'''



from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("http://shop.lemonban.com:3344/")

    #编写自动化脚本完成商城项目登录->搜索商品->浏览商品->下单功能脚本,并添加断言[expect]，提交py文件。

    #登录
    page.locator('//a[text()="登录"]').click()
    page.locator('//input[@placeholder = "请输入手机号/用户名"]').fill("lemon_python")
    page.locator('//input[@placeholder ="请输入密码"]').fill("12345678")


    page.locator('//a[@class="login-button"]').click()

    page.wait_for_timeout(3000)
    page.locator('(//input[@class="search-input" ])[3]').fill("包")
    page.locator('(//input[@type="submit" and @class="search-btn" ])[3]').click()


    page.get_by_text("真皮圆筒包2022新款潮爆款时尚百搭休闲单肩斜挎牛皮圆形桶包包女").click()

    page.wait_for_timeout(3000)







