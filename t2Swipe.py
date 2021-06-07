# 知音楼的安装，启动，自动处理弹窗，权限；
from appium import webdriver
import unittest
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''安装测试环境知音楼APP'''
# import os
# os.system("adb install /Users/tal/yachtest.apk")#安装知音楼app
'''配置及启动知音楼；'''
desired_caps = dict()
desired_caps['platformName'] = 'Android'  # 系统
desired_caps['platformVersion'] = '11.0'  # 系统版本
desired_caps['deviceName'] = '822ac22d'  # 设备名
desired_caps['appPackage'] = 'com.tal100.yach.capi'  # 要打开的应用程序包名
desired_caps['appActivity'] = 'com.tal100.yach.main.activity.MainTabActivity'  # 要打开的应用程序的界面名
desired_caps['udid'] = '822ac22d'  # 连接设备的唯一标识
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接 appium 服务器
driver.implicitly_wait(10)

time.sleep(10)


# 获取屏幕宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 左滑
def swipe_left(t):
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1, t)


# 右滑
def swipe_right(t):
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1, t)


# 上滑
def swipe_up(t):
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y, t)
    i = 0
    while i < 10:
        try:
            driver.find_element_by_name('OKR助手').click()
            break
        except Exception as e:
            driver.swipe(x1, y1, x1, y, t)
            i = i + 1
            '''以知音楼APP上滑举例滑动并循环查找元素，直到查到为止，但是测试环境知音楼的聊天页是动态，以OKR助手为例，不一定在哪个位置，我的账号里是第二页'''

# 下滑
def swipe_down(t):
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y, t)


def swipe_on(direction):
    if direction == 'up':
        swipe_up(t)
    elif direction == 'down':
        swipe_down(t)
    elif direction == 'left':
        swipe_left(t)
    else:
        swipe_right(t)

t = 3000
swipe_on('up')
'''代码没有优化，只是实现，没有很好的封装'''


