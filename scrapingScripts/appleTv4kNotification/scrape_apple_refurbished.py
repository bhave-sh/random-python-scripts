#Web Scraping

#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options


#pip3 install geckodriver-autoinstaller
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()

import requests

# URL = "https://www.apple.com/shop/refurbished/appletv"
URL = "https://www.apple.com/shop/product/FQD22LL/A/Refurbished-Apple-TV-4K-32GB"

"""
Extracts element from URL
"""
opts = Options()
opts.headless = True
# assert opts.headless # Operating in headless mode
driver = webdriver.Firefox(options=opts)
# driver = webdriver.Firefox()
driver.get(URL)
# element = driver.find_element_by_id("fs-grid.filters.dimensions.0-refurbClearModel-appletv4k").get_attribute('class')
element = driver.find_element_by_name("add-to-cart").get_attribute('class')
driver.quit()

my_token = "1205161681:AAHhCNw8IhHSVTFDZOIee0HXyhKuU-1w94U"
chat_id = "713241830"

def send_telegram_message(msg, chat_id=chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    """
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return response.json()
pass

# if element.strip() == "":
if 'disabled' not in element.lower():
    send_telegram_message("Now Available - Apple TV 4k 32 GB Refurbished !!")
else:
    send_telegram_message("Apple TV 4k 32 GB - Still not available")
pass
