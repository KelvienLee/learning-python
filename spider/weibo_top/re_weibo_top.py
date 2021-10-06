import requests
import re
from datetime import datetime
from page_info import PageInfo

start_time = datetime.now()

"""
Author: Kelvin
Date: 2021-10-03

使用正则表达爬取微博热搜榜
"""

pg = PageInfo()


def getHtmlText():
    """获取目标页面并转码为html

    Returns:
        string: 解码后的html字符串
    """
    url = pg.url
    headers = pg.headers
    cookies = pg.cookies
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
    html_text = getHtmlText()
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
    end_time = datetime.now()
    print(end_time - start_time)
