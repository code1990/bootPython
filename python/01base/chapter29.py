from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')

driver.get('https://www.runoob.com/python/python-100-examples.html')

content = driver.find_element_by_id("content")

links = content.find_elements_by_tag_name("a")
print(type(links))
print(len(links))
for i in range(50,len(links)):
    links[i].click()

# print(driver.title)

# driver.quit()
