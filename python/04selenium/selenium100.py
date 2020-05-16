from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()                                         # 网上找到 你可以试试
options.binary_location = r"F:\soft\chrome-win32\chrome.exe"   # 这里是你指定浏览器的路径
driver = webdriver.Chrome(chrome_options=options,executable_path='C:\\driver\\chromedriver68.exe')
# pip install selenium
# 一定要指明 executable_path='C:\driver\chromedriver.exe'
# 否则无法启动
# driver = webdriver.Chrome()

# driver.get('https://duckduckgo.com/?q=bolts+canada&ia=web')
driver.get('http://www.baidu.com')

print(driver.title)

driver.quit()
