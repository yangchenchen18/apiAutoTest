

def loan_add(url,baserequests,data):
    url=url+"futureloan/mvc/api/loan/add"
    r=baserequests.get(url,data=data)
    return r