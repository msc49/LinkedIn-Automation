from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class LinkedInConnections:


  def __init__(self):
    self.login_page = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"
    self.roles = ["software-engineer","full-stack-developer", "backend-developer", "front-end-developer", "python-developer", "blockchain-developer"]
    
    self.find_connections = f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290009496%22%5D&keywords={random.choice(self.roles)}&origin=FACETED_SEARCH&position=0&schoolFilter=%5B%2212682%22%5D&searchId=4650e789-7233-4870-a8aa-9068b3f8f3cf&sid=xNy"
    self.driver = webdriver.Chrome()
    


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
      
      accept_cookies = self.driver.find_element_by_xpath("//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]").click()
    except:
      print("cookies already accepted")


    