import sys
import requests
import json

def getToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx40c91e9f3297e0a4&secret=9f4c668f504e4367119487d9af93e9e5'
    print("开始获取公众号token...")
    result = requests.get(url)
    result.encoding = "utf-8"
    print("response:" + result.text)
    tokens = json.loads(result.text)
    token = tokens['access_token']
    print("获取到的token:" + token + "，有效时间2个小时...")
    return token

def sendToUser(open_id):
    global token
    print("sendToUser:" + open_id)
    print("sendToUser token:" + token)
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + token
    logistics_code = sys.argv[1]
    company = sys.argv[2]
    template_id = "2CpmG208670kd-_za3zQaDYOY9UXDes52dn6PSX3huQ"
    first_value = "你好，鲜食套餐已发货～" #sys.argv[4] #.encode('utf-8').decode('latin-1')
    keyword1_value = logistics_code
    keyword2_value = company#.encode('utf-8').decode('latin-1')
    remark_value = "点击查看套餐详情" #.encode('utf-8').decode('latin-1')

    print("输入的运单号：" + logistics_code)
    print("物流公司：" + company)
    print("要发送给的用户openId:" + open_id)

    header = {"Content-Type":"application/json"}
    miniprogram = {'appid':"wx84ff9429efd5c2f9", 'pagepath':'pages/index/index'}
    first_data = {'value':first_value}
    keyword1_data = {'value':keyword1_value}
    keyword2_data = {'value':keyword2_value}
    remark_data = {'value':remark_value}
    template_data = {
        'first': first_data,
        'keyword1':keyword1_data,
        'keyword2':keyword2_data,
        'remark': remark_data
    }
    body = {
        'touser':open_id,
        'template_id':template_id,
        'url':'http://weixin.qq.com/download',
        'miniprogram': miniprogram,
        'data': template_data
    }
    datas = json.dumps(body)
    print('body:' + datas)

    result = requests.post(url, data=datas, headers=header)
    print(result.text)

if __name__ == '__main__':
    global token
    token = getToken()
    sendToUser(sys.argv[3])
    sendToUser('ob5h55i-5w4YUCb4vEv74nSgyPAI')
