import json
import unittest
import time
import os

from config import BASE_DIR, BASE_HOST
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil, LogUtil, case_driver_quit, jietu
from parameterized import parameterized

logger = LogUtil.get_logger()


# 读取json 构造参数化数据
def get_data():
    # 1.创建参数化数据的结果列表
    result = []
    # 2.读取json 构造参数化数据
    # 通过项目绝对路径+数据位置
    with open(BASE_DIR + "/data/test_login.json", "r", encoding="utf-8") as f:
        python_data = json.load(f)
        for i in python_data:
            username = i["username"]
            password = i["password"]
            code = i["code"]
            yuqi = i["yuqi"]
            result.append((username, password, code, yuqi))
    # 3.返回参数化数据的结果列表
    logger.info("参数化数据:{}".format(result))
    return result


# 创建测试类
class TestLogin(unittest.TestCase):
    # 类级别的setUpClass
    @classmethod
    def setUpClass(cls):
        # 浏览器驱动
        cls.driver = DriverUtil.get_driver()
        cls.index_page = IndexProxy()
        cls.login_page = LoginProxy()
        logger.info("获取浏览器驱动对象:{}".format(cls.driver))
        logger.info("获取页面对象:{}".format((cls.index_page, cls.login_page)))

    # 方法级别的sutUp
    def setUp(self):
        # 用例前置条件
        # 前置 打开首页 进入登录页
        self.driver.get(BASE_HOST)
        logger.info("用例开始执行,初始化页面:{}".format(BASE_HOST))
        # 进入登录页 登录页业务层方法 -->对象
        self.index_page.to_login_page()

    def tearDown(self):
        time.sleep(2)
        logger.info("用例执行结束...")

    # 类级别的tearDownClass
    @classmethod
    def tearDownClass(cls):
        # if BASE_DIR != os.getcwd():
        #     DriverUtil.quit_driver()
        case_driver_quit()

    # 添加测试方法
    @parameterized.expand([("13012345678", "123456", "8888", "我的账户111")])
    def test01_login(self, username, password, code, yuqi):
        logger.info("用例参数数据:{}".format((username, password, code, yuqi)))
        # 业务 -- 登录页面登录操作 登录页业务层代码 --> 登录页对象
        self.login_page.login(username, password, code)
        logger.info("用户登录:{}".format((username, password, code)))
        # 断言 -- 登录成功的标题
        time.sleep(3)
        title = self.driver.title
        try:
            self.assertIn(yuqi, title)
        except Exception as e:
            # 抛异常 --> 用例执行失败
            # 截图
            jietu()
            raise e

# Fixture
# 参数化
