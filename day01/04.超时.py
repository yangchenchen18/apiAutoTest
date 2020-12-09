# 超时
# 1、上传大文件超时
# 2、接口有性能要求，比如接口必须在0.5
#
import requests
for i in range(10):
    try:
        url="http://192.168.150.54:8089//futureloan/mvc/api/member/list"
        r= requests.get(url,timeout=0.009)
        print(r.text)
    except Exception as e:
        print(e)