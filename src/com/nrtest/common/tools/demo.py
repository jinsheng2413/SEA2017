import os
import time
from io import BytesIO

import numpy as np
import requests
from PIL import Image
from past.builtins import raw_input

from com.nrtest.common.setting import Setting

# 获取验证码的网址

CAPT_URL = "http://192.168.176.10:8001/sea2019/validateNumber.action?nocache=1555466819077"
# 验证码的保存路径
CAPT_PATH = Setting.SCREENSHOTS_PATH
if not os.path.exists(CAPT_PATH):
    os.mkdir(CAPT_PATH)
# 将验证码转为灰度图时用到的"lookup table"
THRESHOLD = 165
LUT = [0] * THRESHOLD + [1] * (256 - THRESHOLD)


def capt_fetch():
    """
    从网站获取验证码，将验证码转为Image对象

    :require requests: import requests
    :require time: import time
    :require BytesIO: from io import BytesIO
    :require Image: from PIL import Image

    :param:
    :return capt: 一个Image对象
    """
    # 从网站获取验证码
    capt_raw = requests.get(CAPT_URL)
    # 将二进制的验证码图片写入IO流
    f = BytesIO(capt_raw.content)
    # 将验证码转换为Image对象
    capt = Image.open(f)
    return capt


def capt_download():
    """
    将Image类型的验证码对象保存到本地

    :require Image: from PIL import Image
    :require os: import os

    :require capt_fetch(): 从nbsc网站获取验证码
    :require CAPT_PATH: 验证码保存路径

    :param:
    :return:
    """
    capt = capt_fetch()
    capt.show()
    text = raw_input("请输入验证码中的字符：")
    suffix = str(int(time.time() * 1e3))
    capt.save(CAPT_PATH + text + "_" + suffix + ".jpg")


def capt_process(capt):
    """
    图像预处理：将验证码图片转为二值型图片，按字符切割

    :require Image: from PIL import Image
    :require LUT: A lookup table, 包含256个值

    :param capt: 验证码Image对象
    :return capt_per_char_list: 一个数组包含四个元素，每个元素是一张包含单个字符的二值型图片
    """
    capt_gray = capt.convert("L")
    capt_bw = capt_gray.point(LUT, "1")
    capt_per_char_list = []
    for i in range(4):
        x = 5 + i * 15
        y = 2
        capt_per_char = capt_bw.crop((x, y, x + 15, y + 18))
        capt_per_char_list.append(capt_per_char)
    return capt_per_char_list


def capt_inference(capt_per_char):
    """
    提取图像特征

    :require numpy: import numpy as np

    :param capt_per_char: 由单个字符组成的二值型图片
    :return char_features:一个数组，包含 capt_per_char中字符的特征
    """
    char_array = np.array(capt_per_char)
    total_pixels = np.sum(char_array)
    cols_pixels = np.sum(char_array, 0)
    rows_pixels = np.sum(char_array, 1)
    char_features = np.append(cols_pixels, rows_pixels)
    char_features = np.append(total_pixels, char_features)
    return char_features.tolist()


#
# def train():
#     """
#     将预分类的验证码图片集转化为字符特征训练集
#
#     :require Image: from PIL import Image
#     :require os: import os
#
#     :require capt_process(): 图像预处理
#     :require capt_inference(): 提取图像特征
#
#     :param:
#     :return train_table: 验证码字符特征训练集
#     :return train_labels: 验证码字符预分类结果
#     """
#     files = os.listdir(CAPT_PATH)
#     train_table = []
#     train_labels = []
#     for f in files:
#         if f.endswith('.jpg') and f[0] != '_':
#             train_labels += list(f.split("_")[0])
#             capt = Image.open(CAPT_PATH + f)
#             capt_per_char_list = capt_process(capt)
#             for capt_per_char in capt_per_char_list:
#                 char_features = capt_inference(capt_per_char)
#                 train_table.append(char_features)
#     return train_table, train_labels


def nnc(train_table, test_vec, train_labels):
    """
    Nearest Neighbour Classification（近邻分类法），
    根据已知特征矩阵的分类情况，预测未分类的特征向量所属类别

    :require numpy: import numpy as np

    :param train_table: 预分类的特征矩阵
    :param test_vec: 特征向量， 长度必须与矩阵的列数相等
    :param labels: 特征矩阵的类别向量
    :return : 预测特征向量所属的类别
    """
    dist_mat = np.square(np.subtract(train_table, test_vec))
    dist_vec = np.sum(dist_mat, axis=1)
    pos = np.argmin(dist_vec)
    return train_labels[pos]


def test():
    """
    测试模型分类效果

    :require Image: from PIL import Image

    :require capt_fetch(): 从nbsc网站获取验证码
    :require capt_process(): 图像预处理
    :require capt_inference(): 提取图像特征
    :train_table, train_labels: train_table, train_labels = train()

    :param:
    :return capt: 验证码图片
    :return test_labels: 验证码识别结果
    """
    test_labels = []
    capt = capt_fetch()
    capt_per_char_list = capt_process(capt)
    for capt_per_char in capt_per_char_list:
        char_features = capt_inference(capt_per_char)
        label = nnc(train_table, char_features, train_labels)
        test_labels.append(label)
    test_labels = "".join(test_labels)
    return capt, test_labels


def train():
    """
    将预分类的验证码图片集转化为字符特征训练集

    :require Image: from PIL import Image
    :require os: import os

    :require capt_process(): 图像预处理
    :require capt_inference(): 提取图像特征

    :param:
    :return train_table: 验证码字符特征训练集
    :return train_labels: 验证码字符预分类结果
    """
    files = os.listdir(CAPT_PATH)
    train_table = []
    train_labels = []
    for file in files:
        if file.endswith('.jpg') and file[0] != '_':
            train_labels += list(file.split("_")[0])
            capt = Image.open(CAPT_PATH + file)
            capt_per_char_list = capt_process(capt)
            for capt_per_char in capt_per_char_list:
                char_features = capt_inference(capt_per_char)
                train_table.append(char_features)
    return train_table, train_labels


if __name__ == '__main__':
    # 下载120张图片到本地
    # for i in range(120):
    #     capt_download()

    # 模型的训练与测试
    train_table, train_labels = train()
    for i in range(10):
        test_capt, test_labels = test()
        suffix = str(int(time.time() * 1e3))
        test_capt.save(CAPT_PATH + '_' + test_labels + "_" + suffix + ".jpg")

    # baseTest = BaseTest()
    # driver = baseTest.openBrowser(Setting.BROWSER)
    # driver.maximize_window()
    # driver.get(Setting.TEST_URL)
    # time.sleep(2)
    #
    # loginPage = LoginPage(driver)
    # loginPage.waitFor()
    # time.sleep(3)
    # train_table, train_labels = train()
    # test_capt, test_labels = test()
    # loginPage.input_identifying(test_labels)
