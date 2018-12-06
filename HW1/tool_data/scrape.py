from selenium import webdriver
import time

def get_data(words):
    
    if len(words) > 10:
        return print("No man, you can put just 10 fuckin' words maximum")

    bs_url = "https://tools.wmflabs.org/pageviews/?project=it.wikipedia.org&platform=all-access&agent=user&range=all-time&pages="+"|".join(words)

    driver = webdriver.Chrome()
    driver.get(bs_url)
    
    time.sleep(10)
    
    first_click = driver.find_elements_by_tag_name("button")
    first_click[6].click()
    
    driver.find_element_by_class_name("download-csv").click()