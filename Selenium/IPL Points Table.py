from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Adding Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")

#Invoking browser
service_obj = Service(r"D:\Shivashish\Learning\Software\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options = chrome_options)


driver.get("https://www.iplt20.com/points-table/men")
print(driver.current_url)
print(driver.title)

#Choose Year from the Years Dropdown
ipl_years_list = driver.find_elements(By.XPATH,"//div[@class='col-lg-2 col-md-2 col-sm-3'][2]/div/div[2]/div")

for years in ipl_years_list:
    print("IPL {} held successfully".format(years.text))

# #Print all Teams Participated
teams_ipl_2024 = driver.find_elements(By.XPATH, "//table/tbody[2]/tr/td[3]/div/h2")
for team in teams_ipl_2024:
    print("Team {} Partificated in 2024".format(team.text))

driver.get("https://www.iplt20.com/")
action = ActionChains(driver)
action.move_to_element(By.XPATH,"(//div[@class='row'])[3]/div/div[2]/a")
print(driver.find_element(By.XPATH,"(//div[@class='row'])[3]/div/div[2]/a").text)
