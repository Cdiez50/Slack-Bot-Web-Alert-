#!/bin/python3.6
#
# Dev : F00b4rch

import requests
import time
from slackclient import SlackClient

slack_token = "YOUR_TOKEN_HERE"
sc = SlackClient(slack_token)

urls=['site1', 'site2', 'site3']

while True :

    for i in urls :
        r = requests.head(i)
        t = requests.get(i, timeout=5).elapsed.total_seconds()
        # print(i, r.status_code, t)
        time.sleep(2)

        if r.status_code != 200 :
            sc.api_call(
            "chat.postMessage",
            channel="#infra",
            text=("ALERTE !", i, r.status_code)
            )

        if t > 2 :
            sc.api_call(
            "chat.postMessage",
            channel="#infra",
            text=("LoadSite too long : ", i, r.status_code)
            )

    time.sleep(10)
