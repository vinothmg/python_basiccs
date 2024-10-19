"""
import requests

response = requests.get("http://api.stackexchage.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

print("Response Status Code:", response.status_code)
print("Response Text:", response.text) 


if response.status_code == 200:
    data = response.json()
    for item in data['items']:
        print(item)
else:
    print(f"Request failed with status code: {response.status_code}")
    """
    
import requests
from time import sleep

url = "http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
retries = 5

for i in range(retries):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data=response.json()
        break 
    except requests.exceptions.RequestException as e:
        print(f"Attempt {i + 1} failed: {e}")
        sleep(1) 
else:
    print("All attempts failed.")
    