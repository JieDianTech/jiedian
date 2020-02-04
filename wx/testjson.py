#!/usr/bin/python
# coding=utf-8
import json
import urllib2
import time

class TestJson:
    # 初始化
    def __init__(self, wechat_config):
        self.appid = wechat_config['appid']
        self.appsecret = wechat_config['appsecret']
        self.template_id = wechat_config['template_id']
        self.access_token = ''

    # 获取access_token
    def get_access_token(self, appid, appsecret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            appid, appsecret)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_data = response.read()
        data = json.loads(json_data)
        access_token = data['access_token']
        self.access_token = access_token
        return self.access_token

    # 发送消息
    def send_msg(self, openid, template_id, iciba_everyday):
        msg = {
            'touser': openid,
            'template_id': template_id,
            'url': iciba_everyday['fenxiang_img'],
            'data': {
                'content': {
                    'value': iciba_everyday['content'],
                    'color': '#0000CD'
                },
                'note': {
                    'value': iciba_everyday['note'],
                },
                'translation': {
                    'value': iciba_everyday['translation'],
                }
            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(
            access_token)
        request = urllib2.Request(url, data=json_data)
        response = urllib2.urlopen(request)
        result = response.read()
        return json.loads(result)

    # 获取json数据
    def get_profitjson(self):
        url = 'http://222.186.36.208:88/wx/oeuIhv3vMeXBc3vVfOYqKlC5akGo.json'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_data = response.read()
        data = json.loads(json_data)
        print(data)
        print("\n history:\n")
        print(data["history"])
        return data

    def get_local_json(self, name):
        filename = '../xuchao/wx/' + name + '.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            print("\n history:\n")
            print(data["history"])
            f.close()
            return data

    def write_local_json(self, content, name):
        filename = '../xuchao/wx/' + name + '.json'
        with open(filename, 'w') as f:
            content['history'].append("加上一条新的")
            json.dump(content, f)
            f.close()

    def add_profit_json(self, content, name, profitToday):
        date = time.strftime("%Y/%m/%d")
        filename = '../xuchao/wx/' + name + '.json'
        #profitObj = content['profits'].
        with open(filename, 'w') as f:
            content['profits'].append({
                "date": date,
                "profit": profitToday,
                "paid": False,
            })
            json.dump(content, f)
            f.close()


wechat_config = {
    'appid': 'wxbc8018d134b819a8',  # 此处填写你的appid
    'appsecret': '66ef76776bab236be696aba9c095dc01',  # 此处填写你的appsecret
    'template_id': '9SAobB-MzLFGhO1MT0D_ew7eG8WYg5Z69rD6SwGRkgo'  # 此处填写你的模板消息ID
}

openid_gxj = 'oeuIhvyw19iE5nPqHGFvbWa2Ymlg'  # 高晓骏
openid_w = 'oeuIhv3vMeXBc3vVfOYqKlC5akGo'  #袁文

testjson = TestJson(wechat_config)
#testjson.get_profitjson()
#testjson.get_local_json(openid_gxj)
print ("今日的日期：" + time.strftime("%D"))
content = testjson.get_local_json(openid_w)
#testjson.write_local_json(content, openid_w)
testjson.add_profit_json(content, openid_w, 100)

