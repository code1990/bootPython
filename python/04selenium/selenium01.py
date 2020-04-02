from selenium import webdriver

# pip install selenium
# 一定要指明 executable_path='C:\driver\chromedriver.exe'
# 否则无法启动
driver = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')

driver.get('https://www.baidu.com')

print(driver.title)

driver.quit()
