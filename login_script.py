import requests

username = 'your urp id'
password = 'your urp password'
url = 'http://10.108.255.249/cgi-bin/do_login'

r = requests.post(
    url,
    data={
        'username': username,
        'password': '{TEXT}' + password,
        'drop': 0,
        'type': 1,
        'n': 100
    },
    headers={
        'Host': '10.108.255.249',
        'Origin': 'http://10.108.255.249',
        'Referer': 'http://10.108.255.249/index.html?url=about:startpage',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    }
)

print(r.text)

assert r.status_code == 200
