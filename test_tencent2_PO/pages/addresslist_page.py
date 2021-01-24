from test_tencent2_PO.pages.base_page import BasePage
from test_tencent2_PO.pages.memberinvite_page import MemberInvitePage


class AddressListPage(BasePage):
    # 点击添加成员
    def add_member(self):
        # 滑动查找添加成员
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().'
        #                                                 'text("添加成员").instance(0));').click()
        self.scroll_find_click("添加成员")

        return MemberInvitePage(self.driver)