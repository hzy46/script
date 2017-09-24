import requests

username = 'your urp id'
password = 'your urp password'
ip = 'your ip'
url = 'https://10.108.255.249/include/auth_action.php'

r = requests.post(
    url,
    data={
        'action': 'login',
        'username': username,
        'password': password,
        'ac_id': 1,
        'user_ip': ip,
        'nas_ip': "",
        'user_mac': "",
        'save_me': 1,
        'ajax': 1
    },
    headers={
        'Host': '10.108.255.249',
        'Origin': 'http://10.108.255.249',
        'Referer': 'http://10.108.255.249/srun_portal_pc.php?ac_id=1&&phone=1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    }
)

print(r.text)

assert r.status_code == 200
