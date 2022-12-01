# coding=utf-8
import datetime
import random
import requests
import yaml

s = requests.session()
config_path = "config.yaml"


# 关于洗头
def get_wash_hair():
    if len(str(int(f"{datetime.datetime.now():%d}") / 3)) == 3:
        return '我抬手一算，今天是个洗头的好日子。'
    else:
        return 'emm，阔以不洗，多睡一下下。'


# 获取随机颜色
# def get_color():
#     get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
#     color_list = get_colors(100)
#     return random.choice(color_list)


# 获取当前时间
def now_time():
    return f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"


# 获取配置文件内容
def get_config():
    try:
        with open(config_path, encoding='utf-8') as f:
            x = yaml.load(f, Loader=yaml.FullLoader)
            return x
    except:
        return print("==get_config找不到配置文件,检查下路径==\nconfig_path:", config_path)


# 获取当前天气
def get_weather():
    url = get_config()['get_weather'][0]
    try:
        weather = s.get(url)
        text = weather.json()
        msg = text['data'][0]['narrative']
        return msg
    except:
        print('==获取天气错误，检查地址啥的==')


# 获取微博热搜
def get_weibo():
    access_key = get_config()['get_weibo'][0]
    secret_key = get_config()['get_weibo'][1]
    url = f"https://www.coderutil.com/api/resou/v1/weibo?size=3&access-key={access_key}&secret-key={secret_key}"
    try:
        resow = s.get(url)
        msg = resow.json()['data'][0]['keyword'] + '\n' + '                         ' + resow.json()['data'][1][
            'keyword']
        return msg
    except:
        print("==看看地址对不对==")


# 鸡汤语录
def get_yl():
    access_key = get_config()['get_weibo'][0]
    secret_key = get_config()['get_weibo'][1]
    url = f"https://www.coderutil.com/api/yulu/it?&access-key={access_key}&secret-key={secret_key}"
    try:
        yule = s.get(url)
        text = yule.json()['data']['cnText'] + '\n' + yule.json()['data']['enText']
        return text
    except:
        print('==看看地址对不对==')


# 获取app-id，secret
def get_a_s():
    try:
        get_as = get_config()["get_a_s"]
        return get_as
    except:
        return print("==app-id，secret获取失败==\n", get_config())


# 获取微信access_token
def get_access_token():
    body = get_a_s()
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={body[0]}&secret={body[1]}"
    try:
        token = s.get(url)
        if "access_token" in token.json():
            return token.json()["access_token"]
        else:
            errmsg = token.json()
            return print("==获取token错误==\nerrmsg:", errmsg, url)
    except:
        return print("==access_token请求失败==\nurl:", url)


# 发送消息模板
def send_msg(acc_token):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={acc_token}"
    body = get_config()['send_msg']
    for user in range(len(body['touser'])):
        body2 = dict(touser=body['touser'][user], template_id=body["template_id"], url=body['url'], topcolor="#FF0000",
                     data=dict(nowtime={
                         "value": now_time(),
                         "color": "#ffa631"
                     }, weather={
                         "value": get_weather(),
                         "color": "#ff8936"
                     }, wash_hair={
                         "value": get_wash_hair(),
                         "color": "#c89b40"
                     }, look_on={
                         "value": get_weibo(),
                         "color": "#ca6924"
                     }, constellation={
                         "value": get_yl(),
                         "color": "#d9b611"
                     }))
        try:

            send = s.post(url, headers=headers, json=body2)
            return print(send.json())
        except:
            print(f"==查一下参数=={body2}")
        user += 1


if __name__ == '__main__':
    access_token = get_access_token()
    send_msg(access_token)
