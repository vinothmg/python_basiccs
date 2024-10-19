import requests
import json


city_name = input("Enter The City Name: ")
api_key = 'd991b9641606f00fea6163a7cf5a2dcc'  


api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'


get_server_info = requests.get(api_url)


data = get_server_info.json()

if get_server_info.status_code == 200:
    print(json.dumps(data, indent=3))  
else:
    print(f"Error {data['cod']}: {data['message']}")

 
