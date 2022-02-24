from dotenv import load_dotenv
import os, random, time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LinkedInConnections:


  def __init__(self):
    self.login_page = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"
    self.roles = ["software-engineer","full-stack-developer", "backend-developer", "front-end-developer", "python-developer", "blockchain-developer"]
    self.page = 1
    self.find_connections = f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290009496%22%5D&keywords={random.choice(self.roles)}&origin=FACETED_SEARCH&page={self.page}&position=0&schoolFilter=%5B%2212682%22%5D&searchId=4650e789-7233-4870-a8aa-9068b3f8f3cf&sid=xNy"
    self.driver = webdriver.Chrome()


  def connections(self):
    self.login()
    time.sleep(1.7)

    
    
    while self.page <= 5:
      time.sleep(1.3)
      self.driver.get(self.find_connections)
      all_buttons = self.driver.find_elements_by_tag_name("button")
      connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
      self.page += 1

      for btn in connect_buttons:
        # we will not use btn.click() because although it will work for our first button, the ones after will be intercepted through the blockers linkedin has. Therefore we will click using Javascript
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
        send = self.driver.find_element_by_xpath("//button[@aria-label='Send now']")
        self.driver.execute_script("arguments[0].click();", send)
        close = self.driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        self.driver.execute_script("arguments[0].click();", close)
        time.sleep(1.7)

      print("now")
      print(self.page)



    
    

  def login(self):
    self.driver.get(self.login_page) # go to login page
    self.accept_cookies()
    email_box = self.driver.find_element_by_id("username")
    load_dotenv()
    input_email = email_box.send_keys(os.getenv('EMAIL'))

    password_box = self.driver.find_element_by_id("password")
    input_password = password_box.send_keys(os.getenv('PASSWORD'))

    login_button = self.driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
    click_login = login_button.click()




  def accept_cookies(self):
    try:
      
      accept_cookies = self.driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]').click()
    except:
      print("cookies already accepted")




linkedin = LinkedInConnections()
linkedin.connections()

    