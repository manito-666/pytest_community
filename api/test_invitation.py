import pytest
import allure
from case.community import select_invitation
from api.conftest import api_data
from common.logger import log
# 社区帖子查询
class Test_invitation1():
    @allure.feature("功能点：社区帖子查询")
    @allure.story("用例--查询该游戏下的所有类型的帖子")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("该用例是针对获取所有帖子查询接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {page}, {page_size}, {title}, {type}, {status}, {start_time}, {end_time}, {game_cd}, {except_result},{except_code},{except_msg} 】")
    @pytest.mark.parametrize("page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg", api_data["test_invitation1"])

    def test_invitation(self, page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        result =select_invitation(page, page_size, title, type, status, start_time, end_time, game_cd)
        assert result.success == except_result
        assert result.response.status_code == 200
        assert result.response.json().get("errno") == except_code
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("errno")))
        assert except_msg in result.msg
        log.info("msg ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_msg, result.response.json().get("errmsg")))
        log.info("*************** 结束执行用例 ***************")

class Test_invitation2():
    @allure.feature("功能点：社区帖子查询")
    @allure.story("用例--查询官方公告为已发布的帖子")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("该用例是针对类型来获取帖子查询接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {page}, {page_size}, {title}, {type}, {status}, {start_time}, {end_time}, {game_cd}, {except_result},{except_code},{except_msg} 】")
    @pytest.mark.parametrize(
        "page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg",
        api_data["test_invitation2"])
    def test_invitation2(self, page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        result =select_invitation(page, page_size, title, type, status, start_time, end_time, game_cd)
        assert result.success == except_result
        assert result.response.status_code == 200
        assert result.response.json().get("errno") == except_code
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("errno")))
        assert except_msg in result.msg
        log.info("msg ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_msg, result.response.json().get("errmsg")))
        log.info("*************** 结束执行用例 ***************")

class Test_invitation3():
    @allure.feature("功能点：社区帖子标题查询")
    @allure.story("用例--根据标题来查询帖子")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("该用例是针对根据标题来获取帖子查询接口的测试")
    @allure.issue("🖱️", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("🖱️", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {page}, {page_size}, {title}, {type}, {status}, {start_time}, {end_time}, {game_cd}, {except_result},{except_code},{except_msg} 】")
    @pytest.mark.parametrize(
        "page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg",
        api_data["test_invitation3"])
    def test_invitation2(self, page, page_size, title, type, status, start_time, end_time, game_cd, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        result =select_invitation(page, page_size, title, type, status, start_time, end_time, game_cd)
        assert result.success == except_result
        assert result.response.status_code == 200
        assert result.response.json().get("errno") == except_code
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("errno")))
        assert except_msg in result.msg
        log.info("msg ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_msg, result.response.json().get("errmsg")))
        log.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_invitation.py"])
