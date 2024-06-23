import requests

proxy = {
    'http': 'http://167.88.175.18:34567',
    'https': 'http://167.88.175.18:34567'
}

try:
    response = requests.get("https://ipinfo.io", proxies=proxy)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
