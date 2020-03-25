""" IMPORTANT """
""" In order to use the code, you have to download the webdriver from Chrome's website, 
and have a separate file named tinder_login.py with your username and password """

#Notes: 
# Each action performed on the browser has 2 steps: Select (using the element xpath) and Interact (click/send keys).
# I noticed than when the browser is resized, the xpath of the elements change, therefore making the code 
# unable to reach said element. All the try/except clauses in the code work around this issue.

from selenium import webdriver
import time, random
from tinder_login import username, password
from selenium.webdriver.common.keys import Keys

# path to the webdriver folder
""" UPDATE THIS PATH """
webdriver_path = r""

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=webdriver_path)
        self.driver.maximize_window()
        self.driver.get('https://tinder.com')

    def login(self):
        #select and click the facebook login button
        try:
            fb_btn = self.driver.find_element_by_xpath('//*[contains(@aria-label,"Facebook")]')
            fb_btn.click() 

        except Exception:
            try:
                fb_btn = self.driver.find_element_by_xpath("//*[contains(text(),'Facebook')]")
                fb_btn.click() 

            except Exception:
                try:
                    login_btn = self.driver.find_element_by_xpath("//span[text()='Inicia sesión']/..")
                    login_btn.click()
                    fb_btn = self.driver.find_element_by_xpath('//*[contains(@aria-label,"Facebook")]')
                    fb_btn.click() 

                except:
                    opciones_btn = self.driver.find_element_by_xpath("//button[text()='Más opciones']")  
                    opciones_btn.click()
                    time.sleep(1)
                    fb_btn = self.driver.find_element_by_xpath('//*[contains(@aria-label,"Facebook")]')
                    fb_btn.click() 

        time.sleep(2)
    
        #switch to  facebook login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        #types your credentials into the facebook popup and logs in
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        passw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passw_in.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        #switches back to the main window
        self.driver.switch_to.window(base_window)
        time.sleep(3)
        self.initial_popup_handling()

    """  POPUP HANDLING AFTER LOGING IN  """
    #this takes care of the messages that appear after loging in 
    def initial_popup_handling(self):
        try:
            share_location_btn = self.driver.find_element_by_xpath("//button[@aria-label='Permitir']")
            share_location_btn.click()
            return True
        except Exception:
            pass
        try:
            notif_btn = self.driver.find_element_by_xpath("//*[@data-testid='allow']") #or decline
            notif_btn.click()
            return True
        except Exception: 
            pass

        try:
            popup1 = self.driver.find_element_by_xpath("//button[contains(text(),'Recordarme')]")
            popup1.click()
            return True
        except:
            pass
        try:
            cookies_banner_btn = self.driver.find_element_by_xpath("//*[@aria-label='Activar']")
            cookies_banner_btn.click()
            return True
        except:
            pass
    
    def other_popup_handling(self):
        try:
            #takes care of one of the popups that appear randomly. Gotta change that xpath though
            popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            popup1.click()
            return True
        except Exception:
            return False

    """ LIKE """
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//button[@aria-label="Like"]')                            
        like_btn.click()

    """ DISLIKE """
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//button[@aria-label="No"]') 
        dislike_btn.click()
      
    """ MESSAGE A MATCH IT IT OCCURS DURING SWIPING """ 
    def message_match(self):
        num = random.random()*2+2
        time.sleep(num)
        message = 'Hey! I like your pictures' #CAN BE MODIFIED
        match_popup_message_box = self.driver.find_element_by_xpath('//textarea[@id="chat-text-area"]')
        match_popup_message_box.send_keys(message)
        send_btn = self.driver.find_element_by_xpath('//form/button[@type="submit"]')
        send_btn.click()

        #sigue_deslizando_btn = self.driver.find_element_by_xpath('//a[@aria-current="page"]') #href="/app/recs" #'//a[contains(text(),"Sigue deslizando")]'

        num2 = random.random()*2
        time.sleep(num2)       
        match_popup_message_box.send_keys(message)

    """ SWIPE """
    def swipe(self):
        for i in range(100):
            num = random.random()*3+2
            time.sleep(num)
            try: 
                #photo_swipe_n = random.randint[1,4]
                body = self.driver.find_element_by_xpath('//body') 
                #for p in range(photo_swipe_n):
                for p in range(3):
                    body.send_keys(Keys.SPACE)
                    time.sleep(1)
                #    pp = random.random()+0.5
                #    time.sleep(pp)                    
                n = random.random()
                time.sleep(n*2+1) #Yeah n is used twice
                if n<0.8: #LIKES WITH A PROB OF 80%, DISLIKES WITH 20%
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    #maybe its a match so we gonna try to send a message
                    time.sleep(3)
                    self.message_match()
                    
                    #if it wasnt a match we´re gonna see if there are popups
                except Exception:
                    self.initial_popup_handling()
                    time.sleep(1)
                    self.other_popup_handling()

bot = TinderBot()
#bot.login()
#bot.swipe()