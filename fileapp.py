import requests
import json
url='http://127.0.0.1:8000/stucreate/'

data={
    "name": "Hridoy",
      "age": 26, 
      "grade": 3.99
      }

json_data=json.dumps(data)
new_data=requests.post(url=url,data=json_data)

data=new_data.json()
print(data)
