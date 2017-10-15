# coding:utf-8
# for jd.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

# 不设置个人目录的话，每次重新载入太费时间
option = webdriver.ChromeOptions()
#chrome地址栏输入 chrome://version/ 查看“个人资料路径” 拷贝到下面替换
option.add_argument('--user-data-dir=C:\Users\xxxx\AppData\Local\Google\Chrome\User Data\Profile 1') #设置成用户自己的数据目录

browser = webdriver.Chrome(chrome_options=option)

#不设置个人资料路径
#browser = webdriver.Chrome()

browser.maximize_window();
browser.get('http://www.jd.com')



assert "JD" in browser.title #正常 无异常抛出

# login
def login(user_name, user_passwordd):
    # 载入缓存的话，请登录前面带用户id，采用部分匹配文字
    if browser.find_element_by_partial_link_text('请登录'):
        browser.find_element_by_partial_link_text('请登录').click()
        print(u"请登录")
    if browser.find_element_by_link_text('账户登录'):
        browser.find_element_by_link_text('账户登录').click()
        print(u'账户登录')
    if browser.find_element_by_id('loginname'):
        browser.find_element_by_id('loginname').clear()
        browser.find_element_by_id('loginname').send_keys(user_name)
        print('loginname')
    if browser.find_element_by_id('nloginpwd'):
        browser.find_element_by_id('nloginpwd').send_keys(user_passwordd)
        print('nloginpwd')
    if browser.find_element_by_id('loginsubmit'):
        browser.find_element_by_id('loginsubmit').click()
        print('loginsubmit')
    time.sleep(1)

    now = datetime.datetime.now()
    print(now)
    print("login successful", now.strftime('%Y-%m-%d %H:%M:%S'))

# buy
def buy_on_time(buy_time):
    print(' in buy_on_time %S',buy_time)

    #商品页面
    browser.get('http://item.jd.com/2149294.html')
    # 先打开再说

    if browser.find_element_by_id('InitCartUrl'):
        browser.find_element_by_id('InitCartUrl').click()
        print('InitCartUrl')
    # 找不到这个额按钮，有时间再看看
    #if browser.find_element_by_link_text('去购物车结算'):
    #    browser.find_element_by_link_text('去购物车结算').click()
    #    print('GotoShoppingCart')
    #另外打开购物车页面
    browser.get('https://cart.jd.com/cart.action')
    if browser.find_element_by_link_text('去结算'):
        browser.find_element_by_link_text('去结算').click()
        print(u'去结算')

    while True:
        print ('in 1st wile true')
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buy_time:
            while True:
                print('in 2nd while true')
                try:
                    if browser.find_element_by_id('order-submit'):
                        browser.find_element_by_id('order-submit').click() #秒杀的话，最后提交订单的价格是活动价格么？
                        print('order-submit')
                except:
                    time.sleep(0.1)

        time.sleep(0.1)
# 购物车下单
def buy_on_time_from_cart(buy_time):
    browser.get('https://cart.jd.com/cart.action')
    if browser.find_element_by_link_text('去结算'):
        browser.find_element_by_link_text('去结算').click()
        print(u'去结算')
    while True:
        print ('in 1st wile true')
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buy_time:
            while True:
                print('in 2nd while true')
                try:
                    if browser.find_element_by_id('order-submit'):
                        browser.find_element_by_id('order-submit').click() #秒杀的话，最后提交订单的价格是活动价格么？
                        print('order-submit')
                except:
                    time.sleep(0.1)

        time.sleep(0.1)
#参数是用户名和密码
login('xxx@xxx.com','xxxxxx')

buy_on_time('2017-08-15 07:59:00')
