# Chrome headless 模式
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe', chrome_options=chrome_options)
driver.get("https://www.baidu.com")

print(driver.title)

driver.quit()

# Selenium的发展史

# Selenium是开源自动化工具，是化学元素硒，硒可以对抗汞。

# Selenium IDE
#
# Selenium IDE是嵌入到Firefox浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能。
#
# Selenium Grid
#
# Selenium Grid是一种自动化的测试辅助工具，Grid通过利用现有的计算机基础设施，能加快Web-App的功能测试。利用Grid可以很方便地实现在多台机器上和异构环境中运行测试用例。
#
# Selenium RC
#
# Selenium RC（Remote Control）是Selenium家族的核心部分。Selenium RC 支持多种不同语言编写的自动化测试脚本，通过Selenium RC的服务器作为代理服务器去访问应用，从而达到测试的目的。

# Selenium 2.0
# 因为Selenium和Webdriver的合并，所以，Selenium 2.0由此诞生。简单用公式表示为：

