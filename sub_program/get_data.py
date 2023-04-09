import time
from selenium.webdriver.common.by import By


def get_commet(selenium_element, driver):
    single_post = {}
    post_name = selenium_element.find_element(By.TAG_NAME, "h2")
    post = selenium_element.find_element(By.XPATH, ".//div/span/div/div")
    single_post.update({"post_name": post_name.text, "content": post.text})

    tmp_text = selenium_element.text
    if "先前的留言" in tmp_text or "先前的答案" in tmp_text:
        more_ele = selenium_element.find_element(
            By.XPATH, ".//div/div/div/div/div/div/div/div/div/div[2]/div/div/\
                div[4]/div/div/div[2]/div[2]/div[1]/div[2]")
        more_ele.click()
        time.sleep(2)

    all_comments = selenium_element.find_elements(By.TAG_NAME, "li")
    comments_list = []
    for i in range(len(all_comments)):
        comment = all_comments[i]
        try:
            user_block = comment.find_element(By.CSS_SELECTOR, ".x3nfvp2")
            user_name = user_block.text.split("\n")[0]
            user_comment = user_block.text.split("\n")[1]
            comments_list.append(
                {"comment_name": user_name, "message": user_comment})
        except:
            pass
    single_post.update({"comments": comments_list})

    return single_post
