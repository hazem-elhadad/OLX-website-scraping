import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
links_list=[]
driver.get('https://www.olx.com.eg/en/vehicles/cars-for-sale/')
sleep(20)
try:

    main_page = driver.find_element(By.XPATH, '/html/body/div/div/div/div/a/button')
    sleep(5)
    main_page.click()
    sleep(10)
    cars_key = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/header/div/div[3]/div/div/div[1]/div/div[1]/input')
    sleep(3)
    cars_key.click()
    cars_key.send_keys('سيارات للبيع')
    sleep(2)
    search_key = driver.find_element(By.XPATH, '/html/body/div[2]/div/header[1]/div/div[3]/div/div/div/button')
    sleep(1)
    search_key.click()
    sleep(30)
    liData = driver.find_elements(By.XPATH, "//div[@class='ee2b0479']/child::a")
    sleep(5)
    for element in liData:
        links_list.append(element.get_attribute('href'))
    counter = 0
    while True:
        try:
            next_button = driver.find_element(By.XPATH, "//div[@title='Next']")
            src = next_button.get_attribute("class")
            if src == "d02376f9 ":
                next_button.click()
                sleep(5)
                liData = driver.find_elements(By.XPATH, "//div[@class='ee2b0479']/child::a")
                sleep(5)
                for element in liData:
                    links_list.append(element.get_attribute('href'))
                counter += 1
            else:
                print("Congratulations You finished")
                driver.quit()
                break
        except:
            print("Congratulations You finished")
            df = pd.DataFrame(links_list)
            df.to_csv("ListodCarLinks.csv", index=False)
            driver.quit()
            break
        print(f"Our Page Now Is Page: {str(counter)}")
        print(f"You scrapped: {len(links_list)} Link")


# sleep(10)
# driver.quit()

except:
    counter = 0
    liData = driver.find_elements(By.XPATH, "//div[@class='ee2b0479']/child::a")
    sleep(5)
    for element in liData:
        links_list.append(element.get_attribute('href'))

    while True:
        try:
            next_button = driver.find_element(By.XPATH, "//div[@title='Next']")
            src = next_button.get_attribute("class")
            if src == "d02376f9 ":
                next_button.click()
                sleep(5)
                liData = driver.find_elements(By.XPATH, "//div[@class='ee2b0479']/child::a")
                sleep(5)
                for element in liData:
                    links_list.append(element.get_attribute('href'))
                counter += 1
            else:
                print("Congratulations You finished")
                driver.quit()
                break
        except:
            print("Congratulations You finished")
            df = pd.DataFrame(links_list)
            df.to_csv("ListodCarLinks.csv", index=False)
            driver.quit()
            break
        print(f"Our Page Now Is Page: {str(counter)}")
        print(f"You scrapped: {len(links_list)} Link")


    # sleep(10)
    # driver.quit()


