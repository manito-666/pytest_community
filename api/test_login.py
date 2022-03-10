import pytest
import allure
from case.community import login_user
from api.conftest import api_data
from common.logger import log

class Test_Login():
    @allure.feature("功能点：社区用户登陆")
    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {except_result},{error},{uid} 】")
    @pytest.mark.parametrize("except_result, error, uid", api_data["test_login"])

    def test_login(self, except_result, error, uid):
        log.info("*************** 开始执行用例 ***************")
        result =login_user()
        assert result.success == except_result
        assert result.response.json().get("error") == error
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(error, result.response.json().get("error")))
        assert uid in result.msg["uid"]
        log.info("uid ==>> 期望结果：{}， 实际结果：【 {} 】".format(uid, result.response.json().get("info")['uid']))
        log.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_login.py"])
