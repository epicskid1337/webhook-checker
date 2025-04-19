import requests
from time import sleep

webhook = "https://discord.com/api/webhooks/xxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


data={
    "content": "@everyone Still up!",
    "username": "checker",
}

def check():


    response = requests.post(webhook, data)



    print(response)

check()

while True:
    sleep(140)
    check()

