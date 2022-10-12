from appium.webdriver.common.mobileby import MobileBy

from common.Driver import DriverCommon
class TestSetting:
    def test_setting(self):
        self.driver=DriverCommon()
        self.driver.getDriver().implicitly_wait(15)
        self.driver.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name'][@text='我的']").click()

