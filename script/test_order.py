import time
import unittest

from config import BASE_HOST
from page.cart_order_page import CartOrderProxy
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.order_list_page import OrderListProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil, case_driver_quit, text_exists


class TestOrder(unittest.TestCase):
    # fixture -- 类级别  封装浏览器初始化和销毁操作
    @classmethod
    def setUpClass(cls):
        # 初始化浏览器
        cls.driver = DriverUtil.get_driver()
        cls.index_page = IndexProxy()
        cls.cart_page = CartProxy()
        cls.cart_order_page = CartOrderProxy()
        cls.order_list_page = OrderListProxy()
        cls.order_pay_page = OrderPayProxy()

    @classmethod
    def tearDownClass(cls):
        # 销毁浏览器
        case_driver_quit()

    # fixture -- 方法级别 用例的前置条件和后置处理
    def setUp(self):
        # 回到首页
        self.driver.get(BASE_HOST)

    def tearDown(self):
        # 等待查看
        time.sleep(3)

    # 创建测试方法
    def test01_submit_order(self):
        self.index_page.to_cart_page()
        self.cart_page.go_balance()
        time.sleep(5)
        self.cart_order_page.submit_order()
        time.sleep(3)
        result = text_exists("订单提交成功，请您尽快付款")
        self.assertTrue(result)

    # 测试订单支付 "订单提交成功，我们将在第一时间给你发货"
    def test02_pay_order(self):
        self.index_page.to_order_list_page()
        #  切窗口
        DriverUtil.switch_window()
        self.order_list_page.go_pay()
        #  切窗口
        DriverUtil.switch_window()
        self.order_pay_page.confirm_pay_way()
        time.sleep(3)
        result = text_exists("订单提交成功，我们将在第一时间给你发货")
        self.assertTrue(result)

# 参数化
