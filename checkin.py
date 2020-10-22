import requests
import json
import os

# import environ
# cookie = environ.cookie
# wechat_bot = environ.wechat_bot
cookie = os.environ["COOKIE"]  # 填入glados账号对应cookie
wechat_bot = os.environ["WECHAT_BOT"]  # 企业微信机器人 url


def wechat_bot_message(left_times, message):
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f'# Gloados\n' +
                       f'当前剩余次数：<font color="warning">{left_times}</font>次\n' +
                       f'>{message}'
        }
    }
    r = requests.post(wechat_bot, headers=headers, json=data)


def start():
    payloadData = {"token": "glados_network"}

    headers = {'cookie': cookie,
               'referer': 'https://glados.rocks/console/checkin',
               'origin': 'https://glados.network',
               'content-type': 'application/json;charset=UTF-8',
               }

    url_checkin = "https://glados.rocks/api/user/checkin"
    url_satus = "https://glados.rocks/api/user/status"

    checkin = requests.post(url_checkin, headers=headers,
                            data=json.dumps(payloadData))
    state = requests.get(url_satus, headers=headers)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays'].split('.')[0]
        # print(time)
        # print(mess)
        wechat_bot_message(time, mess)


if __name__ == '__main__':
    # wechat_bot_message('0', 'Please Try Tomorrow')
    start()
