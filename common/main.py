from appium.webdriver.common.mobileby import MobileBy

from common.basePage import BasePage
from common.search import Search


class Main(BasePage):
    def goto_search(self):
        self.set_implicitly(5)
        self.steps("../common/main.yaml")
        #点击基金
        # self.find("xpath","//*[@resource-id='android:id/tabs']//*[@text='基金']").click()
        return Search(self._driver)