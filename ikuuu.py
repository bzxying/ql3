"""
cron: 0 7 * * *
new Env("WEB-ikuuu")
env add web_ikuuu = user#passwd
"""
# !/usr/bin/env python3
# coding: utf-8
import ApiRequest

tokenName = 'web_ikuuu'
msg = ''


class ikuuu(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'authority': 'ikuuu.pw',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'lang=zh-cn; _gid=GA1.2.1830428982.1709332118; ip=e1843fa01e71e2bc761078f1d7366830; expire_in=1709420582; _ga=GA1.1.2125388976.1709033063; _ga_8HVN7928SC=GS1.1.1709334123.3.1.1709334196.0.0.0',
            'origin': 'https://ikuuu.pw',
            'referer': 'https://ikuuu.pw/auth/login',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

    def login(self):
        data = {
            'email': 'darkbfly@163.com',
            'passwd': 'wlwzzfz123.',
            'code': '',
        }
        response = self.sec.post('https://ikuuu.pw/auth/login', data=data)
        print(response.text.encode('utf-8').decode('unicode_escape'))


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, ikuuu)
