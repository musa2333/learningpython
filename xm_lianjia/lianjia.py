import sys
import random
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from functools import reduce
from time import clock


HOUSE_DIR='./houses_lianjia_xm.csv'

def get_one_page_house(url) :
    print ('Fetching data from'+url)
    r=requests.get(url)
    r.encoding='utf8'
    html=r.text
    
    soup=BeautifulSoup(html, "html5lib")
    hlst = soup.findAll('div', class_='info-panel')
    one_page_house=[]
    for h in hlst:
        house=[]
        area=h.parent['data-id'][0:4]
        village=h.find('a',class_='laisuzhou').string
        price = h.find('div',class_='price-pre').string
        totalprice=h.find('span',class_='num').string+'万'
        typeof=h.find('a',attrs={"data-el":"region"}).string
        zone=h.find('a',class_='laisuzhou').next_sibling.next_sibling.string
        meters=h.find('a',class_='laisuzhou').next_sibling.next_sibling.next_sibling.string
        direction = h.find('a',class_='laisuzhou').next_sibling.next_sibling.next_sibling.next_sibling.string
        direction = (direction if direction != None else '')
        #con=h.find('div',class_='con').a.string
        #print(con)
        lent=len(h.find('div',class_='con').contents)
        floor = h.find('div',class_='con').contents[2]
        year=h.find('div',class_='con').contents[4] if lent>4 else ''
        href=h.find('h2').a['href']
        house.append(''.join(area.split()))
        house.append(''.join(village.replace(',','.').split()))
        house.append(''.join(typeof.split()))
        house.append(''.join(zone.split()))
        house.append(''.join(meters.split()))
        house.append(''.join(direction.split()))
        house.append(''.join(totalprice.split()))
        house.append(''.join(price.split()))
        house.append(''.join(floor.split()))
        house.append(''.join(year.split()))
        house.append(''.join(href.split()))
        one_page_house.append(house)
        
    print('done')
    return one_page_house

def write_to_txt(s):

    print('Write to file...')
    h1=open(HOUSE_DIR,'a',encoding='utf-8')
    h1.write(s)
    h1.close()
    print('write done')

if __name__=='__main__':
    start=clock()
    url_pre='http://xm.lianjia.com/ershoufang/pg'
    #url_pre='http://xm.lianjia.com/ershoufang/rs%E5%A4%A7%E5%94%90%E4%B8%96%E5%AE%B6%E4%B8%89/'
    total_page_num=101
    page_num=1
    for p in range(page_num,total_page_num,1):
        url=url_pre+str(p)
    #url=url_pre
        print('page:',str(p))
        write_to_txt('\n'.join([','.join(h) for h in get_one_page_house(url)])+'\n')
    end=clock()

    print('finish',(end-start),'s')       
        
