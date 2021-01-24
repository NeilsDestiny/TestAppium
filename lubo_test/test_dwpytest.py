import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *


class TestDW:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": "true",
            #"dontStopAppOnReset": "true",
            "unicodeKeyBoard":"true",
            "resetKeyBoard":"true"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框里面输入“阿里巴巴”
        4.在搜索结果里选择“阿里巴巴”，然后进行点击
        5.获取这只香港阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        assert current_price > 200

    def test_touchaction(self):
        action = TouchAction(self.driver)
        #获取当前屏幕的宽和高
        window_rect=self.driver.get_window_rect()
        width = window_rect['width']
        heigth = window_rect['height']
        x1 = int(width/2)
        y_start = int(heigth * 0.8)
        y_stop = int(heigth * 0.2)
        #按住屏幕(x1,y_start)位置，等待200ms移动到（x1,y_stop）位置释放并执行
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_stop).release().perform()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main()
