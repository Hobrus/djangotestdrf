import requests

session = requests.Session()

# Получение CSRF-токена
csrf_url = 'http://localhost:8000/csrf/'
csrf_response = session.get(csrf_url)
csrf_token = session.cookies.get('csrftoken')
print("CSRF Token:", csrf_token)

# Авторизация
url = 'http://localhost:8000/login/'
credentials = {
    'username': 'Hobrus',
    'password': '123321'
}
headers = {
    'X-CSRFToken': csrf_token
}
response = session.post(url, data=credentials, headers=headers)
print(response.status_code)
print(response.content)
print("Session ID:", session.cookies.get('sessionid'))
