from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

# pip install selenium
# 一定要指明 executable_path='C:\driver\chromedriver.exe'
# 否则无法启动
chrome_options = Options()
# chrome_options.add_argument('--headless')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe', options=chrome_options)
driver = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
index_url = r'http://www.javazx.com/portal.php'
driver.get(index_url)
driver.maximize_window()
pyautogui.moveTo(982, 312)
pyautogui.click()
pyautogui.typewrite(message='s13322177151', interval=0.5)
pyautogui.moveTo(982, 342)
pyautogui.click()
pyautogui.typewrite(message='My1332177151', interval=0.5)
pyautogui.moveTo(1169, 338)
pyautogui.click()
# 停下3分钟 手动验证
time.sleep(3*60)
# print(driver.title)

# driver.quit()
