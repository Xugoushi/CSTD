import requests
from lxml import etree
import numpy as np
import time
import csv
import random
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}
f = open('广州.csv', mode='a', newline='', encoding='utf-8-sig')
write = csv.DictWriter(f, fieldnames=['title','url','text'])
write.writeheader()

for i in range(1,500):
    if i == 1:
        #url = 'https://whly.hebei.gov.cn/xwzx/wlxw/index.html'
        url = "http://www.gd.gov.cn/xxts/index.html"
    #     url = "https://whly.hebei.gov.cn/zwf/ui/catalog/15931/pc/index_{}.html".format(i)
    else:
        url = 'http://www.gd.gov.cn/xxts/index_{}.html'.format(i)
   # url = 'http://whlyj.np.gov.cn/cms/sitemanage/index.shtml?siteId=100458956908320000&page={}'.format(i)
    # url = 'https://wgly.hangzhou.gov.cn/col/col1692916/index.html'
    # url ='https://sxwg.sx.gov.cn/col/col1647147/index.html?uid=6068758&pageNum={}'.format(i)
           
    print(url)

    response = requests.get(url=url, headers=headers)
    
    content = response.text
    content = response.content.decode('utf-8')
    f_clean=content.replace('<record>','').replace('</record>','').replace('<![CDATA[','').replace(']]>',"").replace('<recordset>',"").replace('</recordset>',"").replace('<nextgroup>',"").replace('</nextgroup>',"").replace('<datastore>',"").replace("</datastore>","").replace('<script type="text/xml">','')
    

    # tree = etree.HTML(f_clean)
    soup = BeautifulSoup(f_clean, 'html.parser')
    url_list=soup.select("div.viewList>ul>li>span>a")
    # title_list=soup.select("div.fr>div>div>a>text()")
    #print(url_list)
    li_list = [a['href'] for a in url_list]
    title_list = [a.text for a in url_list]
    #tree = etree.HTML(response)
    #li_list = tree.xpath('//div[@class="list"]/ul/li/a')
    #li_list = tree.xpath('//ul/li/a')
    # li_list = tree.xpath('//div[@class="right clearfix"]/a')
    # li_list = tree.xpath('//ul[@class="info-list i-show mt10"]/li/a')
    # li_list = tree.xpath('//div[@class="head"]/ul/li/a')
    #li_list = tree.xpath('//div[@class="right_x"]/ul/li/a')
    #li_list = tree.xpath("//ul[@class='doc_list list-6797891']/li/a")	
    print(li_list)
    for i,li in enumerate(li_list): 
        # detail_url1 = li.xpath('@href')[0]
        # count += 1
        # if count <= 20:
        #     #detail_url = 'https://whly.hebei.gov.cn/'+detail_url1[1:]
        #     detail_url = 'http://wlj.xm.gov.cn/zwgk/bmdt/'+ detail_url1[1:]
        # else:
        #     break
            # detail_url = detail_url1
            # print(detail_url)
        #detail_url = 'https://sxwg.sx.gov.cn/'+ li[1:]
        detail_url = li[:]
        print(detail_url)
    
        detail_response1 = requests.get(url=detail_url,headers=headers)
        detail_response1.encoding = detail_response1.apparent_encoding
        detail_response = detail_response1.text

        detail_tree = etree.HTML(detail_response)
        item = {}
        # title_list = detail_tree.xpath('//div[@class="content"]/h1/text()')
        # title_list = detail_tree.xpath('//div[@class="detail-box"]/h1/text()')
        # title_list = detail_tree.xpath('//div[@class="bt"]/text()')
        #title_list = detail_tree.xpath("//div[@class='t']/h2/text()")

        # soup = BeautifulSoup(detail_response, 'html.parser')
        # url_list=soup.select("div.")
        
        # title_list = detail_tree.xpath('//div[@class="fcdiv2"]/p/text()')
        item['title'] = title_list[i] if title_list else None
        item['url'] = detail_url if detail_url else None
        # text_list = detail_tree.xpath('//div[@class="view TRS_UEDITOR trs_paper_default trs_word"]/p/text()') 
        text_list = detail_tree.xpath('//div[@class="zw"]//p//text()') 
        #text_list = detail_tree.xpath('//div[@class="content skin-original line0"]//div//p//text()')
        
        joined_string = ''.join(text_list)
        item['text'] = joined_string if joined_string else None
        # rand_int = random.randint(0, 1)
        # item['label'] = rand_int
        print(item)
        write.writerow(item)

    print(f'成功爬取第{i}页!')
    time.sleep(np.random.randint(1, 3))




