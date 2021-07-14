import os

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome("C:\Users\林先冠\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GoogleChrome")



def scut():
    browser.get('http://xgfx.bnuz.edu.cn/xsdtfw/sys/emapfunauth/pages/welcome.do?service=%2Fxsdtfw%2Fsys%2Fswmxsyqxxsjapp%2F*default%2Findex.do%3FwxType%3D1#/mrbpa')
   
    browser.maximize_window()
   
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='un']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath(
        "//*[@id='pd']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='index_login_btn']").click()
    time.sleep(50)
    try:
        browser.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/button").click()
        print("华工申报成功")
        time.sleep(3)
        saveFile("华工健康申报签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        # js = 'document.getElementById("btn").click();'
        # browser.execute_script(js)
        saveFile("华工签到代码存在异常"+str(e))


def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message+'\n')


def situyun():
    browser.get('http://situcloud.xyz/auth/login')
    
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['1810010214'])
    browser.find_element_by_xpath(
        "//*[@id='password']").send_keys(os.environ['5200138lin'])
    
    browser.find_element_by_xpath("//*[@id='app']/section/div/div/div/div[2]/form/div/div[5]/button").click()
    time.sleep(10)
    try:
        if("明日再来" in browser.find_element_by_xpath("//*[@id='checkin-div']").text):
            saveFile("明日再来!")
        else:
            # browser.find_element_by_xpath("//*[@id='checkin-div']/a").send_keys(Keys.ENTER)
            js = 'document.getElementById("checkin-div").children[0].click();'
            browser.execute_script(js)
            print("司徒云打卡成功")
        time.sleep(3)
        saveFile("司徒云签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("司徒云签到代码存在异常"+str(e))

if __name__ == '__main__':
    scut()
    situyun()
    # 脚本运行成功,退出浏览器
    browser.quit()
