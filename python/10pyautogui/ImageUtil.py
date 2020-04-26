# pic_3 = auto.screenshot("my_screenshot.png ",region=(0,0, 300, 400))
# pyautogui 可以传递区域的左、顶、宽和高的四个整数元组来捕获图片

# 安装aip  pip install baidu-aip
from aip import AipOcr

# APP_ID API_KEY SECRET_KEY，
APP_ID = '16393850'
API_KEY = 'grU7EKi9Zfp1K4GjPxh9MdOb'
SECRET_KEY = 'fW7ZkXsKG6gVPdGoBWxz2QlmArSHFAZF'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
i = open(r'my_screenshot.png','rb')
img = i.read()
message = client.basicGeneral(img)
for i in message.get('words_result'):
    print(i.get('words'))
