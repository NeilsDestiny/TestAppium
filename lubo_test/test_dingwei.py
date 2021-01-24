from time import sleep
from appium import webdriver

caps={
    "platformName":"android",
    "deviceName":"127.0.0.1:7555",
    "appPackage":"com.xueqiu.android",
    "appActivity":"com.xueqiu.android.common.MainActivity",
    "noReset":"true",
    "dontStopAppOnReset":"true"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
sleep(3)
#返回键操作
driver.back()
driver.back()
driver.quit()
