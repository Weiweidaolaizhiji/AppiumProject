from appium.webdriver.common.mobileby import MobileBy

from common.basePage import BasePage


class Search(BasePage):
    def searchname(self):
        self.steps("../common/searchname.yaml")
        # self.find(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        # self.find(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('海康')
        # self.find(MobileBy.XPATH,"//*[@text='SZ002415']").click()