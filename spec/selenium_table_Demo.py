from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

def find_data_from_dynamic_table(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    Arrival = {}

    try:
        sleep(5)
        table = driver.find_element(By.XPATH, "(//div[@class='row cnt-schedule-table'])[1]")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            ArrivalList = []
            cloumns = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text for col in cloumns]
            ArrivalList.extend(row_data)
            key = ArrivalList[2]
            value = ArrivalList[5] if ArrivalList[5]!='' else 'Data Not Available'
            Arrival[key]=value

    except Exception as e:
        print(f"The Exception occured is - {e}")

    # Close the Browser
    driver.quit()

    cities = ["Banglore", "Delhi", "Goa", "Dubai"]
    for x in Arrival.keys():
        if x in cities:
            print(f"{Arrival}")

url = "https://www.flightradar24.com/data/airports/pnq"
find_data_from_dynamic_table(url)
