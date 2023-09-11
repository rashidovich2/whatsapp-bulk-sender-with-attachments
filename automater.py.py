from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****     This tool was built by Anirudh  		   ******")
print("*****     Modified by Mohammed Althaf H			   ******")
print("*****  https://github.com/mohammed-althaf-h         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

with open("message.txt", "r") as f:
    message = f.read()
print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)


numbers = []
with open("numbers.txt", "r") as f:
    numbers.extend(
        line.strip() for line in f.read().splitlines() if line.strip() != ""
    )
total_number=len(numbers)
print(f'{style.RED}We found {total_number} numbers in the file{style.RESET}')
delay = 30
filename=input("Enter the file name exactly: ")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
sleep(10)
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
    	continue
    print(
        f'{style.YELLOW}{idx + 1}/{total_number} => Sending message to {number}.{style.RESET}'
    )
    try:
        url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(f"{style.RED}\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print(f"If there is an alert, please dismiss it.{style.RESET}")
                else:
                    sleep(30)
                    click_btn.click()
                    sleep(2)
                    filen=(f"Give the path name here/{filename}")#path name where file is stored Eg: "C:/Users/Desktop/bot/
                    driver.find_element_by_css_selector('span[data-icon="clip"]').click()
                    attach=driver.find_element_by_css_selector('input[type="file"]')
                    attach.send_keys(filen)
                    send=driver.find_element_by_class_name('_2QbRL')
                    sleep(5)
                    go=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span")
                    go.click()
                    sleep(1)
                    sent=True
                    sleep(5)
                    result = print(f'{style.GREEN}Message sent to: {number}{style.RESET}')
    except Exception as e:
        print(f'{style.RED}Failed to send message to {number}{str(e)}{style.RESET}')
driver.close()