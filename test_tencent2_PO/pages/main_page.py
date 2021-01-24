from appium.webdriver.common.mobileby import MobileBy

from test_tencent2_PO.pages.addresslist_page import AddressListPage
from test_tencent2_PO.pages.base_page import BasePage


class MainPage(BasePage):
    # 点击通信录
    def click_address_list(self):
        self.find_and_click((MobileBy.XPATH,'//*[@text="通讯录"]'))
        return AddressListPage(self.driver)