from selenium import webdriver

class AddEmp:
        DR=webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
        DR.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login")
        username=DR.find_element_by_id("txtUsername")
        username.send_keys("ankur")
        password=DR.find_element_by_id("txtPassword")
        password.send_keys("ankur")
        login.click()
	clickpimmenu=DR.find_element_by_id("menu_pim_viewPimModule")
	clickpimmenu.click()
	addbtn=DR.find_element_by_id("btnAdd")
	addbtn.click()
	firstname=DR.find_element_by_id("firstName")
	firstname.send_Keys("ankur_03")
	lastname=DR.find_element_by_id("lastName")
	lastname.send_Keys("kumar_03")
	savebtn=DR.find_element_by_id("btnSave")
	savebtn.click()
        