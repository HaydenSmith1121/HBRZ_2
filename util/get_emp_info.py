# 导入request模块
import csv
import json

import requests

# 创建一个会话对象
session = requests.session()
# 统一设置会话级别的请求头
session.headers.update({
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpblVzZXIiOnsiYWNjb3VudElkIjoiODgyMDYxMzY0NTQzMjM0MDQ4MCIsInRlbmFudElkIjpudWxsLCJsb2dpbkFjY291bnQiOiIwMDI0NTA2NCIsImxvZ2luUGFzc3dvcmQiOiIkMmEkMTAkN0tnMmxJZ0xDVnFwSER0ZGZvcFEyZU44MXhmSGIxaG8zcHJFc2ZUOEk1MDU5RnJrY244QXEiLCJhY2NvdW50TmFtZSI6bnVsbCwic3RhdHVzIjoiMCIsInBlcm1pc3Npb25zIjpudWxsLCJyb2xlcyI6bnVsbCwiZGF0YVNjb3BlIjpudWxsLCJ1c2VybmFtZSI6IjAwMjQ1MDY0IiwicGFzc3dvcmQiOiIkMmEkMTAkN0tnMmxJZ0xDVnFwSER0ZGZvcFEyZU44MXhmSGIxaG8zcHJFc2ZUOEk1MDU5RnJrY244QXEifSwiZXhwIjoxNzcyMzAwMDEwLCJ1c2VyX25hbWUiOiIwMDI0NTA2NCIsImp0aSI6ImE3YWM2NzdlLTRiYmYtNDcyYy1iNDI5LThhZTllNzBjNTUxMCIsImNsaWVudF9pZCI6Im1hcmNoIiwic2NvcGUiOlsiYWxsIl19.grgNhRsvxKzqTUyNFNd7iPREAoIFoPtoTZQcWbrWkLU",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer": "http://192.168.1.25/pfmcManage/pfmcenvironment/pfmcOrg?isExternalUser=false",
    "menuCode": "8712698855247806464",
    "moduleCode": ""
})

resp = session.get("http://192.168.1.25/api/pfmc-asist/pfmcOrgEmp/listEmpByOrgId?pageNum=1&pageSize=10")

# print(resp.content)
# print(resp.encoding)
print(resp.json())
# data1=resp.json()["data"]
# info=data1["list"]
# # print(len( info))
# # print(len(data1))
# #
# # with open("../res/emp_info.json", "w", encoding="utf-8") as fp:
# #     json.dump(resp.json(), fp, ensure_ascii=False)
# #     fp.write("\n")
#
# with open("../res/emp_info_1.csv", "w", encoding="utf-8", newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["姓名","工号","密码"])
#     for i in range(len(info)):
#         name=info[i]["empName"]
#         empNo=info[i]["empNumber"]
#         writer.writerow([name,empNo,""])




session.close()
