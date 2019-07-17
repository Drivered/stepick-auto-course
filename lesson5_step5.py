from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x,z):
  return int(x) + int(z)
x_element = browser.find_element_by_id("num1")
z_element = browser.find_element_by_id("num2")
x = x_element.text
z = z_element.text
y = calc(x, z)
browser.find_element_by_tag_name("select").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(y)) # ищем элемент с текстом "Python"
# element = browser.find_element_by_css_selector("input[required]")
# element.send_keys(y)
# option1 = browser.find_element_by_css_selector("#robotCheckbox")
# option1.click()
# option2 = browser.find_element_by_css_selector("#robotsRule")
# option2.click()
buttons = browser.find_element_by_css_selector("button.btn.btn-default")
buttons.click()
