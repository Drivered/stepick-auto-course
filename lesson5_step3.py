from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/huge_form.html")
# elements = browser.find_elements_by_tag_name("input")
# for element in elements:
    # element.send_keys("Мой ответ")

# button = browser.find_element_by_css_selector("button.btn")
# button.click()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
buttons1 = browser.find_element_by_id("book")
buttons1.click()

def calc(x):
  return str(log(abs(12*sin(x))))
element = browser.find_element_by_css_selector("#input_value")
z = element.text
y = calc(int(z))
option1 = browser.find_element_by_css_selector("#answer")
option1.send_keys(y)
# input2 = browser.find_element_by_name("firstname")
# input2.send_keys("Petrov")
# input4 = browser.find_element_by_name("lastname")
# input4.send_keys("Ivan")
# input3 = browser.find_element_by_name("email")
# input3.send_keys("Pochta")
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element = browser.find_element_by_id("file")
# element.send_keys(file_path)
buttons = browser.find_element_by_id("solve")
buttons.click()