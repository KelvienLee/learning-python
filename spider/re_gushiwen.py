import requests
import re
import os
from datetime import datetime


def getHtmlText(url):
    """发出请求获得响应并解码为html

    Args:
        url (String): 目标页面URL

    Returns:
        String: 解码后的html内容
    """
    response = requests.get(url)
    return response.text


def reFindAll(regulation, contents):
    """正则表达式匹配

    Args:
        regulation (string): 匹配规则
        contents (string): 待匹配文本

    Returns:
        List: 匹配结果
    """
    result_list = re.findall(regulation, contents, re.DOTALL)
    return result_list


def getPoemContent(htmlContent):
    """匹配出诗词

    Args:
        htmlContent (String): 传入的HTML文档

    Returns:
        List: [ 符合要求并经过处理的结果列表]
    """
    poetryTitleRegulation = '<div class="yizhu">.*?<b>(.*?)</b>'
    poetryTitleList = reFindAll(poetryTitleRegulation, htmlContent)
    poetryContentRegulation = '<div class="contson".*?>(.*?)</div>'
    poetryContentListPro = reFindAll(poetryContentRegulation, htmlContent)
    poetryContentList = []
    for poem in poetryContentListPro:
        poetryContent01 = re.sub('<.*?>', '', poem).strip()
        poetryContent = re.sub('。', '。\n', poetryContent01 )
        poetryContentList.append(poetryContent)
    return list(zip(poetryTitleList, poetryContentList))


def downToLocal(poetryList, path):
    """下载诗词保存到本地txt

    Args:
        poetryList (List): 诗词列表
        path (String): 保存路径

    Returns:
        None
    """
    for content in poetryList:
        with open(f'{path}' f'{content[0]}.txt', 'w', encoding='utf-8') as file:
            file.writelines('\n'.join(content))
    return None


def main():
    """主函数,提取时间作为创建文件夹的规则

    Returns:
        None
    """
    time_now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    root_path = os.getcwd()
    path = os.path.join(root_path, f'{time_now}{os.sep}')
    os.mkdir(path)

    for i in range(1,5):
        urls = f'https://www.gushiwen.cn/default_{i}.aspx'
        htmlContent = getHtmlText(urls)
        contentTuple = getPoemContent(htmlContent)
        downToLocal(contentTuple,path=path)
        print(f'第{i}页写入完成')
    return None


if __name__ == '__main__':
    main()
    print('done')
        