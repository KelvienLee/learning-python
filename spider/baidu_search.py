import requests
from lxml import etree


url = 'https://www.baidu.com'
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"}


re = requests.get(url, headers=headers)
content = re.content.decode("utf-8")
html = etree.HTML(content)


contents = html.xpath("//div[@id='bottom_layer']/div/p/a/text()")
urls = html.xpath("//div[@id='bottom_layer']/div/p/a/@href")
url_tuple = dict(zip(contents, urls))
print(url_tuple)
