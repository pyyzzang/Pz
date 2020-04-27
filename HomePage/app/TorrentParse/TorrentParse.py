import os;
from selenium import webdriver
from time import sleep
import requests
from ..module.osDefine import osDefine;

class TorrentParse:
    def __init__(self):
        os.system("sudo killall -9 /usr/lib/chromium-browser/chromium-browser-v7");
        os.system("sudo killall -9 chromedriver");

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Background(CLI) 동작 사용
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9222")  # 이 부분이 핵심
        binary = "chromedriver"
        self.browser = "";
        self.browser = webdriver.Chrome(binary, chrome_options=chrome_options);

    def isEmpty(self):
        pass;
    def getUpdateList(self):
        pass;
