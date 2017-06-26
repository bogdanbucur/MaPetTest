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
                'platformVersion': '10.3',
                'deviceName': 'iPhone 7',
                'noReset': 'True'
            })

#   Register
#     def test_1(self):
#         sleep(2)
#         self.driver.find_element_by_name('REGISTER').click()
#
#         # Input Email Address
#         self.driver.find_element_by_class_name('XCUIElementTypeTextField').click()
#         self.driver.find_element_by_class_name('XCUIElementTypeTextField').clear()
#         self.driver.find_element_by_class_name('XCUIElementTypeTextField').send_keys('bogdan.bucur@udevoffice.ro')
#
#         # Input Password
#         passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
#         passField.click()
#         passField.clear()
#         passField.send_keys('supersecret')
#
#         # Confirm Password
#         confirmPassField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
#         confirmPassField.click()
#         confirmPassField.clear()
#         confirmPassField.send_keys('supersecret')
#         self.driver.find_element_by_accessibility_id('Done').click()
#
#         # Submit
#         self.driver.find_element_by_accessibility_id('CONTINUE').click()
#         sleep(4)
#
#         # Logout
#         self.driver.find_element_by_accessibility_id('LOGOUT').click()
#         sleep(2)
#         self.driver.find_element_by_name('Yes').click()
#         sleep(3)

# Login with Logout
#     def test_2(self):
#
#         self.driver.find_element_by_name('LOGIN').click()
#         sleep(2)
#
#         # Input Email Address
#         emailField = self.driver.find_element_by_class_name('XCUIElementTypeTextField')
#         emailField.click()
#         emailField.clear()
#         emailField.send_keys('bogdan.bucur@udevoffice.ro')
#
#         # Input Password
#         passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
#         passField.click()
#         passField.clear()
#         passField.send_keys('supersecret')
#
#         # Hide Keyboard
#         self.driver.find_element_by_accessibility_id('Done').click()
#
#         # Login
#         self.driver.find_element_by_accessibility_id('CONTINUE').click()
#         sleep(2)
#
#         # Logout
#         self.driver.find_element_by_accessibility_id('LOGOUT').click()
#         sleep(2)
#         self.driver.find_element_by_name('Yes').click()
#         sleep(3)

# Login
#     def test_3(self):
#         # Enter Login Page
#         sleep(2)
#         self.driver.find_element_by_name('LOGIN').click()
#         sleep(2)
#
#         # Input Email Address
#         emailField = self.driver.find_element_by_class_name('XCUIElementTypeTextField')
#         emailField.click()
#         emailField.clear()
#         emailField.send_keys('bogdan.bucur@udevoffice.ro')
#
#         # Input Password
#         passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
#         passField.click()
#         passField.clear()
#         passField.send_keys('supersecret')
#
#         # Hide Keyboard
#         self.driver.find_element_by_accessibility_id('Done').click()
#
#         # Login
#         self.driver.find_element_by_accessibility_id('CONTINUE').click()
#         sleep(2)

#   Create Custom Pet
#     def test_4(self):
#         sleep(2)
#
#         # Input Name
#         self.driver.find_element_by_accessibility_id('ADD PET').click()
#         sleep(2)
#
#         nameField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
#         nameField.click()
#         nameField.send_keys('Mr. Fluff')
#         self.driver.find_element_by_accessibility_id('Done').click()
#         sleep(1)
#
#         # Add Custom Species
#         self.driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()
#         sleep(2)
#         self.driver.find_element_by_accessibility_id('Done').click()
#         sleep(1)
#         specieField = self.driver.find_element_by_name('Species')
#         specieField.click()
#         specieField.send_keys('Fluff')
#         self.driver.find_element_by_accessibility_id('Confirm').click()
#
#         # Select Male Sex
#         self.driver.find_elements_by_class_name('XCUIElementTypeButton')[4].click()
#         sleep(1)
#         self.driver.find_element_by_accessibility_id('Done').click()
#
#         # Input Description
#         descriptionField = self.driver.find_element_by_name('Description')
#         descriptionField.click()
#         descriptionField.send_keys('Fluffiest fluff in the entire Fluff Land.')
#         self.driver.find_element_by_accessibility_id('Done').click()
#
#         # Create Pet
#         self.driver.find_element_by_accessibility_id('CREATE PET').click()

#   Select Mr. Fluff and Create First Post
#     def test_5(self):
#         sleep(2)
#         self.driver.find_element_by_name('Mr. Fluff').click()
#         self.driver.find_element_by_name('CONTINUE').click()
#         sleep(2)
#
#         # Write Post
#         self.driver.find_element_by_name("Woof! What's up?").click()
#         sleep(2)
#
#         postField = self.driver.find_element_by_name('Write your post...')
#         postField.click()
#         postField.send_keys('My first Post. Woof!')
#         self.driver.find_element_by_accessibility_id('Done').click()
#         sleep(2)
#
#         # Add Location
#         self.driver.find_element_by_name('Location').click()
#         self.driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
#         self.driver.find_element_by_accessibility_id('btn send').click()
#         sleep(5)

#   Scroll through NewsFeed and give some likes
    def test_6(self):
        sleep(2)

        # Go to NewsFeed
        self.driver.find_element_by_accessibility_id('btn menu feed inactive boy').click()

        cell = self.driver.find_elements_by_xpath('//XCUIElementTypeApplication[@name="MaPet"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                  '/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                  '/XCUIElementTypeTable/XCUIElementTypeCell')

        # Iterate the Cell List and give Random likes
        for i in cell:
            like = randint(0, 1)
            if like == 1:
                i.find_elements_by_class_name('XCUIElementTypeButton')[0].click()

        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaPetTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
