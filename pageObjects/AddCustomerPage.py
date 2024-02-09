# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
# class AddCustomerClass:
#     Click_Customer_menu_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
#     Click_Customer_submenu_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
#     Click_AddNewCustomer_Xpath = "//i[@class='fas fa-plus-square']"
#     Text_Email_Xpath = "//input[@id='Email']"
#     Text_Password_Xpath = "//input[@id='Password']"
#     Text_FirstName_Xpath = "//input[@id='FirstName']"
#     Text_LastName_Xpath = "//input[@id='LastName']"
#     Radio_Male_Xpath = "//input[@id='Gender_Male']"
#     Radio_Female_Xpath = "//input[@id='Gender_Female']"
#     Calender_Xpath = "//input[@id='DateOfBirth']"
#     Text_Company_Name_Xpath = "//input[@id='Company']"
#     CheckBox_Tax_Xpath = "//input[@id='IsTaxExempt']"          #this is my xpath  #sir has given same xpath as company name
#     Click_Newsletter_Xpath = "//div[@class='input-group-append']//div[@role='listbox']"
#     Click_Newsletter_list_Xpath = "/html[1]/body[1]/div[5]/div[1]/div[2]/ul[1]/li[1]"
#     # DropDown_CustomerRoles_Xpath = "//li[normalize-space()='Administrators']"
#     DropDown_Manager_Vendor_Xpath = "//option[normalize-space()='Vendor 1']"             # "//select[@id='VendorId']" ---> to select the managervendor dropwdown box
#     Checkbox_Active_Xpath = "//input[@id='Active']"
#     Text_Admin_Comment_Xpath = "//textarea[@id='AdminComment']"
#     Click_SaveButton_Xpath = "//button[@name='save']"
#     Success_Message_Xpath = "//div[@class='alert alert-success alert-dismissable']"         # The new customer has been added successfully.
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def Click_Customers_Menu(self):
#         self.driver.find_element(By.XPATH,self.Click_Customer_menu_Xpath).click()
#
#     def Click_Customers_SubMenu(self):
#         self.driver.find_element(By.XPATH,self.Click_Customer_submenu_Xpath).click()
#
#     def Click_AddNewCustomer(self):
#         self.driver.find_element(By.XPATH,self.Click_AddNewCustomer_Xpath).click()
#
#     def Enter_Email(self,email):
#         self.driver.find_element(By.XPATH,self.Text_Email_Xpath).send_keys(email)
#
#     def Enter_Password(self,password):
#         self.driver.find_element(By.XPATH,self.Text_Password_Xpath).send_keys(password)
#
#     def Enter_FirstName(self,firstname):
#         self.driver.find_element(By.XPATH,self.Text_FirstName_Xpath).send_keys(firstname)
#
#     def Enter_LastName(self,lastname):
#         self.driver.find_element(By.XPATH,self.Text_LastName_Xpath).send_keys(lastname)
#
#     def Enter_Gender(self,gender):
#         if gender == "Male":
#             self.driver.find_element(By.XPATH,self.Radio_Male_Xpath).click()
#         elif gender == "Female":
#             self.driver.find_element(By.XPATH,self.Radio_Female_Xpath).click()
#
#     def Enter_DOB(self,date):
#         self.driver.find_element(By.XPATH,self.Calender_Xpath).send_keys(date)
#
#     def Enter_CompanyName(self,company_name):
#         self.driver.find_element(By.XPATH,self.Enter_CompanyName).send_keys(company_name)
#
#     def CheckBox_Tax(self):
#         self.driver.find_element(By.XPATH,self.CheckBox_Tax_Xpath).click()
#
#     def Click_NewsLetter(self):
#         self.driver.find_element(By.XPATH,self.Click_Newsletter_Xpath).click()
#
#     def Click_Newsletter_list(self):
#         self.driver.find_element(By.XPATH,self.Click_Newsletter_list_Xpath).click()
#
#     def Dropdown_Manager_of_vendor(self,value):
#         Select(self.driver.find_element(By.XPATH,self.DropDown_Manager_Vendor_Xpath)).select_by_visible_text(value)
#
#     def CheckBox_Active(self):
#         self.driver.find_element(By.XPATH,self.Checkbox_Active_Xpath).clcik()
#
#     def Enter_AdminComment(self,comment):
#         self.driver.find_element(By.XPATH,self.Text_Admin_Comment_Xpath).send_keys(comment)
#
#     def Click_SaveButton(self):
#         self.driver.find_element(By.XPATH,self.Click_SaveButton_Xpath).click()
#
#
#     def Validate_Success_Message(self):
#         try:
#             self.driver.find_element(By.XPATH,self.Success_Message_Xpath)
#             return "pass"
#         except:
#             return "fail"
