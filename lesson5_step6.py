from selenium import webdriver

# browser = webdriver.Chrome()
# link = "https://suninjuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
import time
from math import log, sin

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()
window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

def calc(x):
  return str(log(abs(12*sin(x))))
element = browser.find_element_by_css_selector("#input_value")
z = element.text
y = calc(int(z))
option1 = browser.find_element_by_css_selector("#answer")
option1.send_keys(y)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# option1 = browser.find_element_by_css_selector("#robotCheckbox")
# option1.click()
# option2 = browser.find_element_by_css_selector("#robotsRule")
# option2.click()
buttons = browser.find_element_by_css_selector("button.btn.btn-primary")
buttons.click()
