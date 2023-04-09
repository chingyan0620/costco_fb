from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from sub_program.get_data import get_commet

options = Options()
options.headless = True

firefox = webdriver.Firefox(options=options, executable_path="geckodriver")
firefox.get("https://www.facebook.com/groups/1260448967306807/")
time.sleep(2)

content = firefox.find_element(
    By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[\
        1]/div[4]/div/div/div[2]/div/div")

get_post_counter = 0
old_dict = {}
point = 0
while get_post_counter < 5:
    post_block = content.find_elements(
        By.CSS_SELECTOR, "div[class='x1yztbdb \
            x1n2onr6 xh8yej3 x1ja2u2z']")

    if point < len(post_block):
        i = post_block[point]
        point += 1
        try:
            if i.text.strip() != "":
                result = get_commet(i, firefox)
                if not old_dict:
                    old_dict = result
                    get_post_counter += 1
                    with open("./data/selenium_fb_costco.txt", "a") as f:
                        f.write(str(result) + "\n")
                else:
                    if old_dict["post_name"] == result["post_name"]:
                        continue
                    else:
                        old_dict = result
                        get_post_counter += 1
                        with open("./data/selenium_fb_costco.txt", "a") as f:
                            f.write(str(result) + "\n")
        except Exception as e:
            if i == post_block[-1]:
                firefox.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            else:
                pass
    else:
        firefox.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

firefox.quit()
