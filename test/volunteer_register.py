##Author: Divya
##Test Case : Register a volunteer

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
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\login.png")
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
            driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteerlist.png")
            time.sleep(3)
        ##Add volunteer button
            driver.get("https://gs-foodpantry.herokuapp.com/volunteer/signup")
            elem = driver.find_element_by_id("id_username")
            elem.send_keys(username)
            elem = driver.find_element_by_id("id_first_name")
            elem.send_keys(firstname)
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys(lastname)
            elem = driver.find_element_by_id("id_password")
            elem.send_keys(password)
            elem = driver.find_element_by_id("id_password2")
            elem.send_keys(password2)
            elem = driver.find_element_by_xpath("/html/body/form/button")
            elem.click()
            time.sleep(2)
            driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteersignup.png")
            elem = driver.find_element_by_xpath("/html/body/p/a")
            elem.click()
            time.sleep(2)
                ##volunteer gender
            elem = driver.find_element_by_id("id_Volunteer_Gender")
            elem.send_keys(gender)
            driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteerdetailspage.png")
                ##volunteer Age
            elem = driver.find_element_by_id("id_Volunteer_Age")
            elem.send_keys(age)
                ##Volunteer phone number
            elem = driver.find_element_by_id("id_Volunteer_Phone_Number")
            elem.send_keys(phoneno)
            elem = driver.find_element_by_id("id_Volunteer_Address")
            elem.send_keys(adress)
            elem = driver.find_element_by_id("id_Volunteer_City")
            elem.send_keys(city)
            elem = driver.find_element_by_id("id_Volunteer_State")
            elem.send_keys(state)
            elem = driver.find_element_by_id("id_Volunteer_Zipcode")
            elem.send_keys(zipcode)
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/button")
            elem.click()
            time.sleep(2)
            driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteersuccessfullyadded.png")
            assert(firstname)
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()