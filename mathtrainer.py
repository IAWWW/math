from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from time import sleep


class mathtrainer:
	def __init__(self):
		self.operation()
		return
	
	def operation(self):
		self.driver = webdriver.Chrome()																					#open Chrome
		self.driver.get("https://mathtrainer.org")																			#load mathtrainer.org
		sleep(2)
		self.driver.find_element_by_xpath('//div[@class="menu-btn"]').click()												#click menu
		sleep(2)
		#for span in self.driver.find_elements_by_xpath('//span[@class="setting-slider"]'):	
		#	check = self.driver.find_elements_by_xpath('//span[@class="setting-slider"]')
		#	check[2].click()																								#add multi, divi, soustra (pas besoin si login)
		#	check[3].click()
		#	check[4].click()
		#	sleep(3)
		self.driver.find_element_by_xpath('//div[@class="menu-option signin-btn"]').click()									#log in
		sleep(2)
		for span in self.driver.find_elements_by_xpath('//span[@class="firebaseui-idp-text firebaseui-idp-text-long"]'):
			email = self.driver.find_elements_by_xpath('//span[@class="firebaseui-idp-text firebaseui-idp-text-long"]')		#click on sign in email
			email[1].click()
			sleep(2)
			break
		sleep(2)
		self.driver.find_element_by_xpath('//input[@type="email"]').send_keys("xxxx@gmail.com")								#fill all info
		sleep(2)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(2)
		self.driver.find_element_by_xpath('//input[@type="password"]').send_keys("...")
		sleep(2)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(2)
		#self.driver.find_element_by_xpath('//div[@class="close-menu-btn"]').click()										#close menu (si pas log in)
		#break


		self.driver.find_element_by_xpath('//*[@id="start"]').click()														#click on Train
		sleep(5)
		while True:
			train = None 
			while not train:
				try:
					train = self.driver.find_element_by_xpath('//nav[@id="start"]')											#search end of calcul (search train)
					train.click()
					print("try")
				except NoSuchElementException:
					sleep(7)
					pass
				except ElementNotInteractableException:																		#if not train continue calcul
					sleep(0.3)																								#time calcul				
					a = self.driver.find_element_by_xpath('//div[@id="a"]').text											#find first number
					fa = int(a)						
					b = self.driver.find_element_by_xpath('//div[@id="b"]').text											#find second number
					fb = int(b)						
					op = self.driver.find_element_by_xpath('//section[@id="operator"]').text								#find operator
					result = 0						
					resultint = 0						
					if op == "+":						
						result = fa + fb						
						resultint = int(result)																				#put text in float then do operation
						print(fa, "+", fb, "=", resultint)						
					elif op == "−":						
						result = fa - fb						
						resultint = int(result)						
						print(fa, "-", fb, "=", resultint)						
					elif op == "×":						
						result = fa * fb						
						resultint = int(result)						
						print(fa, "×", fb, "=", resultint)						
					elif op == "÷":						
						result = fa / fb						
						resultint = int(result)						
						print(fa, "÷", fb, "=", resultint)						
					self.driver.find_element_by_xpath('//*[@id="input"]').send_keys(resultint)								#enter restult
					pass

mathtrainer()
