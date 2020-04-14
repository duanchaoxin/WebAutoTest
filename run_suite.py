import time
import unittest

# from tools.HTMLTestRunner import HTMLTestRunner


from config import BASE_DIR
from script.test_cart import TestCart
from script.test_login import TestLogin

# 创建套件 组织用例
from script.test_order import TestOrder
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))

# 创建运行器 执行用例
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)
# HTMLTestRunner(文件流,标题,描述)
filename = BASE_DIR + "/report/tpshop{}.html".format(time.strftime("%H%m%d%H%M%S"))
with open(filename, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="报告标题", description="报告描述")
    runner.run(suite)

# 当前执行时
# 执行完登录用例后,浏览器自动关闭
# 然后新启动浏览器,执行添加购物车用例
# 注释tearDownClass内的退出浏览器操作
# 在套件执行之后 手动关闭浏览器驱动
DriverUtil.quit_driver()

# 单个调试测试用例时,浏览器驱动无法自动关闭
# 单个调试  工作目录 !=项目目录  需要自动退出浏览器驱动
# 套件执行  工作目录 == 项目目录   不需要自动退出浏览器驱动
# if 工作目录 !=项目目录 :
# DriverUtil.quit_driver()
