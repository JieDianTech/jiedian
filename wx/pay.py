#!/usr/bin/python
#coding=utf-8
import json
import time

def calculateProfit(openid):
    filename = '/var/www/html/wx/' + openid + '.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        profits = data['profits']
        sum = 0
        for profit in profits: 
            sum += profit['profit']
    return sum

def changeProfit(sum, openid):
    filename = '/var/www/html/wx/' + openid + '.json'
    with open(filename, 'w') as f:
        content = json.load(f)
        content['paid'] = sum
        content['unpaid'] = 0
        json.dump(content, f)
        f.close()
    return

namelist = {

}

openid_gxj = 'oeuIhvyw19iE5nPqHGFvbWa2Ymlg' #高晓骏
openid_w = 'oeuIhv3vMeXBc3vVfOYqKlC5akGo'  #像素

sum_w = calculateProfit(openid_w)
changeProfit( sum_w, openid_w)
