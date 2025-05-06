from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4.2)

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(2.1)
        password.send_keys(Keys.ENTER)
        time.sleep(4.3)

        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]").click()
        time.sleep(3.7)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(8.2)

        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
