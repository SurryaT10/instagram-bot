from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.webdriver = webdriver.Chrome('C:/Users/Surrya Jay/Downloads/chromedriver_win32/chromedriver')

    def login(self):
        bot = self.webdriver
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)

        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

        nt_now_btn = bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        time.sleep(1)

    def sendMsg(self):
        bot = self.webdriver
        dm_btn = bot.find_element_by_class_name('xWeGp').click()
        time.sleep(3)

        msg = bot.find_element_by_class_name('-qQT3.rOtsg').click()
        time.sleep(3)

        dm = bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/textarea')
        time.sleep(10)

        send_btn = bot.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button')
        send_btn.click()
bot = InstaBot('username', 'password')
bot.login()
bot.sendMsg()
