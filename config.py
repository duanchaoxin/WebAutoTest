import os
# 获取到  config.py文件的 目录 --> 整个项目目录
# config.py文件的绝对路径
# print(os.path.abspath(__file__))
# config.py文件的绝对路径目录部分 -> 项目目录
# print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_HOST = "http://localhost/"