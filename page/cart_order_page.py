from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class CartOrderPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()

        # 超链接--提交订单
        self.submit_order = (By.LINK_TEXT, '提交订单')

    # 定位提交订单超链接
    def find_submit_order(self):
        return self.base_find(self.submit_order)


# 操作层
class CartOrderHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.cart_order_page = CartOrderPage()

    # 点击提交订单超链接
    def click_submit_order(self):
        self.cart_order_page.find_submit_order().click()


# 业务层
class CartOrderProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.cart_order_handle = CartOrderHandle()

    # 提交订单
    def submit_order(self):
        # 点击提交订单超
        self.cart_order_handle.click_submit_order()
