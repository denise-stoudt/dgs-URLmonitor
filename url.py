# Assumes requests module is installed. Can be installed via pip: <pip install requests>
import requests
from time import sleep

url = "https://google.com/"

response = requests.get(url)
while response != []:
    if response.status_code == 200:
        print(response.status_code)
        print("Attempt to fetch google.com: Success!")
        print("Time to Response:")
        print(response.elapsed)
    else: 
        print(response.status_code)
        print("Attempt to fetch google.com: Unsucessful")
    sleep (60)
