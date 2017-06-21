import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class MaPetTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/bogdanbucur/PycharmProjects/MaPetTest/src/MaPet.ipa',
                'platformName': 'iOS',
                'platformVersion': '10.0',
                'deviceName': 'iPhone 6'
            })

    def test_1(self):
        sleep(2)

    def tearDown(self):
        self.driver.quit()


suite = unittest.TestLoader().loadTestsFromTestCase(MaPetTest)
unittest.TextTestRunner(verbosity=2).run(suite)
