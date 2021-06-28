import base64
import requests
from lxml import etree
import time

def fofa_search(search_data,page):
    pages = page + 1
    search_data_b=base64.b64encode(search_data.encode('utf-8'))               #转换为base64加密
    search_data_bs=search_data_b.decode('utf-8')
    headers={
        'user-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        "cookie":''     # cookie
    }
    for yeshu in range(1,pages):
        url="https://classic.fofa.so/result?page="+str(yeshu)+"&page_size=10&qbase64="
        urls=url+search_data_bs                #拼接参数  加上base64的值  ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI=
        print("正在提取" + str(yeshu) + "页")
        try:
            result=requests.get(urls,headers=headers,timeout=0.8).content      #请求
            print(urls)
            soup =etree.HTML(result)
            ip_data=soup.xpath('//div[@class="list_mod_t"]/a[@target="_blank"]/@href')    #找到节点的值
            print(ip_data)
            ipdata='\n'.join(ip_data)
            with open(r'ip.txt','a+') as f:                      #写文件
                f.write(ipdata+'\n')
                f.close()
                time.sleep(0.8)
        except Exception as e:
            pass



if __name__ == '__main__':

    fofa_search('body="phpstudy探针" && country="US"',15)
