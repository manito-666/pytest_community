

## 项目说明

本项目在实现过程中，把整个项目拆分成requests_Base请求父类、base继承父类，公共方法封装、配置文件、数据封装与读取、测试用例、测试报告、log日志等模块。

1、首先利用Python编写base基类，继承requests_Base的方法，在unity_data中添加url后引入到User类的函数中
2、在case中编写测试用例，调用父类方法，传入参数，编写断言，返回result结果
3、在api中编写allure装饰器内容，根据case中用例返回的result结果进行断言
4、执行api中的main.py，生成allure测试报告

测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。


## 项目部署
通过 pip 工具生成 requirements.txt 文件方便其他用户导包使用，执行命令：
```
pip freeze > requirements.txt

```
在根目录下找到 ```install.py``` 文件,执行后可以下载导入工程需要的包

接着，修改 ```config/setting.ini``` 配置文件，在相应环境下，安装相应依赖之后，在命令行窗口执行命令：
执行page文件目录下的所有测试集
```
pytest api
```
也可执行单个测试用例
```
pytest  api/test_login.py
```
## 项目结构

- common ====>> 各种公共方法，requests父类、base基类，读取配置yaml数据，生成日志等
- config ====>> 配置文件
- api====>> 存放allure测试用例，conftest文件、生成测试报告 
- case====>> 编写测试用例
- data ====>> 存放yaml类型的测试数据
- log ====>> 存放log文件
- requirements.txt ====>> 相关依赖包文件
- install.py ====>> 自动下载依赖包文件

## 编写用例说明
在base中增加函数，url在yaml文件中读取，继承父类方法
在case中编写测试用例与断言，返回请求结果
在api中编写allure构造器函数，对case中返回的结果断言
数据在unity_data.yaml构造，格式： 
    - [xx，xx,期望结果, 期望返回码, 期望返回信息]

## 测试报告效果展示
执行 main.py后查看所有用例执行的测试报告
生成html报告 打开index.html进行查看

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
# 需要提前配置allure环境，才可以直接使用命令行
pytest  page -s -q --alluredir=./page/result/
生成allure的json文件
allure generate ./page/result -o ./page/report --clean
