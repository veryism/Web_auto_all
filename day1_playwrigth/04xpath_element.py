
import time

# 导包
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    # 打开浏览器
    barwser = playwright.chromium.launch(headless=False)

    # 开启上下文，链接的上下文
    content = barwser.new_context()

    # 创建一个链接的页面
    page = content.new_page()

    # 打开页面
    page.goto("http://shop.lemonban.com:3344/")


    # 前置调前
    page.get_by_text("登录" ,exact=True).click()


    page.locator('//input[@placeholder="请输入手机号/用户名"]').fill("lemon_auto")
    page.locator('//input[@placeholder="请输入密码"]').fill("lemon123456")

    page.locator('.login-button').click()

    # 找到商品本身，在去找对应的目的文件
    # // div[text() = "骆驼男鞋2022年夏新款真皮休闲舒适软底中年爸爸透气商务凉鞋皮鞋"] / following - sibling::div / div


    time.sleep(3)

# 豆瓣电影选票，通过父子节点，和兄弟节点跨度2个找到对应的 数据
# //a[text()="歌声缘何慢半..."]/parent::li/following-sibling::li[2]/span/a
