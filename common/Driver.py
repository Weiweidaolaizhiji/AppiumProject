from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class DriverCommon:
      def getDriver(self):
          devices_info = {
            "platformName": "Android",
            "platformVersion": "6",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset":"true"
          }
          self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',devices_info)
          self._driver.implicitly_wait(15)
          return  self._driver

      def find(self,locator,value):
            self._driver.find_element(locator,value)

