import requests
import json

from wx_api import WeChatOAuth, WeChatCloudDB


def getToken(appid, secret):
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='\
          + appid \
          +'&secret='+ secret
    print("开始获取token...")
    result = requests.get(url)
    result.encoding = "utf-8"
    print("response:" + result.text)
    tokens = json.loads(result.text)
    token = tokens['access_token']
    print("获取到的token:" + token + "，有效时间2个小时...")
    return token

if __name__ =="__main__":
    # getToken("wx40c91e9f3297e0a4",'9f4c668f504e4367119487d9af93e9e5')
    # getToken("wx84ff9429efd5c2f9","7889e11471ab36429e38eba99cbb893e")
    access_token_json = WeChatOAuth.get_access_token("wx84ff9429efd5c2f9","7889e11471ab36429e38eba99cbb893e")
    print(access_token_json)
    access_token = access_token_json["access_token"]
    wechatCloudDb = WeChatCloudDB("test-5gl4dqfw8f7cb546",access_token)
    wechatCloudDb.add_one("combo_test",).commit()