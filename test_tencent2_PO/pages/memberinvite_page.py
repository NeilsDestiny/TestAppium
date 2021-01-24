from appium.webdriver.common.mobileby import MobileBy

from test_tencent2_PO.pages.base_page import BasePage
from test_tencent2_PO.pages.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    # 点击手动输入添加
    def add_connect_menual(self):
        # self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.find_and_click((MobileBy.XPATH,'//*[@text="手动输入添加"]'))
        return ContactEditPage(self.driver)

    def get_toast(self):
        # ele = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        ele = self.find_get_text((MobileBy.XPATH,'//*[@class="android.widget.Toast"]'))
        return ele
