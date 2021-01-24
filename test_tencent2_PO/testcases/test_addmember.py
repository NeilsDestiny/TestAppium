import pytest
import yaml

from test_tencent2_PO.pages.app import App


def get_data():
    with open("../data/data.yml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        return data

class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_data()["adds"],ids=get_data()["ids"])
    def test_add_member(self, name, gender, phonenum):
        toast = self.main.click_address_list().add_member().add_connect_menual(). \
            edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"
