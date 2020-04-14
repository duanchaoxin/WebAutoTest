from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class OrderListPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()

        # 页面元素定位信息
        # 超链接--待付款
        self.wait_pay = (By.LINK_TEXT, "待付款")
        # 超链接--立即支付
        self.now_pay = (By.LINK_TEXT, '立即支付')

    # 定位待付款超链接
    def find_wait_pay(self):
        return self.base_find(self.wait_pay)

    # 定位立即支付超链接
    def find_now_pay(self):
        return self.base_find(self.now_pay)


# 操作层
class OrderListHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.olp = OrderListPage()

    # 点击待付款
    def click_wait_pay(self):
        self.olp.find_wait_pay().click()

    # 点击立即支付
    def click_now_pay(self):
        self.olp.find_now_pay().click()


# 业务层
class OrderListProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.olh = OrderListHandle()

    # 去支付
    def go_pay(self):
        # 点击待付款
        self.olh.click_wait_pay()
        # 点击立即支付
        self.olh.click_now_pay()
