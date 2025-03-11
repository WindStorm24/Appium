import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from  appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "uiautomator2"
options.device_name = "Android"
options.language = "en"
options.locale = "US"

appium_server_url = 'http://localhost:4723'

json_file = 'data.json'


class TestAppium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_get_info(self):

        hotel_name = 'The Grosvenor Hotel'
        dates = [[11, 14],[12, 17],[20, 29],[13, 19],[15,16]]

        main_app = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Tripadvisor"]')
        main_app.click()

        try:
            serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Places to go, things to do, hotels…"]')))
            serch_element.click()
        except:
            self.driver.back()

            serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Places to go, things to do, hotels…"]')))
            serch_element.click()


        serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,  '//*[@text="Search"]')))
        serch_element.send_keys(f'{hotel_name}\n')


        serch_result = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.tripadvisor.tripadvisor:id/imgImage"])[1]')))
        serch_result.click()

        json_data = {}

        json_data[hotel_name] = {}

        for date in dates:

            x, y = date

            select_date_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.tripadvisor.tripadvisor:id/hotelInfoInputField"]')))
            select_date_el.click()


            date_1_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.tripadvisor.tripadvisor:id/txtDay" and @text="{x}"]')))
            date_1_el.click()

            date_2_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.tripadvisor.tripadvisor:id/txtDay" and @text="{y}"]')))
            date_2_el.click()


            apply_btn_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.tripadvisor.tripadvisor:id/btnPrimary"]')))
            apply_btn_el.click()


            provaider = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.tripadvisor.tripadvisor:id/imgProviderLogo")))
            provaider_name = provaider.get_attribute("contentDescription")

            price_el = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.tripadvisor.tripadvisor:id/txtPrice")))
            price = price_el.get_attribute("text")

            time.sleep(2)
            self.driver.get_screenshot_as_file(f"screenshot {x}-{y}.png")

            json_data[hotel_name][f'{x}-{y}'] = {f'{provaider_name}':price,
                                                       'screenshot': f"screenshot {x}-{y}.png"}


        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        return json_data




class Appium_class():
    def __init__(self, hotel_name, date_list):
        super().__init__()
        self.hotel_name = hotel_name
        self.dates = date_list

    def test_get_info(self):

        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.wait = WebDriverWait(self.driver, 10)


        main_app = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Tripadvisor"]')
        main_app.click()

        try:
            serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Places to go, things to do, hotels…"]')))
            serch_element.click()
        except:
            self.driver.back()

            serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Places to go, things to do, hotels…"]')))
            serch_element.click()


        serch_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,  '//*[@text="Search"]')))
        serch_element.send_keys(f'{self.hotel_name}\n')


        serch_result = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.tripadvisor.tripadvisor:id/imgImage"])[1]')))
        serch_result.click()

        json_data = {}

        json_data[self.hotel_name] = {}

        for date in self.dates:

            x, y = date

            select_date_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.tripadvisor.tripadvisor:id/hotelInfoInputField"]')))
            select_date_el.click()


            date_1_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.tripadvisor.tripadvisor:id/txtDay" and @text="{x}"]')))
            date_1_el.click()

            date_2_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.tripadvisor.tripadvisor:id/txtDay" and @text="{y}"]')))
            date_2_el.click()


            apply_btn_el = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.tripadvisor.tripadvisor:id/btnPrimary"]')))
            apply_btn_el.click()


            provaider = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.tripadvisor.tripadvisor:id/imgProviderLogo")))
            provaider_name = provaider.get_attribute("contentDescription")

            price_el = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.tripadvisor.tripadvisor:id/txtPrice")))
            price = price_el.get_attribute("text")

            time.sleep(2)
            self.driver.get_screenshot_as_file(f"screenshot {x}-{y}.png")

            json_data[self.hotel_name][f'{x}-{y}'] = {f'{provaider_name}':price,
                                                       'screenshot': f"screenshot {x}-{y}.png"}


        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        return json_data


if __name__ == "__main__":
    unittest.main()