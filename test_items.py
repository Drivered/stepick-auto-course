import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
	browser.get(link)
	time.sleep(10)
	options1 = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
	assert options1, "Button not in file"