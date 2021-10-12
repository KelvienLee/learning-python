import requests
from datetime import datetime
from lxml import etree
from page_info import PageInfo

start_time = datetime.now()

"""
Author: Kelvin
Date: 2021-10-02

使用xPath爬取微博热搜
"""

pg = PageInfo()


def response():
    """发出请求获取数据
    Returns:
        String: 解析后的html文本数据
    """
    url = pg.url
    headers = pg.headers
    cookies = pg.cookies 
    r = requests.get(url, headers=headers, cookies=cookies)
    content = r.content.decode('utf-8','ignore')
    return etree.HTML(content)


# 数据获取方法一
# 定位表格后再进行数据遍历
def info_methods_1(content):
    """数据获取方法一
    Args:
        content (String): 传入html文本
    Returns:
        list: 数据列表
    """
    # 定位表格
    tr_tags= content.xpath('//tr[position()>1]')
    hots_result_1 = []
    for tr in tr_tags:
        eg = {}
        # 使用循环写入数据，故只取第一个结果再进行遍历
        rank = tr.xpath('.//td[position()<2]/text()')[0] 
        event = tr.xpath('.//a/text()')[0]
        hot = tr.xpath('.//span/text()')[0]
        eg = {
            "rank": rank,
            "content":event,
            "hot": hot
        }
        # 追加进数据列表
        hots_result_1.append(eg)
    return hots_result_1


# 数据获取方法二
# 直接取得表格内数据
def info_methods_2(content):
    """数据获取方法二
    Args:
        content (String): 传入html文本
    Returns:
        list: 数据列表
    """
    rank_2 = content.xpath('//tr[position()>1]//td[position()<2]/text()')  #class: list
    events_2 = content.xpath('//tr[position()>1]//a/text()')    #class: list
    hots_2 = content.xpath('//tr[position()>1]//span/text()')   #class: list
    hots_result_2 = []
    # 使用zip函数处理列表数据
    for rank, content,hot in zip(rank_2, events_2, hots_2):
        eg = {}
        eg = {  "rank": rank, 
                "content": content,
                "hot": hot
                }
        hots_result_2.append(eg)
    return hots_result_2


def main():
    """主函数"""
    content = response()

    # info_1 = info_methods_1(content)
    # print('方法一：')
    # print('序号', '关键词', '热度')
    # for info in info_1: 
    #     print(info['rank'], info['content'], info['hot'])

    info_2 = info_methods_2(content)
    print('方法二：')
    print('序号', '关键词', '热度')
    for info in info_2: 
        print(info['rank'], info['content'], info['hot'])
    
    return None


if __name__ == '__main__':
    main()
    end_time = datetime.now()
    print(end_time - start_time)
