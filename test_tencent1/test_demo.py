from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestTencent:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            #不清空本地缓存，启动app
            "noReset": "true",
            "ensureWebviewsHavePages": True,
            "dontStopAppOnReset": "true",
            "waitForIdleTimeout": 0  #设置页面等待空闲状态的时间为0秒
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #添加隐式等待5s
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath('//*[@text="外出打卡"]')
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        res = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/mn").text
        assert res == "外出打卡成功"

