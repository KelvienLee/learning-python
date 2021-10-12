import requests, re, time 
import main

add_headers = {
    'authority':'ankiuser.net',
    'method':'POST',
    'path':'/edit/save',
    'scheme':'https',
    'accept':'*/*',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':'ankiweb=eyJrIjogIlJxOVNaT2x6MlRtNGZ2NmQiLCAiYyI6IDIsICJ0IjogMTYzMzk1Mjk0MH0.YETFinJeI-tC1crhAcEuYFKqLXDvzEK-JH1urPmrP3Y',
    'dnt':'1',
    'origin':'https://ankiuser.net',
    'referer':'https://ankiuser.net/edit/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}
edit_headers = {
    'authority':'ankiuser.net',
    'method':'GET',
    'path':'/edit/',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie':'ankiweb=eyJrIjogIlJxOVNaT2x6MlRtNGZ2NmQiLCAiYyI6IDIsICJ0IjogMTYzMzk1Mjk0MH0.YETFinJeI-tC1crhAcEuYFKqLXDvzEK-JH1urPmrP3Y',
    'referer':'https://ankiuser.net/study/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}

if __name__ == '__main__':
    # 接码csrf
    url = 'https://ankiuser.net/edit/'
    res = requests.get(url, headers=edit_headers)
    csrf = re.findall(r"new anki.Editor\('(.*)',", res.text)[0]

    url = 'https://ankiuser.net/edit/save'
    params =  {
        'nid': '',
        'data': main.data,
        'csrf_token': csrf,
        'mid': '1633611353388',
        'deck': '1633610331701'
    }
    time.sleep(2)
    res = requests.post(url, data=params, headers=add_headers)
    if res.status_code==200:
        print('success:操作成功')

    print(1)
    print(main.data)
