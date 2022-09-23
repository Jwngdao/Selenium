# tests/lt_sample_todo.py
from selenium import webdriver
import pytest_check as check
import time
import getpass
import pytest
import sys
import os
from weasyprint import HTML
 
driver=webdriver.Firefox()
#@pytest.mark.fixtures('driver')

#locust -f testlo.py --headless --users 50 --spawn-rate 2 -H http://localhost:5000



driver.get('https://bmsuat.trsc.nic.in/bms/')

#driver.find_element_by_id("login-button").click()

def test_current_url_of_Home_Page():

	
	#os.system("locust -f testlo.py --headless --users 50 --spawn-rate 2 --run-time 100 --html=LoadTestReport.html")
	#check if current url is okay
	current_url = driver.current_url	
	check.is_in("https://bmsuat.trsc.nic.in/bms/", current_url)
	print("Checking current url of Home Page Done")


	#Click on Dashboard
	#driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[4]/a").click()
	#driver.switch_to.window(driver.window_handles[1])
	#driver.refresh()

	#check.is_in("https://bmsuat.trsc.nic.in/dashboard/home.jsp", driver.current_url)
	

	#Back to login page
	#driver.switch_to.window(driver.window_handles[0])
	#driver.refresh()

def test_citizen_login_button():

	#click in citizen login
	
	#driver.find_element_by_class_name("btn-success btn-lg btn-block").click()
	driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/a[1]").click()

	#current_url = driver.current_url	
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/login.jsp", driver.current_url)

	print("Citizen Login button test Done")
def test_null_login_value():
	#null value and click login
	driver.find_element_by_id("user_email").send_keys("")
	driver.find_element_by_id("btnForget").click()
	alert=driver.find_element_by_id("user_email-error").text
	check.equal(alert,"This field is required.")
	print("Null Login value Test Done")

	#new registration
def test_registration_link():
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[2]/form/a").click()
	driver.switch_to.window(driver.window_handles[1])
	driver.refresh()
 
	#driver.getCurrentUrl();
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/User/citizeRegistration.jsp", driver.current_url)
	print("Registration link Test Done")

def test_Null_value_registation():
	#enter null value and click next
	driver.find_element_by_id("btnForget").click()
	alert=driver.find_element_by_id("name-error").text
	check.equal(alert,"This field is required.")
	print("Null Value Registration Test Done")
def test_Valid_registration():
	#enter valid details
	driver.find_element_by_id("name").send_keys("selenium")
	driver.find_element_by_id("user_email").send_keys("jwd2.monitor@gmail.com")
	driver.find_element_by_id("user_mobile").send_keys("0000000000")
	driver.find_element_by_id("btnForget").click()
	alert=driver.find_element_by_id("error").text
	check.equal(alert,"Already Registered. Please Login")
	print("Valid Registration Test Done")

def test_Already_registered_login_button():
	#already registered-click login
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/form/div[2]/a").click()
	driver.switch_to.window(driver.window_handles[2])
	driver.refresh()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/login.jsp", driver.current_url)
	print("Already Registered Login Button Test Done")

def test_valid_login():
	
	
	#valid login
	driver.find_element_by_id("user_email").send_keys("jwd2.monitor@gmail.com")
	driver.find_element_by_id("btnForget").click()
	print("Valid login Test Done")
	
	#NUll OTP
	#driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/form/div[5]/button").click()
	#alert=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/form/div[3]/div/label")
	#check.equal(alert,"This field is required.")
	#alert=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/form/div[4]/div/label")
	#check.equal(alert,"This field is required.")
	

	#resent otp 

	#time.sleep(70)
	#driver.find_element_by_id("Resendotp").click()
	#validOTP
def test_otp_validation():

	#OTP = getpass.getpass("Press Enter after entering OTP:")
	OTP="123456"
	time.sleep(5)
	#driver.find_element_by_id("txtemailotp").send_keys(OTP)
	driver.find_element_by_id("txtmobileotp").send_keys(OTP)
	driver.find_element_by_id("btnForgetotp").click()
	time.sleep(10)
	#check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/schemeList.jsp",driver.current_url)

	print("OTP Validation Done")
	
def test_Homepage_url():
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/schemeList.jsp",driver.current_url)
	driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[1]/a").click()
	time.sleep(10)
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/User/userHome.jsp",driver.current_url)
	driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[2]/a").click()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/schemeList.jsp",driver.current_url)
	print("Homepage URL test Done")

def test_Dashboard_Button():
	driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[1]/a").click()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/User/userHome.jsp",driver.current_url)
	print("Dashboard Button Test Done")

def test_Profile_Button():
	driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[3]/a").click()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/User/CitizenProfile.jsp",driver.current_url)
	print("Profile Button Test Done")

def test_Apply_Online_Button():
	driver.find_element_by_xpath("/html/body/div/nav/div/ul/li[2]/a").click()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/schemeList.jsp",driver.current_url)
	print("Apply Online Button Test Done")

def test_search_button():
	#search button
	driver.find_element_by_xpath("/html/body/div/div[2]/fieldset/div/div/div[1]/div[2]/div/label/input").send_keys("Education(Elementary Education)")

	time.sleep(10)
	alert=driver.find_element_by_xpath("/html/body/div/div[2]/fieldset/div/div/div[2]/div/table/tbody/tr/td[1]").text
	
	check.equal(alert,"Education(Elementary Education)")

	driver.find_element_by_xpath("/html/body/div/div[2]/fieldset/div/div/div[2]/div/table/tbody/tr/td[4]/a").click()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/viewanddownload.jsp?data=945",driver.current_url)
	print("Search button Test Done")

def test_proceed_button():
	#proceed button
	driver.find_element_by_xpath("/html/body/div/div[2]/fieldset/a").click()
	driver.switch_to.window(driver.window_handles[3])
	driver.refresh()
	check.is_in("https://bmsuat.trsc.nic.in/bmscitizenportal/Schemes/scheme_enrollment.jsp?data=54",driver.current_url)
	print("Proceed Button Test Done")

def test_form_not_domicile():
	try:
		driver.find_elements_by_xpath("/html/body/div[3]/div/div[4]/div/button").click()
		#click NO
		#driver.find_element_by_id("domicile_of_tripura1").click()
		#driver.find_element_by_id("domicile_of_tripura2").click()
		#name
		#driver.find_element_by_id("name").send_keys("Selenium")
		#FATHERNAME
		driver.find_elements_by_id("guardian_name").send_keys("Python")
		#MOTHERNAME
		driver.find_elements_by_id("mother_name").send_keys("Automation")
		#GENDER
		driver.find_elements_by_id("gender").click()
		#Select Please Select
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[2]/div[2]/select/option[1]").click()
		#Select Female
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[2]/div[2]/select/option[3]").click()
		#select transgender
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[2]/div[2]/select/option[4]").click()
		#select male
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[2]/div[2]/select/option[2]").click()
	
		#SOCIAL CATEGORY
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[1]/div[2]/div[3]/div[1]/select").click()
	
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[3]/div[1]/select/option[1]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[3]/div[1]/select/option[2]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[3]/div[1]/select/option[3]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[3]/div[1]/select/option[4]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[1]/div[2]/div[3]/div[1]/select/option[5]").click()

		#DOB#########################################################################################
		driver.find_elements_by_id("dob").click()
	



		#ADDRESS
		#SUBDIVISIONS
		#DISTRICTwith3SUBDIVISIONS 
		def sub3divisions():
			#SELECT SUBDIVSION
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[1]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[2]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[3]").click()
		#DISTRICTwith4SUBDIVISIONS
		def sub4divisions():
			#SELECT SUBDIVSION
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[1]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[2]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[3]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[4]").click()
		#DISTRICTwith5SUBDIVISIONS
		def sub5divisions():
			#SELECT SUBDIVSION
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[1]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[2]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[3]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[4]").click()
			driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[2]/select/option[5]").click()


		
		


		#SELECT DISTRICT
		#PLEASE SELECT
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[1]").click()
		#SELECT DHALAI
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[2]").click()

		#SELECT SUBDIVSION
		sub5divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[3]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		
		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[3]").click()
		#SELECT SUBDIVSION
		sub4divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[2]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		
		
		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[4]").click()
		#SELECT SUBDIVSION
		sub3divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[3]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		

		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[5]").click()
		#SELECT SUBDIVSION
		sub4divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[2]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		

		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[6]").click()
		#SELECT SUBDIVSION
		sub4divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[3]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		


		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[7]").click()
		#SELECT SUBDIVSION
		sub4divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[2]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[8]").click()
		#SELECT SUBDIVSION
		sub3divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[2]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		

		
		
		#Select next district
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[1]/div[1]/select/option[9]").click()
		#SELECT SUBDIVSION
		sub4divisions()
		#SELECT MC/Block/ADC Block 
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[1]/select/option[3]").click()
		#SELECT Ward/GP/VC :
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[9]").click()
		driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/form[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[11]").click()
		


		#PINCODE
		driver.find_elements_by_id("pincode").send_keys(799001)
		
		driver.find_elements_by_id("Save_profile").click()
		
		#os.system("locust -f testlo.py --headless --users 50 --spawn-rate 2 --html=report.html")

		print("Form Test Done")
	

	except:

		return False

	driver.find_element_by_id("bank_ac_no").send_keys(12345678910)
	driver.find_element_by_id("sameempcode2").click()

	print("Form Test Done")
	

#def test_load():
	#os.system("locust -f testlo.py --headless --users 50 --spawn-rate 2 --run-time 20 --html=LoadTestReport.html")


	#time.sleep(10)
	
	
	

	#Account Number	
	#driver.find_element_by_id("bank_ac_no").send_keys(12345678910)
		#Account holder name, click same as name
		#driver.find_element_by_id("sameempcode2").click()
	#Select bank	
	#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[3]/div[2]/div[2]/div[1]/select/option[2]").click()
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[3]/div[2]/div[2]/div[1]/select/option[5]").click()
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[3]/div[2]/div[2]/div[1]/select/option[8]").click()
		
		#IFSC CODE
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("SBIN0003348")

		#Select Office
		#driver.find_element_by_id("select2-office_name_list-container").click()

		#select photo
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[4]/div[2]/div[1]/div[3]/input").send_keys("/home/zwngdao/Selenium/pytest4/helloworld.jpg")
		 

		#select photo
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[4]/div[2]/div[1]/div[3]/input").send_keys("/home/zwngdao/Selenium/pytest4/helloworld.jpg")
		
		#select photo
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[2]/input").send_keys("/home/zwngdao/Selenium/pytest4/apache airflow.pdf")
		#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/fieldset[1]/div/form[2]/div[4]/div[2]/div[3]/div/div/div[2]/div[2]/input").send_keys("/home/zwngdao/Selenium/pytest4/apache airflow.pdf")


	
	
			

	
	


		

	
	
	
	
	

	
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	
	
	
	
	
	
	
	
	
	
