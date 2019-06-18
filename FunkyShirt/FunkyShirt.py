import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

print("FunkyShirt\n")

sleep_duration = 0.5

driver = webdriver.Chrome()
driver.get("https://secure2.e-konsulat.gov.pl")

time.sleep(sleep_duration)
# first page

# now we have to find to selectors.. to enter country
# and to enter place inside this country
kraj_id = "tresc_cbListaKrajow"
try:
  country_list = driver.find_element_by_id(kraj_id);
except NoSuchElementException:
  print("kraj_id is not found")


# Now we have select country.. in our case it will be
# INDIA
all_options = country_list.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s, text: %s " % (option.get_attribute("value"), option.text))
    # Click two time to invoke onChange event
    if(option.text == "INDIE"):
        option.click()
        break



# After that we should select place inside country, but before we proceed 
# we should wait for a moment to options get updated.
time.sleep(4*sleep_duration) # pause for 2 seconds

# find selector of places
place_id = "tresc_cbListaPlacowek"
try:
    place_list = driver.find_element_by_id(place_id);
except NoSuchElementException:
    print("place_id is not found")

# find all options
all_options = place_list.find_elements_by_tag_name("option")

# and if place_list is still empty loop until they will not, at least n'th times
n = 5
while len(all_options) == 0 and n > 0:
    time.sleep(sleep_duration) # pause for 2 seconds
    all_options = place_list.find_elements_by_tag_name("option")
    n = n - 1

for option in all_options:
    print("Value is: %s, text: %s " % (option.get_attribute("value"), option.text))
    if(option.text == "New Delhi"):
        option.click()





time.sleep(10)
all_hyperlinks = driver.find_elements_by_tag_name("a")
for hyperlink in all_hyperlinks:
    print("text: %s " % hyperlink.text)
    if(hyperlink.text == "Wiza krajowa - Zarejestruj formularz"):
        hyperlink.click()
        break


time.sleep(100)

driver.close()
driver.quit()
