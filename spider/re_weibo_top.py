import requests
import re

"""
Author: Kelvin
Date: 2021-10-03

使用正则表达爬取微博热搜榜
"""

url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6&sudaref=www.google.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
cookie = 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhizyG9QTc9Ef9lFEoXISFj5JpX5KMhUgL.Fo-ESKBN1K.Xe052dJLoIEBLxK-LB.-LB--LxK-L1h-L1h.LxK-LBo5L12qLxKBLBo.L1-Bt; ALF=1664760047; SSOLoginState=1633224048; SCF=AjUyK3V8HfgvKMRoMwkHbh0cf3KmPNSTQovbZRY-1vCvcZHvv0zZzL-eodcMK2NRAIoFmMS9adgOkqhWG7J7XE8.; SUB=_2A25MXXUgDeRhGeNM7lYW-SfIyDyIHXVvK-HorDV8PUNbmtB-LWXlkW9NThtRLUt3Tbex-Oc1V9M-Uy9UNV_oUasE; WBStorage=6ff1c79b|undefined'
cookies = dict(cookies_are=cookie)


def getHtmlText(url, headers, cookies):
    """获取目标页面并转码为html

    Args:
        url (string): 目标URL
        headers (string): 请求头
        cookies (string): cookies 

    Returns:
        string: 解码后的html字符串
    """
    response = requests.get(url, headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    return response.text


def reFindall(regulation, html_text):
    """ 将匹配规则整个到函数内

    Args:
        regulation (string): 匹配规则
        html_text (string): 目标字符串

    Returns:
        List: 返回匹配内容列表
    """
    result = re.findall(regulation, html_text, re.DOTALL)
    return result


def main():
    """主函数

    Returns:
        tuple: 最终结果
    """
    html_text = getHtmlText(url, headers, cookies)
    keyword_regulation = '<td class="td-02">.*?<a.*?>(.*?)</a>'
    contents_keyword = reFindall(keyword_regulation, html_text)
    heat_regulation = '<td class="td-02">.*?<span>(.*?)</span>'
    contents_heat = reFindall(heat_regulation, html_text)
    rank_regulation = '<td class="td-01 ranktop">(.*?)</td>'
    contents_rank = reFindall(rank_regulation, html_text)
    content_tuple = tuple(zip(contents_rank, contents_keyword, contents_heat))
    return content_tuple


if __name__ == '__main__':
    contents = main()
    print('排名', '关键词', '热度')
    for content in contents:
        print(content[0], content[1], content[2])
