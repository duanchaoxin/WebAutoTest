# 页面中的跟浏览器驱动有关的公共操作抽取出来
# 封装在一个单独的类中,作为其他页面对象的基类
from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtil


# 对象库的基类
class BasePage:
    # 元素定位
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def base_find(self, loc):
        ele = self.driver.find_element(loc[0], loc[1])
        ele = WebDriverWait(DriverUtil.get_driver(), 10, 0.5).until(lambda x: x.find_element(loc[0], loc[1]))
        return ele


# 操作层基类 元素相关的操作
class BaseHandle:
    # 元素操作
    def base_input_text(self, element, text):
        # 给某个元素输入指定内容
        element.clear()
        element.send_keys(text)
