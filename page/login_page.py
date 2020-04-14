import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class LoginPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 页面元素定位信息
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.verify_code = (By.ID, "verify_code")
        self.sbtbutton = (By.NAME, "sbtbutton")

    # 定位用户名输入框
    def find_username(self):
        return self.base_find(self.username)

    # 定位密码输入框
    def find_pwd(self):
        return self.base_find(self.password)

    # 定位验证码输入框
    def find_verify_code(self):
        return self.base_find(self.verify_code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.base_find(self.sbtbutton)


# 操作层
class LoginHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.login_page = LoginPage()

    # 输入用户名--参数-用户名
    def input_username(self, text):
        self.base_input_text(self.login_page.find_username(), text)

    # 输入密码--参数-密码
    def input_password(self, text):
        self.base_input_text(self.login_page.find_pwd(), text)

    # 输入验证码--参数-验证码
    def input_verify_code(self, text):
        self.base_input_text(self.login_page.find_verify_code(), text)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.login_handle = LoginHandle()

    # 登录业务
    def login(self, username, password, code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_verify_code(code)
        # 点击登录
        self.login_handle.click_login_btn()


if __name__ == '__main__':
    driver = DriverUtil.get_driver()
    driver.get("http://localhost/Home/user/login.html")

    login_proxy = LoginProxy()
    login_proxy.login("123213", "123123", "123123")

    time.sleep(3)
    DriverUtil.quit_driver()
