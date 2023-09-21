import requests

url = 'http://localhost:5000/courses'

data = {
    'title': 'C#',
    'description': 'C# is a programming language',
    'done': False,
    'price': 100
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())