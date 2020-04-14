# 创建一个类用于保存 / 获取/ 销毁 浏览器驱动对象
import json
import time
import logging
from logging.handlers import TimedRotatingFileHandler

import os
from selenium import webdriver

# 浏览器 保存 获取  销毁
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_DIR


class DriverUtil:
    # 保存
    driver = None

    # 获取
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    # 销毁
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def switch_window(cls):
        # 封装切换新窗口方法
        cls.get_driver().switch_to.window(cls.get_driver().window_handles[-1])

    @classmethod
    def switch_page(cls):
        # 封装切换子页方法
        cls.get_driver().switch_to.frame(cls.get_driver().find_element_by_tag_name("iframe"))

    @classmethod
    def close_alert(cls):
        cls.get_driver().switch_to.alert.dismiss()


# 用例驱动退出方法
def case_driver_quit():
    if BASE_DIR != os.getcwd():
        DriverUtil.quit_driver()


# 用于封装日志器工具
class LogUtil:
    # 保存日志器
    logger = None

    # 获取日志器
    @classmethod
    def get_logger(cls):
        # 如果当前日志器是空, 无法返回
        # 先创建设置好日志器, 保存在logger属性中
        # 最后在返回
        if cls.logger is None:
            # 1.创建日志器 导入logging
            cls.logger = logging.getLogger("logger")
            cls.logger.setLevel(logging.INFO)

            # 2.获取处理器 -- 控制台处理 - 时间分割文件
            shl = logging.StreamHandler()
            trfl = TimedRotatingFileHandler(filename=BASE_DIR + "/log/log.log",  # 日志保存的位置要统一到项目log目录下
                                            when="midnight",
                                            interval=1,
                                            backupCount=0,
                                            encoding="utf-8"
                                            )
            # 3.获取格式器
            fmter = logging.Formatter(
                fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

            # 4.处理器设置格式器
            shl.setFormatter(fmter)
            trfl.setFormatter(fmter)

            # 5.日志器添加处理器
            cls.logger.addHandler(shl)
            cls.logger.addHandler(trfl)

        return cls.logger


# 判断页面是否存在指定的文本内容
def text_exists(text):
    try:
        # 定位成功返回真 -- 存在指定文本
        # 你不知道文本什么时候出现 , 也不知道文本会存在多久  -- 有等待 -- 显式等待
        WebDriverWait(DriverUtil.get_driver(), 5, 0.3).until(
            lambda x: x.find_element_by_xpath('//*[contains(text(),"{}")]'.format(text)))
        # DriverUtil.get_driver().find_element_by_xpath('//*[contains(text(),"{}")]'.format(text))
        return True
    except:
        # 定位失败(抛出异常)返回假 -- 不存在指定文本
        return False


# 读取json文件的方法
def load_json(file_name):
    with open(BASE_DIR + "/data/{}".format(file_name), "r", encoding="utf-8") as f:
        python_data = json.load(f)
        return python_data


# 调整报告保存位置

# 调整日志保存位置

# 截图用例截图方法
def jietu():
    filename = BASE_DIR + "/screenshot/screenshot{}.png".format(time.strftime("%Y%m%d%H%M%S"))
    DriverUtil.get_driver().get_screenshot_as_file(filename)


if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()
    driver.get("http://www.baidu.com")

    logger = LogUtil.get_logger()
    logger.info("woderizhitest")

    time.sleep(3)
    # 关闭浏览器 -- 一定要使用驱动工具的退出方法
    DriverUtil.quit_driver()
