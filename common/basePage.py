import yaml
from appium.webdriver.webdriver import WebDriver

from common.wapper import handle_black


class BasePage:
    def __init__(self,driver : WebDriver = None):
        self._driver = driver

    def set_implicitly(self,time):
        self._driver.implicitly_wait(time)

    # @handle_black
    def find(self,locator,value):
        if isinstance(locator,tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator,value)
        return element

    def finds(self, locator, value):
        if isinstance(locator, tuple):
            element = self._driver.find_elements(*locator)
        else:
            element = self._driver.find_elements(locator, value)
        return element

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        for step in steps:
            element = None
            # if "by" in step.keys():
            #     element = self.find(step["by"],step["locator"])
            if "action" in step:
                action = step["action"]
                if "click" == action:
                    self.find(step["by"],step["locator"]).click()
                if "send" == action:
                    self.find(step["by"],step["locator"]).send_keys(step["value"])



