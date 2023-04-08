import datetime
import time
import selenium
from selenium.webdriver.common.by import By

def get_commet(selenium_element,driver):
    single_post = {}
    tmp_text = selenium_element.text
    if "先前的留言" in tmp_text or "先前的答案" in tmp_text:
        print("======= in post  =======")
        # more_ele = selenium_element.find_element(By.XPATH,".//span[contains(., '先前的留言')]")
        post_name = selenium_element.find_element(By.TAG_NAME,"h2")
        print("======  post_name  =====")
        print(post_name.text)
        post = selenium_element.find_element(By.XPATH,".//div/span/div/div")
        # post = selenium_element.find_element(By.CSS_SELECTOR,".x78zum5.xdt5ytf.xz62fqu.x16ldp7u")
        single_post.update({"post_name": post_name.text,"content":post})
        
        print("======  post  =====")
        print(post.text)

        more_ele = selenium_element.find_element(By.XPATH,".//div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]")

        more_ele.click()
        time.sleep(2)
        all_comments = selenium_element.find_elements(By.TAG_NAME,"li")
        # print(all_comments[0].text)
        print("======= in comment  =======")
        comments_list =[]

        for i in range(len(all_comments)):

            comment = all_comments[i]
            try:
                user_block = comment.find_element(By.CSS_SELECTOR,".x3nfvp2")
                user_name = user_block.text.split("\n")[0]
                user_comment = user_block.text.split("\n")[1]
                print("user_block")
                print(user_name)
                print("comment_user_name")
                # comment_user_name = user_block.find_element(By.CSS_SELECTOR,".x11i5rnm").text
                print(user_comment)
                comments_list.append({"comment_name":user_name,"message":user_comment})
                
            except:
                print(" === with error  ===")
                # print(comment.text)
        single_post.update({"comments":comments_list})


    else:
        print("in short post ~")
        all_comments = selenium_element.find_elements(By.XPATH,".//div/span/div")
        print(all_comments[0].text)
        
        for comment in all_comments:
            print(comment.text)

    return single_post


