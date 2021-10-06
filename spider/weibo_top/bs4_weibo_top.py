import requests
from bs4 import BeautifulSoup
from datetime import datetime
from page_info import PageInfo

start_time = datetime.now()

"""
Author: Kelvin
Date: 2021-10-06

使用BeautifulSoup4配合lxml解析器爬取微博热搜
"""

pg = PageInfo()


def get_html_text():
    """获取目标页面并转码为html

    Returns:
        String: 解码后的html字符串
    """
    url = pg.url
    headers = pg.headers
    cookies = pg.cookies
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.text


def parse_contents(text):
    """ 1.在html文档中查找结果
        2.将查找结果写入列表
        3.将各个结果压缩为一个列表

    Args:
        text (String): 被匹配的html字符串

    Returns:
        List: 最终结果
    """
    soup = BeautifulSoup(text, 'lxml')
    keyword_list_pro = soup.find_all(class_='td-02')
    rank_list_pro = soup.find_all(class_='td-01 ranktop')
    rank_list = []
    keyword_list = []
    heat_list = []
    for keyword in keyword_list_pro:
        if keyword.span == None:
            continue
        keyword_list.append(keyword.a.get_text())
        heat_list.append(keyword.span.get_text())
    for rank in rank_list_pro:
        rank_list.append(rank.get_text())
    return list(zip(rank_list, keyword_list, heat_list))


def main():
    """主函数

    Returns:
        None
    """
    print('序号', '关键词', '热度')
    html_text = get_html_text()
    result = parse_contents(html_text)
    for _ in result:
        print(_[0], _[1], _[2])
    return None



if __name__ == '__main__':
    main()
    end_time = datetime.now()
    print(end_time - start_time)