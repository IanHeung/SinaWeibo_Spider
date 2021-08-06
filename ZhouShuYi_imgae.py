import requests
import time
import re
import pprint
#登录微博
headers_login={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '229',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_T_WM=11481803997; WEIBOCN_FROM=1110003030; MLOGIN=0; M_WEIBOCN_PARAMS=oid%3D180%26luicode%3D10000011%26lfid%3D102803',
    'Host': 'passport.weibo.cn',
    'Origin':'https://passport.weibo.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/91.0.4472.124'
}
print('#'*20+'欢迎使用微博照片爬虫工具，请登录'+'#'*20)
print('\n')
username=input('请输入微博登录帐号(确保帐号和密码都正确)\nID:')
password=input('请输入微博登录密码\npassword:')
print('正在登录中，请稍后...')
data_login={
    'username': str(username),#登录帐号
    'password': str(password),#登录密码
    'savestate': '1',
    'r': 'https://m.weibo.cn/?jumpfrom=weibocom',
    'ec': '0',
    'pagerefer': 'https://m.weibo.cn/',
    'entry': 'mweibo',
    'wentry':'' ,
    'loginfrom': '',
    'client_id': '',
    'code': '',
    'qq': '',
    'mainpageflag': '1',
    'hff': '',
    'hfp': ''
}
url_login='https://passport.weibo.cn/sso/login'
session=requests.Session()
response_post=session.post(url=url_login,data=data_login,headers=headers_login)
print('='*20+'登录成功'+'='*20)
print('\n')
time.sleep(2)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
}
uid=input('请输入uid(例如，不2不叫周淑怡：1890196401)\nuid:')
fid=input('请输入fid(例如，不2不叫周淑怡：1076031890196401)\nfid:')
if int(uid):
    if int(fid):
        print('输入正确,请设置下面选项')
        page_num=int(input('请输入想下载的总页数\npage_num:'))
        for page in range(1,page_num,1):
            base_url='https://m.weibo.cn/api/container/getIndex?is_hot[]=1&is_hot[]=1&jumpfrom=weibocom&type=uid&value='+uid+'&containerid='+fid+'&page='#每页源代码
            url=base_url+str(page)
            resp=requests.get(url=url,headers=headers)
            imgae_url=re.findall('"url":"(.*?)"',resp.text)#正则匹配所有的图片url
            i=1
            for url in imgae_url:
                url=''.join(url)
                url=url.replace('\\','')#替换\
                imgae_name=url.split('/')[-1]
                imgae_name=imgae_name.split('.')[-2]
                response=requests.get(url=url)
                time.sleep(2)
                with open(r"E:\Python\ZhouShuYi./%s.jpg"%imgae_name,'wb') as fp:
                    fp.write(response.content)
                i=i+1
                print('正在下载第'+str(i-1)+'张')
        print('完成')
    else:
        print('fid输入错误，请检查')
else:
    print('uid输入有错误，请检查')