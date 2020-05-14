from bs4 import BeautifulSoup
import requests
import time
import subprocess as sp
# Gopal Narayanan - 14.05.2020 @ 5.45 PM - gopalnarayanantn@gmail.com
# Jiofi product ID - JMR1040 ( Mine )


def scrap():
    web_page = requests.get('http://jiofi.local.html/')
    source_code = BeautifulSoup(web_page.content, 'html.parser')
    battery_level = (source_code.find(id="batterylevel")).get('value')
    battery_percentage = int(battery_level[:-1])
    alert = f"Jiofi's Battery is too low ( {battery_percentage}% ). So charge it !"
    if battery_percentage < 10:
        sp.call(['notify-send', alert])


while True:
    scrap() 
    time.sleep(60)
