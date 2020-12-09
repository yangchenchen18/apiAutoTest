import requests

url = "http://www.httpbin.org/post"
file1 = r"e:/test.txt"

# with open(file,"r", encoding='utf-8' ) as f1:
#     f1.read()
#     # c = f.read()
#     load = {"file1": (file, f1, "text/plain")}
#     r = requests.post(url, files=load)
#     # print(r.text)
file2=r"e:/png.png"
with open(file1,"r", encoding='utf-8' ) as f1:
    with open(file2,'rb')as f2:
    # load={"file1":(file,f,"image/png")}
        load={"file1": (file1, f1, "text/plain"),"file2":(file2,f2,"image/png")}
        r=requests.post(url,files=load)
        print(r.text)

