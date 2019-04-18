##Author: Divya
##Test Case : Delete a volunteer

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

        ##volunteer link
        driver.get("https://gs-foodpantry.herokuapp.com/volunteer_list")
        time.sleep(3)
        ##Delete Volunteer Button
        driver.get("https://gs-foodpantry.herokuapp.com/admin/")
        driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[6]/th/a").click()
        driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[3]/th/a").click()
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\volunteerdeletebutton.png")
        driver.find_element_by_xpath("//*[@id='volunteer_form']/div/div/p/a").click()
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\deleteconfirmation.png")
        driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\visitsite.png")
        driver.find_element_by_xpath("//*[@id='user-tools']/a[1]")
        driver.get("https://gs-foodpantry.herokuapp.com/volunteer_list")
        driver.get_screenshot_as_file("C:\\Users\\Divya\\PycharmProjects\\test\\Screenshots\\updatedvolunteerlist.png")
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()