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

    def test_add_member(self):
        name = 'test1'
        gender = '男'
        phonenum = '13645678912'
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        # self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        #滑动查找添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath( "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        if gender == '女':
            self.driver.find_element_by_xpath( "//*[@text='女']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys(phonenum)
        #点击保存
        self.driver.find_element_by_id("com.tencent.wework:id/gur").click()

        ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele
