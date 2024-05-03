"""
new Env("微信小程序-老板电器")
cron 0 8 * * *
环境变量名称 wx_glg
"""

import ApiRequest
import mytool

title = '微信小程序-老板电器'
tokenName = 'wx_lbdq'


class lbdq(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'vip.foxech.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
            'Content-Type': 'application/json',
            'Referer': 'https://servicewechat.com/wxc8c90950cf4546f6/150/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.token = data.split('#')[0]
        self.openid = data.split('#')[1]
    def login(self):
        json_data = {
            'timestamp': mytool.getMSecTimestamp(),
            'token': self.token,
            'openid': self.openid,
        }

        response = self.sec.post('https://vip.foxech.com/index.php/api/member/user_sign', json=json_data)
        print(response.text)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, lbdq)