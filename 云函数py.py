import requests
# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = '2'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCU89402Tf98b7f01ca3394b9ce9aa5e2ed1a****************'
# 填入glados账号对应cookie
cookie = '__cfduid=d825014ac33b402b3f**************'
referer = 'https://glados.rocks/console/checkin'

def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == '2':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+',xms3，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
