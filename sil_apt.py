import requests
import pandas as pd
from pandas import DataFrame as df
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
import time
import os 
import urllib.request
import urllib.parse
from requests import get
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import re
import json

telgm_token = ''

bot = telegram.Bot(token = telgm_token)

cur_time = time.ctime()
print("_______________" + cur_time + "_______________")

#bot.sendMessage(chat_id='-,', text="이거 지금 텔레그램 봇이 보내주는거 쿄쿄")


import requests

def get_apt_prc_range(c_id):
    cookies = {
        'NNB': 'AN6EKJL4CWLWG',
        'NDV_SHARE': '"MTEHpsjAfehumHHohL3ZOukJvMIIGbjXoGcBX0HC0RCzn5WMxES0gikBNub50uEjYTi88wak0U0TM4slIxBteiVB2vKiBnix8yyHCU0e1PQUGE2euEDriI98S9QOfxTXi3cSpkdcX/VOMnVgUjJpsQw="',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'landHomeFlashUseYn': 'Y',
        'nx_ssl': '2',
        '__utmc': '163452323',
        '_ga': 'GA1.2.1634362597.1671244222',
        '_gcl_au': '1.1.1283574796.1671483413',
        'ASID': '7625715e000001852fb03ce90000005a',
        'realestate.beta.lastclick.cortar': '1156000000',
        '__utma': '163452323.1634362597.1671244222.1671637503.1671809984.5',
        '__utmz': '163452323.1671809984.5.5.utmcsr=land.naver.com|utmccn=(referral)|utmcmd=referral|utmcct=/auction/',
        'nid_inf': '1129651127',
        'NID_JKL': '78Y2upXds01bZi66n0Iss2ZJnttNyMg5LRcknqBLMuo=',
        'SHOW_FIN_BADGE': 'Y',
        'HT': 'HM',
        'page_uid': 'hIVlblp0JXossadS6QhssssssG4-089423',
        'BMR': 's=1672159555330&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Djsk6824%26logNo%3D222072859547&r2=https%3A%2F%2Fwww.google.com%2F',
        'REALESTATE': '1672159640484',
        'wcs_bt': '44058a670db444:1672159640',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'NNB=AN6EKJL4CWLWG; NDV_SHARE="MTEHpsjAfehumHHohL3ZOukJvMIIGbjXoGcBX0HC0RCzn5WMxES0gikBNub50uEjYTi88wak0U0TM4slIxBteiVB2vKiBnix8yyHCU0e1PQUGE2euEDriI98S9QOfxTXi3cSpkdcX/VOMnVgUjJpsQw="; nhn.realestate.article.rlet_type_cd=A01; landHomeFlashUseYn=Y; nx_ssl=2; __utmc=163452323; _ga=GA1.2.1634362597.1671244222; _gcl_au=1.1.1283574796.1671483413; ASID=7625715e000001852fb03ce90000005a; realestate.beta.lastclick.cortar=1156000000; __utma=163452323.1634362597.1671244222.1671637503.1671809984.5; __utmz=163452323.1671809984.5.5.utmcsr=land.naver.com|utmccn=(referral)|utmcmd=referral|utmcct=/auction/; nid_inf=1129651127; NID_JKL=78Y2upXds01bZi66n0Iss2ZJnttNyMg5LRcknqBLMuo=; SHOW_FIN_BADGE=Y; HT=HM; page_uid=hIVlblp0JXossadS6QhssssssG4-089423; BMR=s=1672159555330&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Djsk6824%26logNo%3D222072859547&r2=https%3A%2F%2Fwww.google.com%2F; REALESTATE=1672159640484; wcs_bt=44058a670db444:1672159640',
        'Referer': 'https://m.land.naver.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    params = {
        'hscpNo': c_id,
    }

    response = requests.get(
        'https://m.land.naver.com/complex/getAdditionalBasicInfo',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    
    temp=json.loads(response.text)

    rtype_df=pd.DataFrame()
    type_cnt = len(temp["ptpMnexPtpAtclCntInfoList"])
  
    for nt in range(type_cnt):
      r_type=temp["ptpMnexPtpAtclCntInfoList"][nt]["ptpInfo"]
      type_tmp2=pd.DataFrame(data=r_type,index=[nt])
      rtype_df = rtype_df.append(type_tmp2)
      rtype_df

    rtype_df = rtype_df[["ptpNo","ptpNm","exclsSpc"]]
    
    price_range_df=pd.DataFrame()
    type_cnt = len(temp["ptpMnexPtpAtclCntInfoList"])

    for nt2 in range(type_cnt):
      try:
        apt_price=temp["ptpMnexPtpAtclCntInfoList"][nt2]["ptpAtclCntInfo"]
        type_tmp1=pd.DataFrame(data=apt_price,index=[nt2])
        price_range_df = price_range_df.append(type_tmp1)
      except:
        price_range_df = price_range_df

    price_range_df = price_range_df[["ptpNo","dealPriceMin","dealPriceMax","leasePriceMin","leasePriceMax"]]

    naver_info=pd.DataFrame()
    naver_price_info = pd.DataFrame()
    
    naver_info = pd.merge(rtype_df,price_range_df, on ="ptpNo")

    #가격 str -> float로 타입변경 및 억단위
    for p in range(len(naver_info)):
      for q in range(3,7):
        if len(str(naver_info.iloc[p,q])) > 5 : 
          naver_info.iloc[p,q] = str(naver_info.iloc[p,q]).replace("억 ","").replace(",","")
          naver_info.iloc[p,q] = float(naver_info.iloc[p,q])/10000
        else :
          naver_info.iloc[p,q] = str(naver_info.iloc[p,q]).replace("억","0000").replace(",","")
          naver_info.iloc[p,q] =float(naver_info.iloc[p,q])/10000

    #평형 카테고리 재생성
    naver_info["cateSpc"] = naver_info["exclsSpc"].apply(lambda  x : int(float(x)/5)*5) 

    #한 테이블로 카테고리 재생성
    dealPriceMin_Df=pd.DataFrame(naver_info['dealPriceMin'].groupby(naver_info['cateSpc']).min())  
    dealPriceMax_Df=pd.DataFrame(naver_info['dealPriceMax'].groupby(naver_info['cateSpc']).max())  
    leasePriceMin_Df=pd.DataFrame(naver_info['leasePriceMin'].groupby(naver_info['cateSpc']).min())  
    leasePriceMax_Df=pd.DataFrame(naver_info['leasePriceMax'].groupby(naver_info['cateSpc']).max())  
    naver_price_info = pd.merge(dealPriceMin_Df,dealPriceMax_Df, on ="cateSpc")
    naver_price_info = pd.merge(naver_price_info, leasePriceMin_Df, on ="cateSpc")
    naver_price_info = pd.merge(naver_price_info, leasePriceMax_Df, on ="cateSpc")
    
    print(naver_price_info)
       
    return naver_price_info
landcode_list=[
"11590", #서울특별시동작구
"11230",#서울특별시동대문구
"11380",#서울특별시은평구
"11410",#서울특별시서대문구
"11545",#서울특별시금천구
"11500",#서울특별시강서구
"11200",#서울특별시성동구
"11260",#서울특별시중랑구
"11350",#서울특별시노원구
"11530",#서울특별시구로구
"11470",#서울특별시양천구
"11440",#서울특별시마포구
"11290",#서울특별시성북구
"11140",#서울특별시중구
"11560",#서울특별시영등포구
"11305",#서울특별시강북구
"11650",#서울특별시서초구
"11680",#서울특별시강남구
"11215",#서울특별시광진구
"11740",#서울특별시강동구
"11170",#서울특별시용산구
"11110",#서울특별시종로구
"11710",#서울특별시송파구
"11320",#서울특별시도봉구
"11620"#서울특별시관악구
 ]
 

    
#참고 https://eslife.tistory.com/1100

#api key https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15058747
serviceKey = ""
#법정동리스트참고
#연월
ymd = "202302"
#호출수
numrow = 1000

itemList = []

for a in landcode_list:
    url = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD={a}&DEAL_YMD={ymd}&serviceKey={serviceKey}&numOfRows={numrow}'

    res = urllib.request.urlopen(url)
    result = res.read()
    soup = BeautifulSoup(result, 'lxml-xml')
    items = soup.findAll('item')

    keylist = [
        '거래금액',
        '거래유형',
        '건축년도',
        '년',
        '법정동',
        '아파트',
        '월',
        '일',
        '전용면적',
        '지번',
        '지역코드',
        '층',
        '해제사유발생일',
        '해제여부'
    ]

    try:
        for v in items:
            item = {}

            for key in keylist :
                item[key] = v.find(key).text

            item["매매일"] = int(item['년'])*10000 + int(item['년'])*100 + int(item['일'])
            item["거래금액"] = int(item["거래금액"].replace(',',''))
            item["전용면적"] = float(item["전용면적"])
            item["층"] = int(item['층'])
            item["건축년도"] = int(item['건축년도'])
            itemList.append(item)
        print(str(a)+"완료")
    except:
        print(str(a)+"거래없음")

driver = webdriver.Chrome('C:/Users/Louis/Downloads/chromedriver.exe')

for i in range(0,5):
    
    if itemList[i]["전용면적"] > 40 and itemList[i]["전용면적"] < 120 :
    
        print(i)

        #네이버
        driver.get("https://m.land.naver.com/")
        time.sleep(1)

        # 1. 검색버튼 클릭
        elem1 = driver.find_element('xpath','//*[@id="header"]/div/div[2]/a[1]/i')
        elem1.click()
        time.sleep(1)

        # 2. 검색어 입력
        elem2 = driver.find_element('xpath','//*[@id="query"]')
        elem2.send_keys(itemList[i]["법정동"]+" "+itemList[i]["아파트"])
        driver.find_element('xpath','//*[@id="landSearchBtn"]/i').click()
        time.sleep(1)
        naver_url=driver.current_url

        complex_id = naver_url.strip("https://m.land.naver.com/complex/info/")
        complex_id = complex_id[0:8]
        complex_id = complex_id.strip("?")
        complex_id = complex_id.strip("?p")
        complex_id = complex_id.strip("?pt")
        print(complex_id)

        #호갱노노
        query = str(itemList[i]["법정동"]+" "+itemList[i]["아파트"])
        driver.get("https://hogangnono.com/search?q="+query)
        time.sleep(1)

        # 1. 검색버튼 클릭
        elem1 = driver.find_element('xpath','//*[@id="container"]/div[4]/div/div/div[1]/div/ul/li[1]/a/div[1]')
        elem1.click()
        time.sleep(1)

        hogang_url=driver.current_url

        try: 
            naver_price_info=get_apt_prc_range(complex_id)
            cate = int(float(itemList[i]["전용면적"])/5)*5
            print(cate)

            t4= "매매호가: " + str(naver_price_info.loc[int(cate)][0]) + "억~"+ str(naver_price_info.loc[int(cate)][1]) + "억"
            t5= "전세호가: " + str(naver_price_info.loc[int(cate)][2]) + "억~"+ str(naver_price_info.loc[int(cate)][3]) + "억"
            print("네이버 호가 불러오기 성공")

        except:     
            t4= "매매호가: -" 
            t5= "전세호가: -" 

        t1=itemList[i]["월"]+"월"+itemList[i]["일"]+"일 "+itemList[i]["법정동"]+" "+itemList[i]["아파트"]+" "+str(itemList[i]["층"])+"층 전용 "+str(itemList[i]["전용면적"])+"m2가 "+ str(int(itemList[i]["거래금액"])/10000)+"억에 "+str(itemList[i]["거래유형"])+"로 판매"
        t2= "https://m.land.naver.com/search/result/" + itemList[i]["법정동"]+itemList[i]["아파트"]
        t3= hogang_url            
        button1 = InlineKeyboardButton(text="네이버 매물 \U0001F7E2", url=re.sub(r"\s","",t2))
        button2 = InlineKeyboardButton(text="호갱노노 \U0001F7E3", url=re.sub(r"\s","",t3))
        button_t = InlineKeyboardMarkup(inline_keyboard = [[button1, button2]])
        bot.sendMessage(chat_id='-,', text=t1+"\n"+t4+"\n"+t5, reply_markup =button_t)

        print(itemList[i]["법정동"]+" "+itemList[i]["아파트"]+"크롤링 성공")
    
    else:
        print(itemList[i]["아파트"]+"면적 너무 작거나 커서 패스"+str(itemList[i]["전용면적"]))
