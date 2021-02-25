from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
class LoginPage():

    def Instlogin(self):
        Baseurl='http://login.cengage.com/'

        driver.maximize_window()
        driver.get(Baseurl)
        time.sleep(5)
        print("Title of the page is: " + driver.title)

        UserName=driver.find_element_by_id('idp-discovery-username')
        UserName.send_keys("inst014_mt_10072020@cloud.cengage.com")

        driver.find_element_by_id('idp-discovery-submit').click()

        time.sleep(5)

        Password = driver.find_element_by_id('okta-signin-password')
        Password.send_keys("Mindtap321")

        driver.find_element_by_id('okta-signin-submit').click()
        time.sleep(3)

        print("Title of the page is: " + driver.title)
        #driver.current_window_handle

        #search=driver.find_element_by_id('searchword').send_keys('9781337612487')
        #search.send_keys('9781337612487')
        #driver.find_elements_by_xpath("//form[@id='dashboard_form']//input[@name='search']").click()

        driver.find_element(By.LINK_TEXT,"Manage Courses").click()
        driver.implicitly_wait(3)
        driver.find_element(By.LINK_TEXT,"Regression_Today Technician_23Feb21" ).click()
        driver.implicitly_wait(6)
        print("Title of the page is: " + driver.title)

        parentHandle=driver.current_window_handle
        handles=driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                driver.find_element(By.ID,"AddDropdown").click()
                parent_h = driver.current_window_handle
                driver.find_element(By.LINK_TEXT, "Activity").click()
                handles2 = driver.window_handles  # before the pop-up window closes
                #handles2.remove(parent_h)
                driver.switch_to.window(handles2.pop())


                driver.find_element(By.XPATH,"/html//div[@role='dialog']/div[@class='cl-add-activity-dialog css-108suzk-ModalContent e4fl96f2']/div[@class='css-1ntomz8-ModalBody e4fl96f6']/div/div[5]//div[@class='description']").click()
                handle3 = driver.window_handles
                driver.implicitly_wait(50)

                driver.find_element(By.XPATH,"/html//div[@id='overview_main']/div[@class='pageContentBody']//a[@href='/ilrn/createAssignmentSteps/start.do?invoker=assignments']").click()
                driver.switch_to.window[2]
                driver.implicitly_wait(15)

                driver.find_element(By.LINK_TEXT,"Continue").click()
                # time.sleep(3)
                # driver.find_element(By.XPATH,"//input[@id='assignmentName']").send_keys('TB 1')


Login=LoginPage()
Login.Instlogin()

