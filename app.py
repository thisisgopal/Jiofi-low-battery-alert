from bs4 import BeautifulSoup
import requests
import time
import subprocess as sp


def scrap():
    web_page = requests.get('http://jiofi.local.html/')
    source_code = BeautifulSoup(web_page.content, 'html.parser')
    battery_level = (source_code.find(id="batterylevel")).get('value')
    battery_percentage = int(battery_level[0:2])
    alert = f"Jiofi's Battery is too low ( {battery_percentage}% ). So charge it !"
    if battery_percentage < 10:
        sp.call(['notify-send', alert])


while True:
    scrap()
    time.sleep(100)
