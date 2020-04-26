import unittest

from util.TxtUtil import TxtUtil


class TxtUtilTest(unittest.TestCase):
    def test_read(self):
        txt_path = r'C:\Users\admin\Desktop\ebook\douban\python_catalog.txt'
        txt_path2 = r'C:\Users\admin\Desktop\tmp1.txt'

        listInfo = TxtUtil.readTxt(txt_path)
        TxtUtil.writeTxt(txt_path2,listInfo)
        for s in listInfo:
            print(s,end='')
        # print()
    # def test_read_txt(self):
    #     print()
    #     txt_path = r'C:\Users\admin\Desktop\new 10.txt'
    #     listInfo= TxtUtil.readTxt(txt_path)
    #     # file = open(txt_path,encoding='utf-8')
    #     # listInfo = file.readlines()
    #     print(len(listInfo))
    #     print(type(listInfo))
    #     txt_path2 = r'C:\Users\admin\Desktop\tmp.txt'
    #     file = open(txt_path2,'w', encoding='utf-8')
    #     for s in listInfo:
    #         if(len(s.strip())==0 or s.isspace() == True):
    #             continue
    #         if('地图"' in s or '微信分享' in s):
    #             print(s)
    #             continue
    #         if('      ' in s or '；' in s ):
    #             s= s.replace('      ','\n').replace('；','\n')
    #         file.writelines(s.strip())
    #         file.write("\n")
