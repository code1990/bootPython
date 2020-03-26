**1.命令行安装方法**
pip install pywinauto

pyWin32: python调用windows api的库

Pillow：可选，用来做屏幕截图的

Pywinauto：PC端自动化工具

二、PC端元素定位工具介绍及判断backend
1.Backend判断
Pywinauto中backend有两种：win32和uia，默认为win32。可使用spy++和Inspect工具判断backend适合写哪种。例如：如果使用Inspect的UIA模式，可见的控件和属性更多的话，backend可选uia，反之，backend可选win32。

三、启动并创建一个实例对象
1.启动
start()用于还没有启动软件的情况。timeout为超时参数（可选），若软件启动所需的时间较长可选timeout，默认超时时间为5s。
start(self, cmd_line, timeout=app_start_timeout)
示例：
app = Application(backend = ‘uia’).start(r"E:\Office\Office14\EXCEL.exe)

2.连接
connect()用于连接已经启动的程序。连接一个已经运行的程序有以下几种方法：
a)process：进程id
app = Application().connect(process=2341)
b)handle：应用程序的窗口句柄
app = Application().connect(handle=0x010f0c)
c)path：进程的执行路径（GetModuleFileNameEx 模块会查找进程的每一个路径并与我们传入的路径去做比较）
app = Application().connect(path=“D:\Office14\EXCEL.exe”)

d)参数组合（传递给pywinauto.findwindows.find_elements()这个函数）
app = Application().connect(title_re=".*Notepad", class_name=“Notepad”)

注：
应用程序必须先准备就绪，才能使用connect()，当应用程序start()后没有超时和重连的机制。在pywinauto外再启动应用程序，需要sleep，等程序start

四、 窗口、对话框及控件元素定位方式
1.window，dialog定位方式
1)基于title定位
a)如何获取title？
title为窗口的名称，可使用UISpy一类的定位元素工具去查找。
如图所示，该对话框中的title为Name属性值：“替换”

b)若使用定位元素工具找不到title怎么办？
使用print_control_identifiers()方法打印出当前窗口或对话框中的所有title
格式：
app.YourDialog. print_control_identifiers()

示例如图，demo详见locate_by_title.py：

c)使用title定位方式的写法
Untitled_notepad = u’无标题 – 记事本’
app. Untitled_notepad.draw_outline(colour = ‘red’) #app.window(best_match=‘Untitled - Notepad’)
注：这种写法适用于英文系统，英文软件,其他语言的系统会存在编码问题，需转码再使用。
或
app[‘无标题 – 记事本’] .draw_outline(colour = ‘red’)
注：适用于除英文外其他语言的系统,不用转码

2)top_window()定位
app.top_window() #此方法可返回应用软件的最顶层窗口（是窗口，不是窗口弹出的对话框）
注：此方法目前没有经过测试，它会返回应用程序的顶级窗口，但可能不是Z-Order中的顶级窗口。

3)关键字传参
若以上方法不能满足定位元素的需求，可使用以下列表中的参数传参定位元素，参数可以组合使用。
示例：
app.window(class_name = ‘Notepad’).draw_outline(colour = ‘red’)

2． control定位方式

基于title定位（同window，dialog中的title定位）
app[‘your dialog title’][‘your control title’]
或
app.dlg.control

层级定位
app.window(class_name = ’Notepad’).window(class_name = ‘#32770’)
app.window(class_name = ‘Notepad’).child_window(class_name = ‘#32770’)

wpath定位
若元素值为空，或不是唯一的情况下，可使用类似selenium中xpath的定位方式，根据查子元素的序号去定位元素。
示例：
app_window = app.window(class_name=‘Qt5QWindowIcon’) #定位登录窗口
app_window.children()[1].children()[0].children()[0] .children()[2] #定位用户名输入框控件（序号从0开始查）

五、常用方法

1**.调试定位控件**
a)print_control_identifiers(depth = None, filename = None)
以树形结构打印出所有控件可识别出的标识
depth:打印的深度，缺省时打印最大深度。
filename:将返回的标识存成文件（生成的文件与当前运行的脚本在同一个路径下）
eg：dlg. print_control_identifiers(filename =’a.txt’)

b)draw_outline(colour =’green’,thickness = 2,
fill = win32defines.BS_NULL, rect = None)
默认为在当前定位到的窗口或控件周围画出一条边界线，方便我们看出定位到了哪个控件
colour:边界线的颜色，默认为绿
thickness：线的粗细，默认为2
fill：以何种方式填充矩形（没试过，详见源码base_wrapper.py）
rect:根据坐标画出矩形（默认是在当前定位到的元素上画出一个矩形）
c) is_dialog 判断是否为dialog

2. 隐式等待
a) wait(wait_for, timeout = None, retry_interval = None)
wait_for可传入五种参数, 可以组合传参，但要以空格隔开：
exists: 窗口变成有效的句柄
visible: 窗口可见，没有隐藏
enabled: 窗口没有disable
ready: visible + enable
active: active
timeout:设置超时时间，若在n秒内没有等到窗口在wait_for中传入的几种状态，则会抛出TimeoutError。
retry_interval:超时后，间隔n秒再次重试。
Dlg.wait(“exists ready”, timeout = 5, retry_interval = 3)

b) wait_not(wait_for_not,timeout = None，retry_interval = None)
等待窗口不处于某种状态时。参数与wait传参一致。

3. 输入框输入
a)type_keys()
Dlg.control.type_keys(“xxxxx”)
4. 菜单栏
menu_select()
eg：app.window.menu_select(Edit -> Replace)
5. 鼠标点击
a)click() 点击Button控件
b)check_by_click() 通过click()方法勾选checkbox
c)uncheck_by_click() 通过click()方法取消勾选checkbox
d)get_check_state() 返回checkbox的勾选状态（0没勾选，1勾选，2不定）
e)is_checked(勾选返回true，为勾选返回false，不定返回None)
f)check() 勾选checkbox
g)uncheck() 不勾选checkbox
h)invoke() 点击(uia mode)
i)toggle () 勾选checkbox(uia mode)
6. 键盘操作
“+”：Shift
“^”：Control
“%”：Alt

https://www.cnblogs.com/wuxunyan/p/9366178.html