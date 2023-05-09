import requests
from lxml import etree
import numpy as np
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}
f = open('beijing.csv', mode='a', newline='', encoding='utf-8-sig')
write = csv.DictWriter(f, fieldnames=['title','url','text'])
write.writeheader()

for i in range(1,3):
    if i == 1:
        url = 'http://whlyj.beijing.gov.cn/zwgk/xwzx/szfdt/'
    else:
        url = 'http://whlyj.beijing.gov.cn/zwgk/xwzx/szfdt/index_{}.html'.format(i-1)

    response = requests.get(url=url, headers=headers).text
    tree = etree.HTML(response)
    li_list = tree.xpath('//ul[@class="bmbct-list10"]/li/a')

    for li in li_list:
        detail_url1 = li.xpath('@href')[0]
        detail_url = 'http://whlyj.beijing.gov.cn/zwgk/xwzx/szfdt/'+detail_url1[1:]
        detail_response = requests.get(url=detail_url, headers=headers).text
        detail_tree = etree.HTML(detail_response)
        item = {}
        title_list = detail_tree.xpath('//div[@class="pageArticleTitle aCur2"]/h3/text()')
        item['title'] = title_list[0] if title_list else None
        item['url'] = detail_url if detail_url else None
        text_list = detail_tree.xpath('//div[@class="view TRS_UEDITOR trs_paper_default trs_web trs_key4format"]/p/text()')
        joined_string = ''.join(text_list)
        item['text'] = joined_string if joined_string else None
        print(item)
        write.writerow(item)

    print(f'成功爬取第{i}页!')
    time.sleep(np.random.randint(1, 3))




