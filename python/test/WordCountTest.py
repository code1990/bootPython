import unittest
import pkuseg
class WordCountTest(unittest.TestCase):
    print("111")
    def test_one(self):
        print(1)
        seg = pkuseg.pkuseg()  # 以默认配置加载模型
        text = seg.cut('我爱北京天安门')  # 进行分词
        print(text)

