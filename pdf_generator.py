import  requests

web_page_url = "https://metanit.com/dart/tutorial/"

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

response = requests.get(url=web_page_url, headers=headers)

page_content = response.text
# print(page_content)

with open('./google.html', 'w', encoding='utf8') as fp:
        fp.write(page_content)