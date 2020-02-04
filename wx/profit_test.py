#!/usr/bin/python
#coding=utf-8
import json
import urllib2
import random
import time

class iciba:
    # 初始化
    def __init__(self, wechat_config):
        self.appid = wechat_config['appid']
        self.appsecret = wechat_config['appsecret']
        self.template_id = wechat_config['template_id']
        self.access_token = ''

    # 获取access_token
    def get_access_token(self, appid, appsecret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, appsecret)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_data = response.read()
        data = json.loads(json_data)
        access_token = data['access_token']
        self.access_token = access_token
        return self.access_token

    # 发送消息//"https://docs.qq.com/sheet/DVUJyemdxeEJWd2Fv?c=A1A0A0",
    def send_msg(self, openid, template_id, day_profit, userid):
        msg = {
            'touser': openid,
            'template_id': template_id,
            'url': "http://www.btcat.cn/my.html",
            'data': {
                'content': {
                    'value': '您有一笔收益到账啦，金额是：' + str(day_profit) + "元。",
                    'color': '#0000CD'
                    },
                'note': {
                    'value': '今日挖的是 BFC',
                }
            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
        request = urllib2.Request(url, data=json_data)
        response = urllib2.urlopen(request)
        result = response.read()
        return json.loads(result)

    # 为设置的用户列表发送消息
    def send_everyday_words(self, openids):
     
		
        result = self.send_msg(openid_chen, self.template_id, day_profit_chen, openid_chen)
     #   result = self.send_msg(openid_w, self.template_id, day_profit_w, openid_w)
     #   result = self.send_msg(openid_liubai, self.template_id, day_profit_w, openid_w)
     #   result = self.send_msg(openid_chen, self.template_id, day_profit_chen, openid_chen)
     #   result = self.send_msg(openid_gxj, self.template_id, day_profit_gxj, openid_gxj)
     #   for openid in openids:
     #       result = self.send_msg(openid, self.template_id, day_profit_w, openid_w)
     #       result = self.send_msg(openid, self.template_id, day_profit_gxj, openid_gxj)
     #       if result['errcode'] == 0:
     #           print ' [INFO] send to %s is success' % openid
     #       else:
     #           print ' [ERROR] send to %s is error' % openid

    # 执行
    def run(self, openids):
        self.send_everyday_words(openids)

    def get_local_json(self, name):
        filename = '/var/www/html/wx/' + name + '.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            f.close()
            return data
    
    def add_profit_json(self, content, name, profitToday):
        date = time.strftime("%Y/%m/%d")
        filename = '/var/www/html/wx/' + name + '.json'
        with open(filename, 'w') as f:
            content['profits'].append({
                "date": date,
                "profit": profitToday,
                "paid": False,
            })
            json.dump(content, f)
            f.close()


if __name__ == '__main__':
    #day_profit_gxj = round(109000 * 0.31 / 365 + random.random() * 10, 2)
    #day_profit_w = round(500000 * 0.31 / 365 + random.random() * 10, 2)
    #新增---test---
    day_profit_chen = round(200000 * 0.31 / 365 + random.random() * 10, 2)

    # 微信配置
    wechat_config = {
        'appid': 'wxbc8018d134b819a8', #此处填写你的appid
        'appsecret': '66ef76776bab236be696aba9c095dc01', #此处填写你的appsecret
        'template_id': '6-0Sfm7DpU4pX3uY40bRVqGHaoMLYmo8M80boWLo__M' #此处填写你的模板消息ID
    }
    # 用户列表
    openids = [
        'oeuIhv3ku6RV--VRJNlI5xW79Ek0', #猫猫姐姐
        'oeuIhv-sAMcBCx8e-lEIg7RVYoHA' #马思腾
    ]
    openid_chen = 'oeuIhv7aSAcPr3HsAoXsUMlkq0Go'  #陈旺龙
    
    # 执行
    icb = iciba(wechat_config)
    content = icb.get_local_json(openid_chen)
    icb.add_profit_json(content, openid_chen, day_profit_chen)
    icb.run(openids)
