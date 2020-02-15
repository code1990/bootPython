from selenium import webdriver
import time
file = open("C:\\Users\\Administrator\\Desktop\\122.txt","r+")
for line in file.readlines():
    driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
    driver.get(line)
    print(line,end="")
    time.sleep(2)
# while file.r
#
#
#
#
# content = driver.find_element_by_id("content")
#
# links = content.find_elements_by_tag_name("a")
# print(type(links))
# print(len(links))
# for link in links:
#     print(link.get_attribute("href"))
#     # link.click()
#
# # print(driver.title)
#
# driver.quit()
