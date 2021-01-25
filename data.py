import requests
import time
import psycopg2

url = "https://www.noon.com/_svc/catalog/api/search"
page_number=1
payload="{\"brand\":[\"apple\"],\"category\":[\"electronics-and-mobiles/mobiles-and-accessories/mobiles-20905\"],\"filterKey\":[],\"f\":{},\"sort\":{\"by\":\"popularity\",\"dir\":\"desc\"},\"limit\":50,\"page\":2}"
headers = {
  'authority': 'www.noon.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
  'x-locale': 'en-eg',
  'x-content': 'mobile',
  'x-mp': 'noon',
  'x-platform': 'web',
  'x-cms': 'v2',
  'content-type': 'application/json',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'origin': 'https://www.noon.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/apple',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
}


lists=[]
payload={"brand":[],"category":["electronics-and-mobiles"],"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":page_number}
response = requests.request("POST", url, headers=headers, json=payload)
if(response.status_code==429):
    time.sleep(5)
else:
    response=response.json()
    v=response.get('hits')
for l in response['navPills']:
    p=l['code']
    print(p)
