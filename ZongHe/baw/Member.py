
def register(url,baserequests,data):
    '''

    :param url:环境信息比如：http：//jy001:9081
    :param baserequests:
    :param data:
    :return:
    '''
    url=url+"futureloan/mvc/api/member/register"
    r=baserequests.post(url,data=data)
    return r

def list(url,baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url )
    return r
def login(url,baserequests,data):
    url=url+"futureloan/mvc/api/member/login"
    r = baserequests.post(url,data=data)
    return r



if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests
    b=BaseRequests()
    canshu={ "mobilephone": "13567890090","pwd":"123456"}
    r=register("http://jy001:8081/",b,canshu)
    print(r.text)