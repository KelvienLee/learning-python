import requests, re, html
from lxml import etree


class GetWordInfo(object):
    def __init__(self):
        self.search_word = input('查词：')
        self.url = f'https://cn.bing.com/dict/search?q={self.search_word}'

    def get_html(self,url):
        response = requests.get(url=self.url)
        response.encoding = 'utf-8'
        content = response.content.decode('utf-8')
        html_content = etree.HTML(content)
        text_pro = response.text
        text = html.unescape(text_pro)
        return html_content, text

    def get_word(self):
        html_content = self.get_html(self.url)[0]
        text = self.get_html(self.url)[1]
        # str: 顶部提示，如果存在则返回提示字符串，不存在则输出空字符串
        is_top_tip_exists = re.findall('<div class="in_tip b_fpage">(.*?)</div>', text, re.DOTALL)
        if not is_top_tip_exists:
            top_tip = ''
        else: 
            top_tip = is_top_tip_exists[0]
        # str: 单词，主键
        word = re.findall('<h1.*?<strong>(.*?)</strong>', text, re.DOTALL)[0]
        # str: 音标
        us_soundmark = re.findall('<div class="hd_prUS b_primtxt">美(.*?)</div>', text, re.DOTALL)[0].strip().replace('[', '').replace(']', '')
        uk_soundmark = re.findall('<div class="hd_pr b_primtxt">英(.*?)</div>', text, re.DOTALL)[0].strip().replace('[', '').replace(']', '')
        # str: 发音音频
        us_sounds = re.findall('<a class="bigaud".*?https://(.*?).mp3.*?</a>', text, re.DOTALL)[0]
        uk_sounds = re.findall('<a class="bigaud".*?https://(.*?).mp3.*?</a>', text, re.DOTALL)[1]
        # list: 单词释义列表
        info_list_pro = re.findall('<div class="hd_area">.*?</div>.*?(<li>.*?</li>)</ul>', text, re.DOTALL)[0]
        info_list = re.findall('<li>.*?<span class="pos[ web]*">(.*?)</span>.*?<span>(.*?)</span>.*?</li>', info_list_pro, re.DOTALL)
        # list: 单词变体列表
        if not re.search('<div class="hd_if">', text, re.DOTALL) == None:
            tense_div = re.findall('<div class="hd_if">.*?</div>', text, re.DOTALL)[0]
            tense_list = re.findall('<span class="b_primtxt">(.*?)</span>.*?<a class="p1-5" .*?>(.*?)</a>', tense_div, re.DOTALL)
        else: tense_list = []
        # 例句
        # list: 英语例句
        example_en_list_pro = html_content.xpath('//div[@class="se_li"][position()<4]')
        example_en_list = []
        i = 1
        for _ in example_en_list_pro:
            r1 = _.xpath('.//div[@class="sen_en b_regtxt"]//text()')
            r2 = ''.join(r1)
            r3 = f'<span class="list">{i}. </span>' + r2
            example_en_list.append(r3)
            i += 1
        # list: 中文例句
        example_zh_list_pro = html_content.xpath('//div[@class="se_li"][position()<4]')
        example_zh_list = []
        for _ in example_zh_list_pro:
            r1 = _.xpath('.//div[@class="sen_cn b_regtxt"]//text()')
            r2 = ''.join(r1)
            example_zh_list.append(r2)
        # list: 使用zip合并为一个新列表
        example_list = list(zip(example_en_list, example_zh_list))
        # 短语搭配
        # list: 搭配类别提示
        collocation_title_list_pro = html_content.xpath('//div[@id="colid"]/div[@class="df_div2"]/div[@class="de_title2 b_dictHighlight"]//text()')
        collocation_title_list = []
        for _ in collocation_title_list_pro:
            collocation_title_list.append(_)
        # list: 搭配具体内容
        collocation_content_list_pro = html_content.xpath('//div[@id="colid"]/div[@class="df_div2"]/div[@class="col_fl"]')
        collocation_content_list = []
        for _ in collocation_content_list_pro:
            r1 = _.xpath('.//a/span/text()')
            r2 = ', '.join(r1)
            collocation_content_list.append(r2)
        # list: 使用zip合并为一个列表
        collocation = list(zip(collocation_title_list,collocation_content_list))
        # str: 主要释义部分组接字符串
        main_info = ''
        for _ in info_list:
            r = "<div class='info'>" + "<span class='title'>" + _[0] + '</span>' + "<span class='content'>" + _[1] + '</span>' + '</div>'
            main_info += r
        # str: tense组接字符串
        tense = ''
        for _ in tense_list:
            r = "<div class='tense'>" + "<span class='title'>" + _[0] + '</span>' + "<span class='content'>" + _[1] + '</span></div>'
            tense += r
        # str: collocation_result组接字符串
        colllocation_result = ''
        for _ in collocation:
            r = "<div class='col'>" + "<span class='title'>" + _[0] + '</span>' + "<span class='content'>" + _[1] + '</span>' + '</div>'
            colllocation_result += r
        # str: 例句字符串组接
        example = ''
        for _ in example_list:
            r = "<div class='en'>" + _[0] + "</div><div class='zh'>" + _[1] + '</div>'
            example += r
        # str: 容错处理，如果例句中有英文双引号则替换为单引号
        new_example = example.replace('"', '\'')
        # str: 最终数据输出组接
        data = f"""[["{word}","{us_soundmark}","{uk_soundmark}","{us_sounds}","{uk_sounds}","{main_info}","{tense}","{colllocation_result}","{new_example}"],""]"""
        print(data)
        return data

if __name__ == '__main__':
    t = GetWordInfo()
    t.get_word()