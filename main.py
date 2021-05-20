from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'

headers = {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.instagram.com/',
    'Cookie': '',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers'
}



session = requests.Session()
session.headers.update(headers)
responce = session.get(BASE_URL)
soup = BeautifulSoup(responce.content, "html.parser")
csrf = responce.cookies['csrftoken']
session.headers.update({'X-CSRFToken': csrf})

data = {'username': "login", 'password': "pass"}

login = session.post(LOGIN_URL, data=data, allow_redirects=True)
print(login)