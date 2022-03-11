#coding=utf-8
import os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.result_base import ResultBase
from common.base import user
from common.logger import log
from config.allpath import *
from common.read_data import r
import json


def login_user():
    """
    登录社区
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    #配置文件中获取headers
    headers =json.loads(r.load_ini(ini_path)['host']['headers'])
    #执行继承父类的子类方法
    res = user.login(headers=headers)
    result.success = False
    if res.json()["error"] == 0:
        result.success = True
    else:
        result.error= "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["error"], res.json()["info"])
    result.msg = res.json()["info"]
    result.response = res
    log.info("登录成功后 ==>> 返回结果 ==>> {}".format(result.response.json()))
    return result


def select_invitation(page, page_size, title, type, status, start_time, end_time, game_cd):
    """
       查询帖子
       :return: 自定义的关键字返回结果 result
       """
    # 配置文件中获取headers
    headers = json.loads(r.load_ini(ini_path)['host']['headers'])
    # 执行继承父类的子类方法
    datas = {"page":page,"page_size":page_size,"tiele":title,"type":type,"status":status,"start_time":start_time,"end_time":end_time, "game_cd":game_cd}

    result = ResultBase()
    res = user.invitation(data=datas, headers=headers)
    result.success = False
    if res.json()["errno"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["errno"], res.json()["errmsg"])
    result.msg = res.json()["errmsg"]
    result.response = res
    log.info("查询成功后 ==>> 返回结果 ==>> {}".format(result.response.json()))
    return result


# if __name__ == '__main__':
#     # login_user()
#     select_invitation(1,20,"",0,0,1644249600,1646927999, "1001")