import requests


url = 'https://www.instagram.com/accounts/login/'
url_main = url + 'ajax/'
auth = {'username': 'login', 'password': 'pass'}
headers = {'referer': "https://www.instagram.com/accounts/login/"}



with requests.Session() as s:
    req = s.get(url)
    headers['x-csrftoken'] = req.cookies['csrftoken']
    s.post(url_main, data=auth, headers=headers)
    # Now, you can use 's' object to 'get' response from any instagram url
    # as a logged in user.
    r = s.get('https://www.instagram.com/accounts/edit/')
    # If you want to check whether you're getting the correct response,
    # you can use this:
    print(auth['username'] in r.text)  # which returns 'True'