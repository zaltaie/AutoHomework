'''
This will login into coursesapces, and whenever a question with,
"What is the output" is included will return the answer"
'''

from selenium import webdriver
from login import user,passw
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class CourseSpaces():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://www.uvic.ca/cas/login?service=https%3A%2F%2Fcoursespaces.uvic.ca%2Flogin%2Findex.php')
        
        user_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        user_in.send_keys(user)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(passw)

        login_btn = self.driver.find_element_by_xpath('//*[@id="form-submit"]')
        login_btn.click()
        
        sleep(1)
        
        course_btn = self.driver.find_element_by_xpath('//*[@id="course-info-container-79167"]/div/div[2]/h4/a')
        course_btn.click()
        
        #Need
        
