from classes.parser import Parser
import configparser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Instagram:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
    
    def login(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        
        usr=config["Instagram"]["username"]
        pwd=config["Instagram"]["password"]

        self.driver.get('https://www.instagram.com/') 
        print ("Opened instagram")
        sleep(1)

        username_box = self.driver.find_element_by_name('username')
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(1) 
        
        password_box = self.driver.find_element_by_name('password')
        password_box.send_keys(pwd) 
        print ("Password entered") 
        login_box = self.driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div") 
        login_box.click() 
        
        print ("Done")
        sleep(5)

    def openInbox(self):
        self.driver.get('https://www.instagram.com/direct/inbox')
        shutdown_notification = self.driver.find_element_by_class_name("HoLwm")
        shutdown_notification.click()
        print("hide popup")
        sleep(10)

    def openUnreadChat(self):
        self.driver.get('https://www.instagram.com/direct/inbox')
        sleep(10)
        try:
            unread_msg = self.driver.find_element_by_class_name("soMvl")
            unread_msg.click()
            print("select unread chat")
            sleep(10)
            parser = Parser(self.driver.page_source)
            parser.get_content()
            sleep(5)
            self.openUnreadChat() #todo
        except NoSuchElementException:
            sleep(10)
            self.openUnreadChat()
    
    def finish(self):
        self.driver.quit()
        print("Finished")

