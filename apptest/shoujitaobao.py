# coding=utf-8
import random
import requests
import yaml
import time

s = requests.session()
config_path = "config.yaml"


# 关于洗头
def get_wash_hair():

    if len(str(int(time.strftime("%d", time.localtime()))/3)) == 3:
        return '我抬手一算，今天是个洗头的好日子。'
    else:
        return 'emm，阔以不洗，多睡一下下。'

# 获取随机颜色
def get_color():
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)

# 获取当前时间
def now_time():

    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 获取配置文件内容
def get_config():
    try:
        with open(config_path, encoding='utf-8') as f:
            x = yaml.load(f, Loader=yaml.FullLoader)
            return x
    except:
        return print("==get_config找不到配置文件,检查下路径==\nconfig_path:",config_path)

#获取当前天气
def get_weather():

    url = get_config()['get_weather'][0]
    try:
        weather = s.get(url)
        text = weather.json()
        msg = text['data'][0]['narrative']
        return msg
    except:
        print('==获取天气错误，检查地址啥的==')

#获取微博热搜
def get_weibo():

    access_key = get_config()['get_weibo'][0]
    secret_key = get_config()['get_weibo'][1]
    url = "https://www.coderutil.com/api/resou/v1/weibo?size=3&access-key=%s&secret-key=%s"%(access_key,secret_key)
    try:
        resou = s.get(url)
        msg = resou.json()['data'][0]['keyword']+'\n'+'                         '+resou.json()['data'][1]['keyword']
        return msg
    except:
        print("==看看地址对不对==")

#鸡汤语录
def get_yulu():

    access_key = get_config()['get_weibo'][0]
    secret_key = get_config()['get_weibo'][1]
    url = "https://www.coderutil.com/api/yulu/it?&access-key=%s&secret-key=%s"%(access_key,secret_key)
    try:
        yulu = s.get(url)
        text = yulu.json()['data']['cnText']+'\n'+yulu.json()['data']['enText']
        return text
    except:
        print('==看看地址对不对==')


# 获取appid，secret
def get_a_s():
    try:
        get_a_s = get_config()["get_a_s"]
        return get_a_s
    except:
        return print("==appid，secret获取失败==\n",get_config())

#获取微信access_token
def get_access_token():

    body = get_a_s()
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(body[0],body[1])
    try:
        TOKEN = s.get(url)
        if "access_token" in TOKEN.json():
            return TOKEN.json()["access_token"]
        else:
            errmsg = TOKEN.json()
            return print("==获取token错误==\nerrmsg:",errmsg,url)
    except:
        return print("==access_token请求失败==\nurl:",url)

# #获取模板id
# def get_templateid(access_token):
#
#     url = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=%s"%(access_token)
#     templateid = s.get(url)
#     return print(templateid.json())


#发送消息模板
def send_msg(access_token):

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s"%(access_token)
    body = get_config()['send_msg']
    for user in range(len(body['touser'])):
        body2 = data = {
            "touser": body['touser'][user],
            "template_id": body["template_id"],
            "url": body['url'],
            "topcolor": "#FF0000",
            "data": {
                "nowtime": {
                    "value": now_time(),
                    "color": get_color()
                    },
                "weather": {
                    "value": get_weather(),
                    "color": get_color()
                    },
                "wash_hair": {
                    "value": get_wash_hair(),
                    "color": get_color()
                    },
                "look_on": {
                    "value": get_weibo(),
                    "color": get_color()
                    },
                "constellation": {
                    "value": get_yulu(),
                    "color": get_color()
                    },
                }
            }
        try:

            send_msg = s.post(url,headers=headers,json=body2)
            return print(send_msg.json())
        except:
            print("==查一下参数==")
    user += 1

if __name__ == '__main__':

    access_token = get_access_token()
    send_msg(access_token)



