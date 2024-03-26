import time

#from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options= chrome_options)

# Service_obj = Service(r"C:\Users\shiva\OneDrive\Desktop\Shivashish\Learning\Software\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(2)
url = "https://www.flipkart.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

wait = WebDriverWait(driver,10)     #waiting for Login window to appear on screen
cross = wait.until(E.visibility_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")))
cross.click()

driver.find_element(By.XPATH,"//input[@placeholder='Search for products, brands and more']").send_keys("IPHONE")
driver.find_element(By.CLASS_NAME,"L0Z3Pu").click()
#cross = wait.until(E.visibility_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")))
#cross.click()
#driver.find_element(By.CSS_SELECTOR, "._1_3w1N").click()

search_list = driver.find_elements(By.CLASS_NAME, "_2kHMtA")
print(len(search_list))
price=[]
for elements in search_list:
    #driver.find_elements(By.CLASS_NAME, "_1AtVbE col-12-12")
    price.append(elements.find_element(By.XPATH, "//div[@class=_30jeq3 _1_WHN1]").text)
print(price)


        #price_before_sale = price_before_sale.append(item_price.text)
# print(len(price_before_sale))
# print(price_before_sale)
