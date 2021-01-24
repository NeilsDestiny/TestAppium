# 存放对app的操作 ： 启动、关闭、重启、进入首页。。。
from appium import webdriver
from test_tencent2_PO.pages.base_page import BasePage
from test_tencent2_PO.pages.main_page import MainPage

class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                # 不清空本地缓存，启动app
                "noReset": "true",
                "ensureWebviewsHavePages": True,
                "dontStopAppOnReset": "true",
                "waitForIdleTimeout": 1  # 设置页面等待空闲状态的时间为0秒
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 添加隐式等待5s
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self):
        return MainPage(self.driver)
