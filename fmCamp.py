from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time,re,os,requests
import random
from pprint import pprint 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs
driver,fm_url=None,None
def open_site(): 
    url="https://www.fmkorea.com/gallery_girlgroup"
    html=requests.get(url)
    soup=bs(html.text,'html.parser')
    data1=soup.find('tbody')
    data2=data1.find('td',{'class':'title hotdeal_var8'})
    data3=data2.find('a')['href']
    # data3는 첫게시물의 뒤에붙는 숫자부분이다. ex) /2695397198
    driver.get(fm_url+data3)
    time.sleep(random.random()+2)
    
def log_in():
    global driver,fm_url
    options = Options()
    options.add_argument('--start-fullscreen')
    driver = webdriver.Chrome(executable_path='C:/Users/edhz8/OneDrive/바탕 화면/fmCamp/chromedriver', chrome_options=options)
    fm_url='https://www.fmkorea.com/'
    driver.get(fm_url)
    id='edhz8888'
    pw='$hassk@9797'

    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/input[4]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/input[5]').send_keys(pw)
    # 로그인 버튼을 눌러주자.
    time.sleep(random.random()+3)
    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/button').click()

def move_to_page(limit):
    cnt=0
    while cnt<limit:
        current_html=driver.page_source
        current_soup=bs(current_html,'html.parser')
        currnet_atag=current_soup.findAll('a',{'class':'bubble'})
        count=1
        time.sleep(random.random()+2)
        temppic,tempmp4=[],[]
        for i in currnet_atag:
            temp=i.text
            if temp[-4:] =='.jpg' or temp[-4:]=='.gif':
                temppic.append(temp)
                if cnt==limit: return
                pic=i['data-href']
                driver.get(fm_url+pic)
                cnt+=1
            elif temp[-4:]=='.mp4':
                tempmp4.append(i)
                
        for j in tempmp4:
            down=True
            tempj=j.text
            for k in temppic:
                if tempj[:-4] == k:
                    down=False
                    break
            
            if down:
                if cnt==limit: return
                pic=j['data-href']
                driver.get(fm_url+pic)
                cnt+=1
        if len(temppic)==0 and len(tempmp4)==0:
            current_video=current_soup.findAll('video')
            for v in current_video:
                if cnt==limit: return
                src=v['src']
                driver.get(src)
                cnt+=1
              


        time.sleep(random.random()+2)
        driver.execute_script("return go_to_next_('next');")
    #driver.quit()
    os.system('start c:/Users/edhz8/Downloads')

log_in()
open_site()
move_to_page(2000)

    


