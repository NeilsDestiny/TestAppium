from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_tencent2_PO.pages.base_page import BasePage

#编辑成员信息
class ContactEditPage(BasePage):
    def edit_name(self,name):
        # self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find_and_sendkeys((MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText"),name)
        return self

    def edit_gender(self,gender):
        locator = (MobileBy.XPATH,"//*[@text='男']")
        ele = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        # self.driver.find_element_by_xpath("//*[@text='男']").click()
        if gender == '女':
            # self.driver.find_element_by_xpath("//*[@text='女']").click()
            self.find_and_click((MobileBy.XPATH,"//*[@text='女']"))
        else:
            # self.driver.find_element_by_xpath("//*[@text='男']").click()
            self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
        return self

    def edit_phonenum(self,phonenum):
        # self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys(phonenum)
        self.find_and_sendkeys((MobileBy.ID,"com.tencent.wework:id/eq7"),phonenum)
        return self

    def click_save(self):
        from test_tencent2_PO.pages.memberinvite_page import MemberInvitePage
        # self.driver.find_element_by_id("com.tencent.wework:id/gur").click()
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/gur"))
        return MemberInvitePage(self.driver)