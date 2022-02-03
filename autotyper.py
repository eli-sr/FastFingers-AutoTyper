#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

def random_errors():
    # Randoming typing errors
    if random.randint(1,10) <= 4:
        in_tar.send_keys("a")
        if random.randint(1,10) <= 2:
            in_tar.send_keys(" ")
        else:
            in_tar.send_keys(Keys.BACKSPACE)

# Setting user
username = 'imthabestt'

# Browsing to the web
web = webdriver.Firefox()
web.get('https://10ff.net/login')

sleep(1)

# Writing the user
in_un = web.find_element_by_xpath('//*[@id="username"]')
in_un.send_keys(username)
in_un.send_keys(Keys.RETURN)

sleep(2)

# Preparing to type
test = web.find_element_by_xpath('/html/body/div/div/div[2]/div')
print("[*] Waiting for the count down")
while test.text.isdigit():
    sleep(1)

# Giving advantage to the oponents haha
#sleep(20)
input("[Type any key to START]")

# Setting the word-target and the input-target
target = web.find_element_by_class_name('highlight')
in_tar = web.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/input')

x = 1 # Bigger = Faster
# Typing :)
while True:
    ##sleep(1/random.randint(1,x))
    ##random_errors()
    # Exp speed
    sleep(1/x)
    x = x * 2
    # Typing the correct word
    in_tar.send_keys(target.text)
    in_tar.send_keys(" ")
    try:
        target = web.find_element_by_class_name('highlight')
    except:
        print("FINSHED!!!")
        break

