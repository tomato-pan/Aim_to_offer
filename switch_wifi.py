# _*_ coding:utf-8 _*_
import os
import time
import subprocess
import random


def check_ping(ip, count=1, timeout=1000):
    cmd = 'ping -n %d -w %d %s > NUL' % (count, timeout, ip)
    # 通过os.system()方法执行命令
    response = os.system(cmd)
    return 'ok' if response == 0 else 'failed'


def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    ret = p.stdout.read()
    ret = str(ret)
    index = ret.find('SSID')
    index2 = ret.find('BSSID')
    if index > 0:
        print(index,index2)
        wifi_name = ret[index:index2-1].split(':')[1].strip().replace(r"\r\n","")
        return wifi_name


def auto_switch_wifi(wifiList):
    wifi = random.choice(wifiList)
    cmd = 'netsh wlan connect name="%s"' % wifi
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'



def main():
    # 百度ip
    ipTest = '61.135.169.121'
    # 可以切换的wifi
    wifiList = ['802.1x',"lys5"]
    while True:
        current_wifi = get_current_wifi()
        print ("当前的wifi为：", current_wifi)
        if auto_switch_wifi(wifiList) == 'ok':
            print ("切换成功")
            print ("-" * 40)
        else:
            continue
        time.sleep(5)




if __name__ == "__main__":
    main()
