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
        
        pre_lecture_btn = self.driver.find_element_by_xpath('//*[@id="module-1494772"]/div/div/div[2]/div/a/span')
        pre_lecture_btn.click()
        
        sleep(1)
        
        continue_test_btn = self.driver.find_element_by_xpath('//*[@id="single_button5ee5ac712f5fa16"]')
        continue_test_btn.click()
        
        
        
    def get_questions(self):
        question = self.driver.find_element_by_xpath('//*[@id="q1"]/div[2]/div/div[1]')
        question.send_keys(Keys.CONTROL, 'a')  # highlight all in box
        question.send_keys(Keys.CONTROL, 'c')  # copy
        
        answer_in = self.driver.find_element_by_xpath('//*[@id="q1689368:1_answer"]')
        answer_in.click()
        answer_in.send_keys(Keys.CONTROL, 'v')  # paste


        
        
'''           
    def auto_answer(self):
        answered = 0
        
        while True:
            sleep(1)
            try:
                self.get_question()
                self.get_answer()
                answered += 1
                print(f'Questions answered: {answered}')
            except Exception:
                pass
            
'''
