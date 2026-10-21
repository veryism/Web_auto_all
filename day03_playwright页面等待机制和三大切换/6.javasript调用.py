import time

from playwright.sync_api import sync_playwright,expect



with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.baidu.com/")


    #使用js命令
    # page.evaluate(' document.getElementById("chat-submit-button").innerHTML="百度三下" ')
    # page.evaluate(' document.getElementById("chat-textarea").setAttribute("placeholder","你好")')
    #
    # page.evaluate(' document.getElementById("chat-textarea").style.backgroundColor="red"')
    #
    # time.sleep(5)

    #扩展使用js 脚本

    page.locator("#chat-submit-button").evaluate('ele=>ele.innerHTML="百度三下" ')
    page.locator("#chat-textarea").evaluate('ele=>ele.setAttribute("placeholder","你好") ')
    page.locator("#chat-textarea").evaluate('ele=>ele.style.backgroundColor="red" ')

    #ele 是一个变量名，指前面的locator 里的元素，这个名字可以自己随便起
    #扩展箭头里面的函数。js 里的一种写法

    #=>箭头函数（arrow Function） 用简介定义一个函数，它的作用是将传入的参数 ele 效果等于定义一个函数，ele 作为参数

    

    time.sleep(5)









