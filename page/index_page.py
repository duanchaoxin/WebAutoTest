import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


# 对象库层
class IndexPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 页面元素定位信息
        self.login_link = (By.LINK_TEXT, "登录")
        self.search_input = (By.ID, "q")
        self.search_btton = (By.CLASS_NAME, "ecsc-search-button")
        self.my_cart = (By.ID, "hd-my-cart")
        self.my_order = (By.LINK_TEXT, "我的订单")

    # 登录超链接
    def find_login_link(self):
        # 调用父类中的定位方法实现
        return self.base_find(self.login_link)

    # 搜索框
    def find_search_input(self):
        return self.base_find(self.search_input)

    # 搜索按钮
    def find_search_button(self):
        return self.base_find(self.search_btton)

    # 我的购物车
    def find_my_cart(self):
        return self.base_find(self.my_cart)

    # 我的订单
    def find_my_order(self):
        return self.base_find(self.my_order)


# 操作层
class IndexHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.index_page = IndexPage()

    # 登录超链接 -- 点击
    def click_login_link(self):
        self.index_page.find_login_link().click()

    # 搜索框 -- 输入
    def input_search_input(self, text):
        self.base_input_text(self.index_page.find_search_input(), text)

    # 搜索按钮 -- 点击
    def click_search_button(self):
        self.index_page.find_search_button().click()

    # 点击我的购物车
    def click_my_cart(self):
        self.index_page.find_my_cart().click()

    # 点击我的订单
    def click_my_order(self):
        self.index_page.find_my_order().click()


# 业务层
class IndexProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.index_handle = IndexHandle()

    # 前往登录页
    def to_login_page(self):
        # 点击登录超链接
        self.index_handle.click_login_link()

    # 搜索商品
    def search_goods(self, goods_name):
        # 输入商品名称
        self.index_handle.input_search_input(goods_name)
        # 点击搜索按钮
        self.index_handle.click_search_button()

    # 进入购物车页面
    def to_cart_page(self):
        self.index_handle.click_my_cart()

    # 进入我的订单页面
    def to_order_list_page(self):
        self.index_handle.click_my_order()


if __name__ == '__main__':
    # 获取浏览器驱动
    driver = DriverUtil.get_driver()
    # 打开首页
    driver.get("http://localhost/")

    # 点击登录连接  业务层代码
    index_parxy = IndexProxy()
    # index_parxy.to_login_page()
    index_parxy.search_goods("小米")
    # 暂停关闭浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
