import requests

# endpoint = "https://httpbin.org/get"
# print(get_response.status_code)
# print(get_response.headers)
# print(get_response.text)
# print(get_response.json())
endpoint = "http://127.0.0.1:8000/api/home"
get_response = requests.get(endpoint, json = {'message': "Hello World"})
print(get_response.json())
