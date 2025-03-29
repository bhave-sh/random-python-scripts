#Web Scraping

#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options


#pip3 install geckodriver-autoinstaller
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()


# pip3 install requests
import requests
URL = "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html"


# pip3 install urllib.parse
import urllib.parse

"""
Extracts element from URL
"""
opts = Options()
opts.headless = True
# assert opts.headless # Operating in headless mode
driver = webdriver.Firefox(options=opts)
# driver = webdriver.Firefox()
driver.get(URL)
element = driver.find_element_by_xpath("/html/body/main/div[1]/div[6]")
paragraph = str(element.text).split('\n')
result = []
for i in paragraph:
    if "#" in i or ":" in i:
        result.append(i)
driver.quit()


my_token = ""
chat_id = ""

def send_telegram_message(msg, chat_id=chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    """
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    # print(send_text)
    response = requests.get(send_text)
    return response.json()
pass

send_telegram_message(urllib.parse.quote('\n'.join(result)))


