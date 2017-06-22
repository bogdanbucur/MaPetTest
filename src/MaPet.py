import unittest
import os
import random
from random import randint
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class MaPetTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/bogdanbucur/PycharmProjects/MaPetTest/src/MaPet.app',
                'automationName': 'XCUITest',
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6s Plus'
            })

    # # Register
    # def test_1(self):
    #     sleep(2)
    #     if self.driver.find_element_by_accessibility_id('OK').is_displayed():
    #         self.driver.find_element_by_accessibility_id('OK').click()
    #     sleep(2)
    #
    #     self.driver.find_element_by_accessibility_id('REGISTER').click()
    #
    #     # Input Email Address
    #     self.driver.find_element_by_class_name('XCUIElementTypeTextField').click()
    #     self.driver.find_element_by_class_name('XCUIElementTypeTextField').clear()
    #     self.driver.find_element_by_class_name('XCUIElementTypeTextField').send_keys('bogdan.bucur@udevoffice.ro')
    #
    #     # Input Password
    #     passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
    #     passField.click()
    #     passField.clear()
    #     passField.send_keys('supersecret')
    #
    #     # Confirm Password
    #     confirmPassField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
    #     confirmPassField.click()
    #     confirmPassField.clear()
    #     confirmPassField.send_keys('supersecret')
    #     self.driver.find_element_by_accessibility_id('Done').click()
    #
    #     # Submit
    #     self.driver.find_element_by_accessibility_id('CONTINUE').click()
    #     sleep(4)

    # Login with Logout
    def test_2(self):
        sleep(2)
        if self.driver.find_element_by_accessibility_id('OK').is_displayed():
            self.driver.find_element_by_accessibility_id('OK').click()
        sleep(2)

        self.driver.find_element_by_accessibility_id('LOGIN').click()
        sleep(2)

        # Input Email Address
        emailField = self.driver.find_element_by_class_name('XCUIElementTypeTextField')
        emailField.click()
        emailField.clear()
        emailField.send_keys('bogdan.bucur@udevoffice.ro')

        # Input Password
        passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        passField.click()
        passField.clear()
        passField.send_keys('supersecret')

        # Login
        self.driver.find_element_by_accessibility_id('CONTINUE').click()
        sleep(2)

        # Logout
        self.driver.find_element_by_accessibility_id('LOGOUT').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Yes')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaPetTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
