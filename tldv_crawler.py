from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv

username = "sunkid"
password = "ccnnts"

start_page = 2
end_page = 100

driver = webdriver.Chrome()

driver.get("https://tldv.io/app/meetings/676a401350559700133a1707/?transcript=true&video=true")
# driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
try:
    print("in try")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-profile"))
    )
    elements = driver.find_elements(By.CLASS_NAME, "cursor-pointer.text-base-600.font-semibold.block.select-none")
    for element in elements:
        print(element.text)
    print("in intry 2")

    #
    # driver.find_element(By.NAME, 'login').send_keys(username)
    # driver.find_element(By.NAME, 'password').send_keys(password)
    # driver.find_element(By.CLASS_NAME, 'button--icon--login').submit()
    # print("Ok")
    #
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "p-navgroup-link--user"))
    # )
    #
    # src_list = []
    # for i in range (start_page, end_page):
    #     driver.get("" + str(i))
    #     elements = driver.find_elements(By.CLASS_NAME, "bbImage")
    #     # elements = driver.find_elements(By.CLASS_NAME, "file-preview")
    #     for element in elements:
    #         src = element.get_attribute("src")
    #         print(src)
    #         # src_list.append(src)
    #
    #         # src = element.get_attribute("href")
    #         if "cdn" in src:
    #         # if "attachments" in src:
    #             # url = "" + src
    #             src_list.append(src)

    # with open("data/page-" + str(start_page) + "-" + str(end_page) + ".csv", 'w') as csvfile:
    # with open("data/threads-2726-" + str(start_page) + "-" + str(end_page) + ".csv", 'w') as csvfile:
    #     # creating a csv writer object
    #     csvwriter = csv.writer(csvfile)
    #     for item in src_list:
    #         csvwriter.writerow([item])

finally:
    print("Finally")
    driver.quit()



