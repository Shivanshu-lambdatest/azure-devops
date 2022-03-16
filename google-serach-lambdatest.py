#!/usr/local/bin/python

import time
import os
import multiprocessing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib3
import sys
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options

build_name = os.getenv("LT_BUILD_NAME")

def call():
    desired_cap = {
        "browserName":"Chrome",
        "console": True,
        "build": build_name,
        "name" : "Test Shiv 3",
        "version":"latest",                   #88.0
        "headless":False,
        "network": False,
        "platformName": "Windows 10",
        "resolution":"1024x768",
        "video":True,
        "visual":True,
        "w3c":True
    }
    try:
        url = "https://shivanshus:EErB4HiGjznFLP2uXiDYlxTIXtuN9MQI5efwn7nZkDB8G2jVF3@hub.lambdatest.com/wd/hub"
        print(desired_cap)
        driver=webdriver.Remote(desired_capabilities=desired_cap,command_executor=url)
        print(driver.session_id)
        # driver.get("https://mylocation.org/")
        # driver.get("https://www.whatismybrowser.com/")
        driver.get("https://www.google.com/")
        driver.get("https://www.halowaypoint.com/en-us/games/halo-infinite")
        print("=============1===========")
        # driver.get("https://www.serverless.com/blog/cors-api-gateway-survival-guide")
        driver.get("https://en.wikipedia.org/wiki/Halo_Infinite")
        print("=============2===========")
        # driver.get("https://www.thrillophilia.com/best-mountain-trek-in-india")
        # driver.get("https://indiahikes.com/")
        driver.get("https://www.facebook.com/")
        print("=============3===========")
        driver.get("https://google.com/")
        start_time = time.time()
        driver.quit()
        print("quit time {0} secs".format((time.time()-start_time) % 60))
    except Exception as e: 
        print(e)
        driver.quit()

if __name__ == '__main__':
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=call)
        jobs.append(p)
        p.start()
