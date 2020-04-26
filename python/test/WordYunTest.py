# -*- coding:utf-8 -*-
import pkuseg
from collections import Counter
import pprint
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import imageio
# from scipy.misc import imread  # 这是一个处理图像的函数

#加载文件
content = []
with open("./fenci/yanjiang.txt", encoding="utf-8") as f:
    content = f.read()

seg = pkuseg.pkuseg(user_dict='my_dict.txt') # 加载模型，给定用户词典,比如'小程序','朋友圈','公众号'这些词
text = seg.cut(content)
#停用词
stopword_list = []
with open("./fenci/stopword.txt", encoding="utf-8") as f:
    stopword_list = f.read()
new_text = []
for w in text:
    if w not in stopword_list:
        new_text.append(w)
#统计频率
counter = Counter(new_text)
#换行打印
pprint.pprint(counter.most_common(40))

word_list = {}
for i in counter.most_common(20):
    word_list[i[0]] = int(i[1]) # list变dict

#加载背景图片
cloud_mask = np.array(Image.open("./fenci/milaoshu.png"))
back_color = imageio.imread("./fenci/milaoshu.png")  # 解析该图片

#生成wordcloud对象
wc = WordCloud(background_color='black',  # 背景颜色
               max_words=2000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               collocations=False,
               #max_font_size=100,  # 字体最大值
               #min_font_size=20,  # 字体最小值
               font_path="./fenci/MSYH.TTC",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               # random_state=42,  # 为每个词返回一个PIL颜色
               )
print(word_list)
wc.generate_from_frequencies(word_list) #使用频率绘制云图
#基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
#plt.imshow(wc)
# 关闭坐标轴
#plt.axis('off')
# 绘制词云
plt.figure()
# plt.imshow(wc, interpolation="bilinear")
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
plt.show()
# 保存图片
wc.to_file('wordcloud2.png')