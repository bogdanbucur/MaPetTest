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

    # Register
    def test_001(self):
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

    # Login with Logout
    def test_002(self):

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

    # Login
    def test_003(self):
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

    # Create Custom Pet
    def test_004(self):
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

    # Select Mr. Fluff and Create First Post
    def test_005(self):
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

    # Scroll through NewsFeed and give some likes
    def test_006(self):
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

    # Add a Random Pet as Friend
    def test_007(self):
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

    # Fill in About section
    def test_008(self):
        sleep(2)

        # Enter About section
        self.driver.find_element_by_name('About').click()

        # Select Breed
        self.driver.find_elements_by_class_name('XCUIElementTypeButton')[4].click()
        self.driver.find_element_by_name('Done').click()
        sleep(2)
        breedField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        breedField.click()
        breedField.send_keys('HuffleFluff')
        self.driver.find_element_by_name('Confirm').click()

        # # Input Date of Birth
        # self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[3].click()
        # datePicker = self.driver.find_elements_by_class_name('XCUIElementTypeDatePicker')
        # datePicker['contains(@value, "June")'].click()
        # datePicker['contains(@value, "14")'].click()
        # datePicker['contains(@value, "2016")'].click()
        # self.driver.find_element_by_name('Done').click()

        # Input Place of Birth
        pobField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[4]
        pobField.click()
        pobField.send_keys('Bucharest')
        self.driver.find_element_by_name('Done').click()

        # Input Weight
        weightField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[5]
        weightField.click()
        weightField.send_keys('12.4 kg')
        self.driver.find_element_by_name('Done').click()

        # Save Data
        self.driver.find_element_by_name('SAVE').click()
        sleep(2)

    # Create a Post with Media
    def test_009(self):
        sleep(2)

        # Enter Create Post View
        self.driver.find_element_by_name("Woof! What's up?").click()

        # Input Text
        textField = self.driver.find_element_by_class_name('XCUIElementTypeTextView')
        textField.click()
        textField.send_keys('First post with media. Woof!')
        self.driver.find_element_by_name('Done').click()

        # Add Location
        self.driver.find_element_by_name('Location').click()
        self.driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()

        # Add Media
        self.driver.find_element_by_name('icn_bazaar_add.png').click()
        self.driver.find_element_by_name('Import from Gallery').click()
        sleep(2)
        self.driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
        self.driver.find_element_by_name('Select(1)').click()

        # Create Post
        self.driver.find_element_by_name('btn send').click()
        sleep(3)

    # Fill in Account Details
    def test_010(self):
        sleep(2)

        # Enter Settings View
        self.driver.find_element_by_name('icn settings').click()

        # Enter Account Settings View
        self.driver.find_element_by_name('Account Settings').click()

        # Select Male Gender
        self.driver.find_element_by_name('Gender').click()

        picker = self.driver.find_element_by_class_name('XCUIElementTypePickerWheel')
        xPicker = picker.location['x']
        yPicker = picker.location['y']
        heightPicker = picker.size['height']
        widthPicker = picker.size['width']

        self.driver.swipe(xPicker + widthPicker / 2, yPicker + heightPicker / 2 + 25, xPicker + widthPicker / 2, yPicker + heightPicker / 2)
        self.driver.find_element_by_name('Done').click()

        # Input Phone Number
        sleep(2)
        phoneField = self.driver.find_element_by_name('Telephone')
        phoneField.click()
        phoneField.send_keys('(555) 555 - 5555')
        self.driver.find_element_by_name('Done').click()

        # Input Website
        webField = self.driver.find_element_by_name('Website')
        webField.click()
        webField.send_keys('www.google.com')
        self.driver.find_element_by_name('Done').click()

        # Input Address
        addressField = self.driver.find_element_by_name('Address')
        addressField.click()
        addressField.send_keys('93.102.15.240')
        self.driver.find_element_by_name('Done').click()

        # Input City
        cityField = self.driver.find_element_by_name('City')
        cityField.click()
        cityField.send_keys('Bucharest')
        self.driver.find_element_by_name('Done').click()

        # Save Data
        self.driver.find_element_by_name('Save').click()
        sleep(3)

    # Check credits total and place an Offer afterwards
    def test_011(self):
        sleep(2)

        # Go to Settings
        self.driver.find_element_by_name('icn settings').click()

        # Go to Credits and check total
        self.driver.find_element_by_name('Credits').click()

        creditsText = self.driver.find_element_by_class_name('XCUIElementTypeAlert').get_attribute('name')
        creditsList = [int(s) for s in creditsText.split() if s.isdigit()]
        credits = int(''.join(map(str, creditsList)))

        self.driver.find_element_by_name('Ok').click()

        if credits > 50:

            # Go to My Offers
            self.driver.find_element_by_name('My Offers').click()
            self.driver.find_elements_by_class_name('XCUIElementTypeButton')[1].click()

            # Input title
            titleField = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
            titleField.click()
            sleep(2)
            titleField.send_keys('Giving away my Fluff')
            self.driver.find_element_by_name('Done').click()

            # Input description
            descriptionField = self.driver.find_elements_by_class_name('XCUIElementTypeTextView')[0]
            descriptionField.click()
            descriptionField.send_keys('My Fluff is the fluffiest fluff in the whole FluffLand and I am trying to find a more suitable owner for him.'
                                       'You need to be able to fully understand this kind of fluffness in order for him to feel comfortable.')
            self.driver.find_element_by_name('Done').click()

            # Add Photo
            self.driver.find_element_by_name('icn_bazaar_add.png').click()
            self.driver.find_element_by_name('Import from Gallery').click()
            sleep(2)
            self.driver.find_elements_by_class_name('XCUIElementTypeCell')[2].click()
            self.driver.find_element_by_name('Select(1)').click()

            # Select Free as Price
            self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[1].click()
            self.driver.find_element_by_name('Free').click()
            self.driver.find_element_by_name('Done').click()

            # Select Offer
            self.driver.find_element_by_name('Offer').click()

            # Scroll to bottom
            xSilver = self.driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther[3]').size['width'] / 2
            ySilver = self.driver.find_element_by_name('Silver').location['y']
            xPhotos = self.driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther[3]').size['width'] / 2
            yPhotos = self.driver.find_element_by_name('Photos').location['y']

            self.driver.swipe(xSilver, ySilver, xPhotos, yPhotos, 1000)
            print(xSilver, ySilver, xPhotos, yPhotos)

            # Create Offer
            self.driver.find_element_by_name('Create').click()
            sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaPetTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
