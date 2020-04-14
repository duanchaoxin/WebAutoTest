import json
import unittest

# 1.测试类
import time

import os
from parameterized.parameterized import parameterized

from config import BASE_DIR, BASE_HOST
from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil, text_exists, case_driver_quit, load_json


# 读取json 构造参数化数据
def get_data():
    # 1.创建结果列表
    result = []
    # 2.读取json数据构造参数化数据
    python_data = load_json("test_cart.json")
    for i in python_data:
        goods_name = i["goods_name"]
        yuqi = i["yuqi"]
        result.append((goods_name, yuqi))
    # 3.返回结果列表
    return result


class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 浏览器驱动
        cls.driver = DriverUtil.get_driver()
        cls.indpex_page = IndexProxy()
        cls.goods_search_page = GoodsSearchProxy()
        cls.goods_detail_page = GoodsDetailProxy()

    # 方法级别的sutUp
    def setUp(self):
        # 用例前置条件
        # 前置 打开首页 进入登录页
        self.driver.get(BASE_HOST)

    def tearDown(self):
        time.sleep(2)

    # 类级别的tearDownClass
    @classmethod
    def tearDownClass(cls):
        # if BASE_DIR != os.getcwd():
        #     DriverUtil.quit_driver()
        case_driver_quit()

    # 2. 测试方法  "小米"  "添加成功"
    @parameterized.expand(get_data())
    def test01_add_goods_to_cart(self, goods_name, yuqi):
        # 搜索小米  首页 --  搜索功能
        self.indpex_page.search_goods(goods_name)
        # 点击商品进入详情页   商品搜索页 -- 进入详情页
        self.goods_search_page.to_goods_detail()
        # 点击加入购物车    商品详情页 -- 添加购物车
        self.goods_detail_page.join_to_cart()

        # 判断页面中是否存在添加成功
        time.sleep(2)
        DriverUtil.switch_page()
        # msg = self.driver.find_element_by_css_selector(".conect-title span").text
        # self.assertIn(yuqi, msg)
        result = text_exists(yuqi)
        self.assertTrue(result)
        # 3. 业务断言

        # 4. fixture


        # 5. 参数化
