from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import datetime

#leaves the window open after running the program
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#defines driver
driver: any

#login with give user and passward
def login(user: str, passward:str):
    username_input = '/html/body/div[1]/div/div[1]/form/ul[1]/li[1]/input'
    password_input = '/html/body/div[1]/div/div[1]/form/ul[1]/li[2]/input'
    login_submit = '/html/body/div[1]/div/div[1]/form/ul[2]/li/input'
    driver.find_element(by=By.XPATH, value=username_input).send_keys(user)
    driver.find_element(by=By.XPATH, value=password_input).send_keys(passward)
    driver.find_element(by=By.XPATH, value=login_submit).click()


#adds SLN codes, if there is additional SLN codes it will go to the next input
SLN_box = 2
def addSLN(class_code: int):
    global SLN_box 
    SLN_input = '/html/body/div[2]/form/p[2]/table/tbody/tr['+str(SLN_box)+']/td[1]/input'
    driver.find_element(by=By.XPATH, value=SLN_input).send_keys(class_code)
    if SLN_box <=8:
        SLN_box += 1

#adds class entry codes if it is need to join the class
addCode_box =2
def addCodes(add_code: int):
    global addCode_box
    addCode_input = '/html/body/div[2]/form/p[2]/table/tbody/tr['+str(addCode_box)+']/td[2]/input'
    driver.find_element(by=By.XPATH, value=addCode_input).send_keys(add_code)
    if addCode_box <=8:
        addCode_box += 1

#adds a credit amount for credit variable classes
credit_box =2
def addCredit(credit_code: str):
    global credit_box
    credit_input = '/html/body/div[2]/form/p[2]/table/tbody/tr['+str(credit_box)+']/td[3]/input'
    driver.find_element(by=By.XPATH, value=credit_input).send_keys(credit_code)
    if credit_box <=8:
        credit_box += 1

#runs until it is 5 seconds before the given registration date
#it will then continously submit codes until classes are registered
def registerDate(hour: int, min: int, sec: int):
    t=datetime.datetime.now()
    print(hour,min,sec)

    #starts the registering 5 seconds before actual date
    sec = 55
    min = min - 1
    send_class = '/html/body/div[2]/form/input[7]'
    while(1): 
        if (t.hour == hour)and(t.minute == min)and(t.second == sec):
            #driver.find_element_by_xpath(send_class).click()
            break
        else:
            t=datetime.datetime.now()
    
    t=datetime.datetime.now()
    #runs for an additional 5 seconds which submits 
    while((t.second >=57)or(t.second < 2)):
        #driver.find_element_by_xpath(send_class).click()
        t=datetime.datetime.now()

#main driver
def getData(data:any):
    global driver 
    driver = webdriver.Chrome(chrome_options=options, executable_path=(r"C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"))

    #Opens up the my uw login page
    driver.get('https://sdb.admin.uw.edu/students/uwnetid/register.asp')

    #login with user and pass
    login(data[0],data[1])

    #add any SLN codes, add codes, or credits
    i =0
    while i <8:
        addSLN(data[i+2])
        addCodes(data[i+10])
        addCredit(data[i+18])
        i +=1

    #specify registration time remember to uncomment to method
    registerDate(7,0,0)
    
    

