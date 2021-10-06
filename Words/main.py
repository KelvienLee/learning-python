import requests
import re


search_word = 'test'
URL = f'https://cn.bing.com/dict/search?q={search_word}'


def get_html(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    html = get_html(URL)

    word = re.findall('<h1.*?<strong>(.*?)</strong>', html, re.DOTALL)[0]
    us_soundmark = re.findall('<div class="hd_prUS b_primtxt">.*?;(.*?)</div>', html, re.DOTALL)[0]
    uk_soundmark = re.findall('<div class="hd_pr b_primtxt">.*?;(.*?)</div>', html, re.DOTALL)[0]
    us_sounds = re.findall('<a class="bigaud".*?(https://.*?.mp3).*?</a>', html, re.DOTALL)[0]
    uk_sounds = re.findall('<a class="bigaud".*?(https://.*?.mp3).*?</a>', html, re.DOTALL)[1]
    in_list = re.findall('<div class="hd_area">.*?</div>.*?<li>(.*?)</li></ul>', html, re.DOTALL)

    print(word)
    print('美', us_soundmark)
    print('英', uk_soundmark)
    print(us_sounds)
    print(uk_sounds)
    print(len(in_list))
    print(in_list)
