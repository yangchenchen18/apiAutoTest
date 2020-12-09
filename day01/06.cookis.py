

import requests
url="https://www.bagevent.com/account/dashboard"
r=requests.get(url)
print(r.text)

headers = {"Cookie":'MEIQIA_TRACK_ID=1l8RlEua0appPmidcDpvwsVrtjH; __auc=29cc77ea1762748f491f93883f5; _ga=GA1.2.214410457.1606976863; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; BAGSESSIONID=ff1fdd97-2f59-4262-b58c-42a2e5070102; JSESSIONID=7EDB8E650967408898619B6F01CD3639; __asc=23cc63f41762cbb11eefc91227e; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976860,1607068226; MEIQIA_VISIT_ID=1lBQx3MdrOd9381AAJgiuVTUKpA; _gid=GA1.2.1610011343.1607068450; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068450'

}
url="https://www.bagevent.com/account/dashboard"
r=requests.get(url,headers=headers)
print(r.text)

