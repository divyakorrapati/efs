##Author: Divya
##Test Case : Edit volunteer details

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


class foodpantry_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_pantry(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://gs-foodpantry.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id('id_username')
        elem.send_keys("instructor")
        elem = driver.find_element_by_id('id_password')
        elem.send_keys("instructor1a")
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        with open("data.csv", "r") as fh:
            lines = csv.reader(fh)
            for line in lines:
                username = line[0]
                firstname = line[1]
                lastname = line[2]
                password = line[3]
                password2 = line[4]
                gender = line[5]
                age = line[6]
                phoneno = line[7]
                adress = line[8]
                city = line[9]
                state = line[10]
                zipcode = line[11]
        ##volunteer link
        driver.get("https://gs-foodpantry.herokuapp.com/volunteer_list")
        time.sleep(3)
        ##Add volunteer button
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[3]/td[12]/a").click()
        #driver.get("https://gs-foodpantry.herokuapp.com/volunteer/3/edit/")
        time.sleep(2)
        ##volunteer gender
        elem = driver.find_element_by_id("id_Volunteer_Gender")
        elem.send_keys()
        elem.send_keys(gender)
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteeredit.png")
        ##volunteer Age
        elem = driver.find_element_by_id("id_Volunteer_Age")
        elem.clear()
        elem.send_keys(age)
        ##Volunteer phone number
        elem = driver.find_element_by_id("id_Volunteer_Phone_Number")
        elem.clear()
        elem.send_keys(phoneno)
        elem = driver.find_element_by_id("id_Volunteer_Address")
        elem.clear()
        elem.send_keys(adress)
        elem = driver.find_element_by_id("id_Volunteer_City")
        elem.clear()
        elem.send_keys(city)
        elem = driver.find_element_by_id("id_Volunteer_State")
        elem.clear()
        elem.send_keys(state)
        elem = driver.find_element_by_id("id_Volunteer_Zipcode")
        elem.clear()
        elem.send_keys(zipcode)
        elem = driver.find_element_by_xpath("/html/body/div[2]/form/button")
        elem.click()
        time.sleep(2)
        assert(zipcode)
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteereditsucessful.png")
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()