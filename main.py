from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from sub_program.get_data import get_commet

options = Options()
options.headless = True

 
firefox = webdriver.Firefox(options=options,executable_path="geckodriver")
firefox.get("https://www.facebook.com/groups/1260448967306807/")
time.sleep(2)

content = firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div")


get_post_counter = 0
while get_post_counter < 5:
    post_block = content.find_elements(By.XPATH,"./div/div[2]/div[2]/*")
    for i in post_block:
        print("--------")
        try:
            if i.text.strip() != "" :
                result = get_commet(i,firefox)
                get_post_counter += 1
            with open("./data/selenium_fb_costco.txt","a") as f:
                f.write(str(result) +"\n")
        except Exception as e:
            # print(e)
            # print("element remove!!")
            # scroll page and recatch element
            firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
    
firefox.quit()

