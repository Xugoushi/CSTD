import csv
import jieba
import nltk

f = open("new_beijing.csv", mode="a", newline='', encoding='utf-8-sig')
writer = csv.DictWriter(f, fieldnames=['url', 'text'])
writer.writeheader()

keywords = ['旅游']
#keywords = ['社会旅游', '福利旅游', '社会补贴旅游', '补贴旅游', '公益旅游', '旅游优惠券', '免费旅游']

with open(r'G:\code\社会旅游数据\beijing.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        text = row[2]
        url = row[1]
        if any(keyword in text for keyword in keywords):
            list1 = {'url':url, 'text':text}
            # tokens = nltk.word_tokenize(text)
            # tokens = jieba.lcut(text)
            print(list1)
            writer.writerow(list1)





