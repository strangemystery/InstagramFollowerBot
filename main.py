import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import ElementClickInterceptedException
import time
import random

searching_id = "User to extract Followers from"
login_id = os.environ.get("USERNAME")
ser = Service(r" The Driver's Location")
password = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        self.a = None
        global ser
        global searching_id
        global login_id
        global password
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("no-sandbox")
        options.add_argument("disable-infobars")
        options.add_argument("disbale-dev-shm-usage")
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)

        options.add_argument("disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(service=ser, options=options)

    def login_insta(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(5)
        input_username = self.driver.find_element(By.NAME, "username")
        input_username.send_keys(login_id)
        time.sleep(1)
        input_password = self.driver.find_element(By.NAME, "password")
        input_password.send_keys(password)
        time.sleep(1)
        submit = self.driver.find_element(By.CLASS_NAME, "_acas")
        submit.click()
        time.sleep(7)

        notification_off = self.driver.find_element(By.CSS_SELECTOR, "._a9_1")
        notification_off.click()
        time.sleep(5)

    def search(self):
        search_select = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]')
        search_select.click()
        time.sleep(5)
        id_entry = self.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        id_entry.send_keys(searching_id)
        time.sleep(8)
        search_result = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[2]/span")
        search_result.click()
        time.sleep(8)

    def followers_check(self):
        followers_list = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span')


        # for Listing most Followers
        """
        num_to_scroll = followers_list.text
        if "K" in num_to_scroll:
            fin = num_to_scroll.strip('K')
            final_num = float(fin) * 1000
            div_factor = 100
        if "M" in num_to_scroll:
            fin = num_to_scroll.strip('M')
            final_num = float(fin) * 100000
            div_factor = 10000

        else:
            final_num = int(num_to_scroll)
            div_factor = 6
        """
        div_factor = 6
        final_num = 30

        followers_list.click()
        time.sleep(10)
        modal = self.driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(int(final_num / div_factor)):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(random.randint(1, 4))

        actual_followers = self.driver.find_elements(By.CSS_SELECTOR,
                                                     ".x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")
        followers = []

        for follower in actual_followers:
            followers.append(follower.text)

        print(followers)
        print(len(followers))
        self.a = len(followers)

    def follow(self):
        for i in range(1, self.a):
            print(i, "   ", self.a)
            peoples_follow = self.driver.find_elements(By.XPATH,
                                                       f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button/div/div')

            for button in peoples_follow:
                print(button.text)
                if button.text == "Follow":
                    print("following")
                    # action.move_to_element(button).click().perform()
                    button.click()
                    print("Followed\n")
                    time.sleep(random.randint(5, 10))

        time.sleep(15)


bot = InstaFollower()
bot.login_insta()
bot.search()
bot.followers_check()
bot.follow()
