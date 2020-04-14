import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        # 加入购物车定位信息
        self.join_cart = (By.ID, "join_cart")

    # 定位方法
    def find_join_cart(self):
        return self.base_find(self.join_cart)


# 操作层
class GoodsDetailHandle(BaseHandle):
    # 对象库层对象获取
    def __init__(self):
        self.gdp = GoodsDetailPage()

    # 点击购物车
    def click_join_cart(self):
        self.gdp.find_join_cart().click()


# 业务层
class GoodsDetailProxy:
    # 操作层对象获取
    def __init__(self):
        self.gdh = GoodsDetailHandle()

    # 加入购物车
    def join_to_cart(self):
        self.gdh.click_join_cart()


if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()

    # 打开商品详情业
    driver.get("http://localhost/Home/Goods/goodsInfo/id/104.html")

    # 点击点击加入购物车
    gdp = GoodsDetailProxy()
    gdp.join_to_cart()

    # 查看退出浏览器
    time.sleep(5)
    DriverUtil.quit_driver()
