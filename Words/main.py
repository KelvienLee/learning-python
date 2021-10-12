import requests, re
from lxml import etree


search_word = 'access'
URL = f'https://cn.bing.com/dict/search?q={search_word}'


def get_html(url):
    response = requests.get(url)
    content = response.content.decode('utf-8')
    html = etree.HTML(content)
    text = response.text
    return html, text


if __name__ == '__main__':
    html = get_html(URL)[0]
    text = get_html(URL)[1]

    word = re.findall('<h1.*?<strong>(.*?)</strong>', text, re.DOTALL)[0]
    us_soundmark = re.findall('<div class="hd_prUS b_primtxt">.*?;(.*?)</div>', text, re.DOTALL)[0]
    uk_soundmark = re.findall('<div class="hd_pr b_primtxt">.*?;(.*?)</div>', text, re.DOTALL)[0]
    us_sounds = re.findall('<a class="bigaud".*?(https://.*?.mp3).*?</a>', text, re.DOTALL)[0]
    uk_sounds = re.findall('<a class="bigaud".*?(https://.*?.mp3).*?</a>', text, re.DOTALL)[1]
    info_list_pro = re.findall('<div class="hd_area">.*?</div>.*?(<li>.*?</li>)</ul>', text, re.DOTALL)[0]
    info_list = re.findall('<li>.*?<span class="pos[ web]*">(.*?)</span>.*?<span>(.*?)</span>.*?</li>', info_list_pro, re.DOTALL)

    if not re.search('<div class="hd_if">', text, re.DOTALL) == None:
        tense_div = re.findall('<div class="hd_if">.*?</div>', text, re.DOTALL)[0]
        tense_list = re.findall('<span class="b_primtxt">(.*?)</span>.*?<a class="p1-5" .*?>(.*?)</a>', tense_div, re.DOTALL)
    else: tense_list = []

    example_en_list_01 = html.xpath('//div[@class="se_li"][position()<2]/div[@class="se_li1"]/div[@class="sen_en b_regtxt"]//text()')
    example_zh_list_01 = html.xpath('//div[@class="se_li"][position()<2]/div[@class="se_li1"]/div[@class="sen_cn b_regtxt"]//text()')
    example_en_01 = ''.join(example_en_list_01)
    example_zh_01 = ''.join(example_zh_list_01)
        
    example_en_list_02 = html.xpath('//div[@class="se_li"][position()>1][position()<3]/div[@class="se_li1"]/div[@class="sen_en b_regtxt"]//text()')
    example_zh_list_02 = html.xpath('//div[@class="se_li"][position()>1][position()<3]/div[@class="se_li1"]/div[@class="sen_cn b_regtxt"]//text()')
    example_en_02 = ''.join(example_en_list_02)
    example_zh_02 = ''.join(example_zh_list_02)

    example_en_list_03 = html.xpath('//div[@class="se_li"][position()>2][position()<4]/div[@class="se_li1"]/div[@class="sen_en b_regtxt"]//text()')
    example_zh_list_03 = html.xpath('//div[@class="se_li"][position()>2][position()<4]/div[@class="se_li1"]/div[@class="sen_cn b_regtxt"]//text()')
    example_en_03 = ''.join(example_en_list_03)
    example_zh_03 = ''.join(example_zh_list_03)

    # 搭配
    collocation_title_list_pro = html.xpath('//div[@id="colid"]/div[@class="df_div2"]/div[@class="de_title2 b_dictHighlight"]//text()')
    collocation_title_list = []
    for _ in collocation_title_list_pro:
        collocation_title_list.append(_)

    collocation_content_list_pro = html.xpath('//div[@id="colid"]/div[@class="df_div2"]/div[@class="col_fl"]')
    collocation_content_list = []
    for _ in collocation_content_list_pro:
        r = _.xpath('.//a/span/text()')
        collocation_content_list.append(r)
        
    collocation_content = []
    for _ in collocation_content_list:
        r = ', '.join(_)
        collocation_content.append(r)
    
    collocation = list(zip(collocation_title_list,collocation_content))

    print(word)
    print('-' * 90)

    print('发音')
    print('美', us_soundmark, '英', uk_soundmark)
    print(us_sounds)
    print(uk_sounds)
    print('-' * 90)

    print('释义')
    for _ in info_list:
        print(_[0], _[1])
    print('-' * 90)

    if not tense_list == []:
        print('变体')
        for _ in tense_list:
            print(_[0], _[1])
        print('-' * 90)

    print('搭配')
    for _ in collocation:
        print(f'{_[0]}: {_[1]}')
    print('-' * 90)

    print('例句：')
    print(example_en_01)
    print(example_zh_01)
    print('\n')
    print(example_en_02)
    print(example_zh_02)
    print('\n')
    print(example_en_03)
    print(example_zh_03)


