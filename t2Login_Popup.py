#知音楼的安装，启动，自动处理弹窗，权限；
from appium import webdriver
import unittest
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
'''安装测试环境知音楼APP'''
import os
os.system("adb install /Users/tal/yachtest.apk")#安装知音楼app
'''配置及启动知音楼；'''
class LoginTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',#模拟器:emulator-5554
            'platformVersion': '11.0',
            'appPackage': 'com.tal100.yach.capi',
            'appActivity': 'com.tal100.yach.main.activity.MainTabActivity',
            'automationName': 'UiAutomator2',
            #'noReset': "True",#为复现首次安装app弹窗，注释
            #'fullReset': "False"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def testCase(self):
        """知音楼账号密码自动登录"""
        driver = self.driver
 #隐形等待，测试环境知音楼及模拟器运行中加载时间较慢；
        driver.implicitly_wait(10)
        #time.sleep(7)#知音楼启动调试时可能需要强制等待；
        driver.find_element_by_id("com.tal100.yach.capi:id/btn_privacy_policy_positive").click()#点击同意并继续
        #time.sleep(2)
        driver.find_element_by_id("com.tal100.yach.capi:id/et_account").send_keys("13301266607")#输入手机号
        driver.find_element_by_id('com.tal100.yach.capi:id/et_mobile_code').send_keys("111111")#输入写死的验证码
        driver.find_element_by_id("com.tal100.yach.capi:id/check_login_agreement").click()#点击勾选协议
        driver.find_element_by_id("com.tal100.yach.capi:id/btn_login").click()#点击登录按钮
        #time.sleep(60)#调试时模拟器内登录知音楼时间太长；
        '''自动处理权限弹窗，知音楼包括app内开通权限弹窗及Android系统内允许弹窗，验证可连续处理成功'''
        for i in range(4):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass
        driver.find_element_by_id("com.tal100.yach.capi:id/btn_selectPositive").click()  # app内权限请求弹窗通讯录-开通权限
        time.sleep(1)
        #driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_buttonAndroid").click()  # 系统权限请求弹窗-允许
        driver.find_element_by_xpath("//*[@text='允许']").click()  # 系统权限请求弹窗-允许
        time.sleep(1)
        driver.find_element_by_id("com.tal100.yach.capi:id/btn_selectPositive").click()  # app内权限请求弹窗存储-开通权限
        time.sleep(1)
        driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_button").click()  # Android系统权限请求弹窗-允许
        time.sleep(1)
        '''处理不彻底，连接到我的小米手机又换成了MIUI的系统弹窗样式，模拟器可以通过，应该有系统级强制允许吧，后边研究研究'''
        #driver.quit()
