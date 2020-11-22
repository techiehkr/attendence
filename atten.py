#arthur => techie
#need :- python3,selenium,xcode(browser extension)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
driver = webdriver.Chrome()

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

name = "" #your email
pwd = "" #ur pass
keys = "keys to put in zoom inbox" #your data

driver.get("https://accounts.google.com/login")

enter_email = driver.find_element_by_name(name="identifier")
enter_email.send_keys(name)

name_next = driver.find_element_by_class_name("VfPpkd-dgl2Hf-ppHlrf-sM5MNb")
name_next.click()
#wait for next operation
driver.implicitly_wait(5)


enter_pwd = driver.find_element_by_name(name="password")
enter_pwd.send_keys(pwd)

pwd_next= driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
pwd_next.click()


def choose():
    print("< press [1] for computer networks class >")
    print("< press [2] for java class >")
    print("< press [3] for maths class >")
    print("< press [4] for web technology class >")
    choose=int(input(">>> "))
    if (choose == 1):
        driver.get("https://meet.google.com/uai-dfab-mqt")
    elif (choose==2):
        driver.get("https://meet.google.com/tis-mvco-uta")
    elif (choose==3):
        driver.get("https://meet.google.com/gjc-mvun-iar")
    elif(choose==4):
        driver.get("https://meet.google.com/nfs-hoha-cet")
    else:
        print("unknown option selected")
choose()
driver.implicitly_wait(5)
dis = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span')
dis.click()


driver.implicitly_wait(5)
join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
join.click()

#driver.implicitly_wait(5)
#video_off = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div/div[1]')
#video_off.click()

driver.implicitly_wait(5)
chat = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span')
chat.click()

prasent = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea')
prasent.send_keys(keys)

driver.close()
#there is a problem we can't off alert with this idk if its work below code will work
#send = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span/svg/path')
#send.click()