# Make sure chromedriver.exe is present in your root directory(check requirements.txt)
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Built-In Library time
from time import sleep

# User Credentials stored in local variables(notice here there's no database connected so your data is safe)
username_input = input("Username/email: ")
password_input = input("Password: ")

# Input the receiver's Username/Name
recipient_input = input("Receiver: ")

# Input the desired message you would like to send
message_input = input("Message: ")

# Open Chrome Window
driver = webdriver.Chrome()
driver.maximize_window()

# Go to Instagram Website
driver.get("https://www.instagram.com")
sleep(5)

# Auto-fills Username
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.clear()
username.send_keys(username_input)

# Auto-fills Password
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.clear()
password.send_keys(password_input)

#Auto-clicks Log In
submit = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
submit.click()
sleep(7)

# Ensures your info is not cached on the browser
info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
info.click()
sleep(3)

# Ignores Desktop Notifications
notif = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notif.click()
sleep(3)

# Searches up the person whom you want to send the message
search = driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search[0].send_keys(recipient_input)
sleep(2)

# Clicks the first result
result = driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
result[0].click()
sleep(1)

# Auto-Clicks the Message Button
message_btn = driver.find_elements_by_tag_name('button')
message_btn[0].click()
sleep(2)

# And Finally Auto-fills in your message and sends it
message = driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
message[0].send_keys(message_input)
message[0].send_keys(Keys.RETURN)
