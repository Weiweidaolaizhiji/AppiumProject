from appium import webdriver

from common.basePage import BasePage
from common.main import Main


class App(BasePage):
    def start(self):
        devices_info = {
            "platformName": "Android",
            "platformVersion": "6",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true"
        }
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', devices_info)
        self.set_implicitly(15)
        # self._driver.implicitly_wait(15)
        return self

    def main(self) ->Main:
        return Main(self._driver)