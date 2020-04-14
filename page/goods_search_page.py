import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class GoodsSearchPage(BasePage):
    def __init__(self):
        super().__init__()
        # 商品名称定位信息
        self.goods_name = (By.CSS_SELECTOR, ".s_xsall .shop_name2 a")

    def find_goods_name(self):
        return self.base_find(self.goods_name)

# 操作层
class GoodsSearchHandle(BaseHandle):
    def __init__(self):
        self.gsp = GoodsSearchPage()

    # 点击商品名
    def click_goods_name(self):
        self.gsp.find_goods_name().click()


# 业务层
class GoodsSearchProxy:
    def __init__(self):
        self.gsh = GoodsSearchHandle()

    # 进入商品详情
    def to_goods_detail(self):
        self.gsh.click_goods_name()

if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()

    # 打开商品搜索页
    driver.get("http://localhost/Home/Goods/search.html?q=%E5%B0%8F%E7%B1%B3")

    # 点击商品
    gsp = GoodsSearchProxy()
    gsp.to_goods_detail()

    # 查看退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
