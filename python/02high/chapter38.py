# Python GUI编程(Tkinter)
# Python 提供了多个图形开发界面的库，几个常用 Python GUI 库如下：
#
# Tkinter： Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .
#
# wxPython：wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，
#
# Jython：Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。

# Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。

import tkinter

top = tkinter.Tk()
top.mainloop()

from tkinter import *

root = Tk()

li = ["java", "python"]
movie = ["hadoop", "storm"]
listb = Listbox(root)
listb2 = Listbox(root)

for item in li:
    listb.insert(0, item)

for item in li:
    listb2.insert(0, item)

listb.pack()
listb2.pack()
root.mainloop()

# Tkinter 组件
# Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。
#
# 目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:
#
# 控件	描述
# Button	按钮控件；在程序中显示按钮。
# Canvas	画布控件；显示图形元素如线条或文本
# Checkbutton	多选框控件；用于在程序中提供多项选择框
# Entry	输入控件；用于显示简单的文本内容
# Frame	框架控件；在屏幕上显示一个矩形区域，多用来作为容器
# Label	标签控件；可以显示文本和位图
# Listbox	列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
# Menubutton	菜单按钮控件，用于显示菜单项。
# Menu	菜单控件；显示菜单栏,下拉菜单和弹出菜单
# Message	消息控件；用来显示多行文本，与label比较类似
# Radiobutton	单选按钮控件；显示一个单选的按钮状态
# Scale	范围控件；显示一个数值刻度，为输出限定范围的数字区间
# Scrollbar	滚动条控件，当内容超过可视化区域时使用，如列表框。.
# Text	文本控件；用于显示多行文本
# Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似
# Spinbox	输入控件；与Entry类似，但是可以指定输入范围值
# PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
# LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
# tkMessageBox	用于显示你应用程序的消息框。
# 标准属性
# 标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。
#
# 属性	描述
# Dimension	控件大小；
# Color	控件颜色；
# Font	控件字体；
# Anchor	锚点；
# Relief	控件样式；
# Bitmap	位图；
# Cursor	光标；
# 几何管理
# Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置
#
# 几何方法	描述
# pack()	包装；
# grid()	网格；
# place()	位置；
