#coding=utf-8
from common.requests_Base import RestClient
from common.read_data import r
from api.conftest import api_data
from config.allpath import *

api_root_url = r.load_ini(ini_path)["host"]["api_root_url"]

class User(RestClient):   #以下类均继承init方法获取url和发送请求

    def __init__(self, api_root_url,**kwargs):
        super(User, self).__init__(api_root_url)

    def login(self,**kwargs):
        return self.get(api_data["test_url"][0],**kwargs)

    def invitation(self, **kwargs):
        return self.post(api_data["test_url"][1], **kwargs)


    def publish(self,**kwargs):
        return self.post(api_data["test_url"][2], **kwargs)





user = User(api_root_url)

