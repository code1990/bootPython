# （十一）多表单切换
# 遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。
# 这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.get("http://www.126.com")

# switch_to.frame() 默认可以直接取表单的id 或name属性
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
# 通过switch_to.default_content()跳回最外层的页面
driver.switch_to.default_content()

driver.quit()
