from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class OrderPayPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 业务元素定位信息
        # 单选按钮--货到付款
        self.cod = (By.CSS_SELECTOR, '[value="pay_code=cod"]')
        # 超链接--确认支付方式
        self.confirm_pay = (By.LINK_TEXT, '确认支付方式')

    # 定位货到付款单选按钮
    def find_cod(self):
        return self.base_find(self.cod)

    # 定位确认支付方式超链接
    def find_confirm_pay(self):
        return self.base_find(self.confirm_pay)


# 操作层
class OrderPayHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.order_pay_page = OrderPayPage()

    # 点击货到付款
    def click_cod(self):
        self.order_pay_page.find_cod().click()

    # 点击确认支付方式
    def click_confirm_pay(self):
        self.order_pay_page.find_confirm_pay().click()


# 业务层
class OrderPayProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.order_pay_handle = OrderPayHandle()

    # 确认支付方式
    def confirm_pay_way(self):
        # 点击货到付款款
        self.order_pay_handle.click_cod()
        # 点击确认支付方式
        self.order_pay_handle.click_confirm_pay()
