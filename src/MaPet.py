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
                'noReset': True,
                'fullReset': False
            })


#   Register
    def test_1(self):
        sleep(2)
        self.driver.find_element_by_name('REGISTER').click()

        # Input Email Address
        self.driver.find_element_by_class_name('XCUIElementTypeTextField').click()
        self.driver.find_element_by_class_name('XCUIElementTypeTextField').clear()
        self.driver.find_element_by_class_name('XCUIElementTypeTextField').send_keys('bogdan.bucur@udevoffice.ro')

        # Input Password
        passField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[0]
        passField.click()
        passField.clear()
        passField.send_keys('supersecret')

        # Confirm Password
        confirmPassField = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')[1]
        confirmPassField.click()
        confirmPassField.clear()
        confirmPassField.send_keys('supersecret')
        self.driver.find_element_by_accessibility_id('Done').click()

        # Submit
        self.driver.find_element_by_accessibility_id('CONTINUE').click()
        sleep(4)

        # Logout
        self.driver.find_element_by_accessibility_id('LOGOUT').click()
        sleep(2)
        self.driver.find_element_by_name('Yes').click()
        sleep(3)

#   Login with Logout
    def test_2(self):

        self.driver.find_element_by_name('LOGIN').click()
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

        # Hide Keyboard
        self.driver.find_element_by_accessibility_id('Done').click()

        # Login
        self.driver.find_element_by_accessibility_id('CONTINUE').click()
        sleep(2)

        # Logout
        self.driver.find_element_by_accessibility_id('LOGOUT').click()
        sleep(2)
        self.driver.find_element_by_name('Yes').click()
        sleep(3)

#   Login
    def test_3(self):
        # Enter Login Page
        sleep(2)
        self.driver.find_element_by_name('LOGIN').click()
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

        # Hide Keyboard
        self.driver.find_element_by_accessibility_id('Done').click()

        # Login
        self.driver.find_element_by_accessibility_id('CONTINUE').click()
        sleep(2)

#   Create Custom Pet
    def test_4(self):
        sleep(2)

        try:
            # Input Name
            self.driver.find_element_by_accessibility_id('ADD PET').click()
            sleep(2)
            pass
        except:

            # Login
            self.driver.find_element_by_name('LOGIN').click()
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

            # Hide Keyboard
            self.driver.find_element_by_accessibility_id('Done').click()

            # Login
            self.driver.find_element_by_accessibility_id('CONTINUE').click()
            sleep(2)

        # Input Name
        self.driver.find_element_by_accessibility_id('ADD PET').click()
        sleep(2)

        nameField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        nameField.click()
        nameField.send_keys('Mr. Fluff')
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)

        # Add Custom Species
        self.driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)
        specieField = self.driver.find_element_by_name('Species')
        specieField.click()
        specieField.send_keys('Fluff')
        self.driver.find_element_by_accessibility_id('Confirm').click()

        # Select Male Sex
        self.driver.find_elements_by_class_name('XCUIElementTypeButton')[4].click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Done').click()

        # Input Description
        descriptionField = self.driver.find_element_by_name('Description')
        descriptionField.click()
        descriptionField.send_keys('Fluffiest fluff in the entire Fluff Land.')
        self.driver.find_element_by_accessibility_id('Done').click()

        # Create Pet
        self.driver.find_element_by_accessibility_id('CREATE PET').click()

#   Select Mr. Fluff and Create First Post
    def test_5(self):
        sleep(2)
        self.driver.find_element_by_name('Mr. Fluff').click()
        self.driver.find_element_by_name('CONTINUE').click()
        sleep(2)

        # Write Post
        self.driver.find_element_by_name("Woof! What's up?").click()
        sleep(2)

        postField = self.driver.find_element_by_name('Write your post...')
        postField.click()
        postField.send_keys('My first Post. Woof!')
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(2)

        # Add Location
        self.driver.find_element_by_name('Location').click()
        self.driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
        self.driver.find_element_by_accessibility_id('btn send').click()
        sleep(5)

#   Scroll through NewsFeed and give some likes
    def test_6(self):
        sleep(2)

        # Go to NewsFeed
        self.driver.find_element_by_accessibility_id('btn menu feed inactive boy').click()

        cellList = self.driver.find_elements_by_class_name('XCUIElementTypeCell')

        # Iterate the Posts List
        for i in range(1, len(cellList)):

            el1 = self.driver.find_elements_by_class_name('XCUIElementTypeCell')[i]
            el2 = self.driver.find_elements_by_class_name('XCUIElementTypeCell')[i + 1]
            navbar = self.driver.find_element_by_class_name('XCUIElementTypeNavigationBar')

            like = randint(0, 1)

            if like == 1:
                try:
                    el1.find_element_by_name('Liked')
                    pass
                except:
                    likeButton = el1.find_element_by_name('Like')
                    likeButton.click()
            else:
                pass

            # el1Height = el1.size['height']
            # el1Width = el1.size['width']
            # el1x = el1.location['x'] + el1Width / 2
            # el1y = el1.location['y'] + el1Height / 2

            navbarHeight = navbar.size['height']
            navbarWidth = navbar.size['width']
            xNavbar = navbar.location['x'] + navbarWidth
            yNavbar = navbarHeight + 20

            el2Height = el2.size['height']
            el2Width = el2.size['width']
            el2x = el2.location['x']
            el2y = el2.location['y']

            self.driver.swipe(el2x, el2y, (xNavbar - el2x), (yNavbar - el2y), 1000)

            print(navbarHeight, navbarWidth, xNavbar, yNavbar, '/n', el2Height, el2Width, el2x, el2y)

        sleep(4)

#   Do a Random Pet as Friend
    def test_7(self):
        sleep(2)

        # Go to NewsFeed
        self.driver.find_element_by_accessibility_id('btn menu feed inactive boy').click()

        # Get Cell List
        cellList = self.driver.find_elements_by_class_name('XCUIElementTypeCell')

        # Iterate the Posts List
        for i in range(1, len(cellList)):
            el1 = self.driver.find_elements_by_class_name('XCUIElementTypeCell')[i]
            el2 = self.driver.find_elements_by_class_name('XCUIElementTypeCell')[i + 1]
            navbar = self.driver.find_element_by_class_name('XCUIElementTypeNavigationBar')

            # 50% Chance of Befriending a pet
            chance = randint(0, 1)

            if chance == 1:

                # Check if cell is a Post
                try:
                    el1.find_element_by_name('Stevie')

                    # Make sure that the Post is not yours
                    petName = el1.find_elements_by_class_name('XCUIElementTypeStaticText')[1]

                    # If Post is not yours then access Pet's Profile and Add as Friend
                    if petName.get_attribute('value') != 'Mr. Fluff':
                        el1.find_elements_by_class_name('XCUIElementTypeButton')[2].click()
                        sleep(2)
                        self.driver.find_element_by_name('btn addPhotos topBar').click()
                        self.driver.find_element_by_name('Add Friend Request').click()
                    else:
                        pass

                except:
                    pass

                break

            # Chance is 0, Scroll to next Post
            navbarHeight = navbar.size['height']
            navbarWidth = navbar.size['width']
            xNavbar = navbar.location['x'] + navbarWidth
            yNavbar = navbarHeight + 20

            # el2Height = el2.size['height']
            # el2Width = el2.size['width']
            el2x = el2.location['x']
            el2y = el2.location['y']

            self.driver.swipe(el2x, el2y, (xNavbar - el2x), (yNavbar - el2y), 1000)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaPetTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
