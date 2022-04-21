import requests
import os

def get_status_codes():
    url = 'https://www.baidu.com'

    headers = {
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/12.0.0.300'
    }

    r = requests.get(url,headers=headers)

    try:
        print(r.status_code)
        return r.status_code
        #return r.json()
    except Exception as msg:
        print('失败了!')

def ENV(keyname):
    value = os.environ.get(keyname)
    try:
        print(value)
        return value
    except Exception as msg:
        print('没获取到.')

# def hook_up(textup):
#     print('前置处理')
#     return textup
#
# def hook_down(textdown):
#     print('后置处理')
#     return textdown


if __name__ == '__main__':
    get_status_codes()