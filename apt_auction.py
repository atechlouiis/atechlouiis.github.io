import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

#2주치 하루씩 긁어오기 한페이지에 최대 40건
#전체데이터
a_tot = pd.DataFrame()
si=pd.read_csv("D:daepyosido_auction.csv")

for do in range(len(si)):
    print(si.labelsigu[do])
    print(str(si.sido[do]))
    print(str(si.sigu[do]))
    
    for p in range(13,14): 
            try:
                day2 = datetime.today()+timedelta(days=p)
                StartDt=day2.strftime('%Y.%m.%d')

                cookies = {
                    'WMONID': 'N6AvbfdRfHJ',
                    'realJiwonNm': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8',
                    'rd2Cd': '',
                    'realVowel': '35207_45207',
                    'daepyoSidoCd': str(si.sido[do]),
                    'daepyoSiguCd': str(si.sigu[do]),
                    'toMul': '%BC%AD%BF%EF%B5%BF%BA%CE%C1%F6%B9%E6%B9%FD%BF%F8%2C20210130053594%2C1%2C20230109%2CB%5E',
                    'rd1Cd': '11',
                    'page': 'default40',
                    'JSESSIONID': 'pHq22gaAwxr4Ie0Zw8qhZb681WK15IGxkWpkYHuMEKG20jzGbLw9bPTblalrIc20.amV1c19kb21haW4vYWlzMQ==',
                    'locIdx': '',
                }

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    # 'Cookie': 'WMONID=N6AvbfdRfHJ; realJiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8; daepyoSiguCd=; rd2Cd=; realVowel=35207_45207; daepyoSidoCd=11; toMul=%BC%AD%BF%EF%B5%BF%BA%CE%C1%F6%B9%E6%B9%FD%BF%F8%2C20210130053594%2C1%2C20230109%2CB%5E; rd1Cd=11; page=default40; JSESSIONID=pHq22gaAwxr4Ie0Zw8qhZb681WK15IGxkWpkYHuMEKG20jzGbLw9bPTblalrIc20.amV1c19kb21haW4vYWlzMQ==',
                    'Origin': 'https://www.courtauction.go.kr',
                    'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                }

                data = 'bubwLocGubun=2&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=11&daepyoSiguCd=&daepyoDongCd=&notifyLoc=on&rd1Cd=11&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2023&saSer=&ipchalGbncd=000331&termStartDt='+StartDt+'&termEndDt='+StartDt+'&lclsUtilCd=0000802&mclsUtilCd=000080201&sclsUtilCd=00008020104&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'

                response = requests.post(
                    'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf',
                    cookies=cookies,
                    headers=headers,
                    data=data,
                )

                html = response.content
                soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

                trData=soup.find('tbody')
                trData

                rowList = []
                columnList = []

                auc_tbl = pd.DataFrame ()


                #.replace("\n","").replace("\r","").replace("\t","")
                trDataLen = len(trData.find_all('td'))
                for i in range(0,trDataLen):
                    element=trData.find_all('td')[i].text
                    columnList.append(element)

                trData_n = int(len(columnList)/7)
                for k in range(0,trData_n):
                    df=pd.DataFrame(columnList[0+7*k:7+7*k])   
                    df=df.transpose()
                    df.columns = ['체크','사건번호', '구분', '주소', '비고','가격', '정보']
                    auc_tbl=pd.concat([auc_tbl, df], ignore_index=True)

                a1=auc_tbl['사건번호'].str.split('\r\n\t\t\t', expand=True)
                try: 
                    a1=a1.drop(columns = [3,4])
                except:
                    a1=a1.drop(columns = [3])
                a1.columns= ["index",'법원','사건번호']
                a1['사건번호'] = a1.apply(lambda x : x.사건번호.replace("\n","") , axis = 1 )

                a2=auc_tbl['구분'].str.split('\r\n\t\t\t', expand=True)
                a2=a2.drop(columns = [1])
                a2.columns= ["index",'구분']
                a2['구분'] = a2.apply(lambda x : x.구분.replace("\n","") , axis = 1 )
                a3=auc_tbl['주소'].str.split('\r\n\t\t\t', expand=True)
                a3=a3.drop(columns = [0,2,4])
                a3= a3[[1, 3]]
                a3.columns= ["주소",'넓이']
                a3['주소'] = a3.apply(lambda x : x.주소.replace("\n","").replace("\r","") , axis = 1 )
                a3['넓이'] = a3.apply(lambda x : x.넓이.replace("\n","").replace("\r","").replace("[","").replace("]","") , axis = 1 )
                a4=a3['주소'].str.split('(', expand=True).replace("\n",")")
                a4.columns= ["주소","아파트명"]
                a4["아파트명"] = a4.apply(lambda x : str(x.아파트명).replace(")","") , axis = 1 )
                a3_1 = a3.drop(columns = ["주소"])

                a5=auc_tbl['비고'].str.split('\r\n\t\t\t', expand=True)
                try: 
                    a5=a5.drop(columns = [0,2])
                except:
                    a5=a5
                a5.columns= ["비고"]
                a5['비고'] = a5.apply(lambda x : str(x.비고).replace("\n","").replace("\t","").replace("\r","") , axis = 1 )

                a6=auc_tbl['가격'].str.split('\r\n\t\t\t', expand=True)
                a6=a6.drop(columns = [0,2,4,6])
                a6.columns= ["감정가","최저입찰가","입찰가율"]
                a6['최저입찰가'] = a6.apply(lambda x : str(x.최저입찰가).replace("\r\n","") , axis = 1 )
                a6['입찰가율'] = a6.apply(lambda x : str(x.입찰가율).replace("(","").replace(")","") , axis = 1 )

                a7=auc_tbl['정보'].str.split('\r\n\t\t\t', expand=True)
                a7=a7.drop(columns = [0,2,4])
                a7.columns= ["담당",'경매기일','유찰횟수']
                a7['담당'] = a7.apply(lambda x : x.담당.replace("\r\n","") , axis = 1 )
                a7['유찰횟수'] = a7.apply(lambda x : x.유찰횟수.replace("\t ","").replace("\t","").replace(" \r\n\n","") , axis = 1 )

                a_inf=pd.concat([a1,a2,a4, a3_1,a5,a6,a7], axis=1).drop(columns = ["index"])

                print(StartDt+"엔 물건 존재")

                if p==0:
                    a_tot = a_inf
                    #print(a_tot.iloc[1])
                else:
                    a_tot = a_tot.append(a_inf)
                    #print(a_tot.iloc[1])
            except:
                print(StartDt+"엔 물건 존재 하지 않음")

#구분
a_tot=a_tot[a_tot.구분 == "아파트"]

#시범아파트는 아파트명이 안나오네..
a_tot=a_tot[a_tot.아파트명 != "None"]

#지분있는 물건, 위반건축물 제외
ex_list = ["지분경매", "지분", "공유자", "일괄매각", "지분매각", "공동소유","위반"]
test = '|'.join(ex_list)

a_tot=a_tot[~a_tot.비고.str.contains(test)]
a_tot=a_tot.reset_index(drop=True)

driver = webdriver.Chrome('C:/Users/Louis/Downloads/chromedriver.exe')

for s in range(len(a_tot)):
    driver.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+a_tot["아파트명"][s].replace(",", " "))
    print(a_tot["아파트명"][s].replace(",", " "))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('#main_pack > section.sc_new.sp_nland._prs_lan_clc > div.api_subject_bx._au_nland_apart_single > div._interest_wrap > div.content_group._unit_wrap > div.title_area > div:nth-child(2) > span:nth-child(2)')
    
    time.sleep(1)
    try:
        if len(notices)==0:
            #네이버
            driver.get("https://m.land.naver.com/")
            time.sleep(1)

            # 1. 검색버튼 클릭
            elem1 = driver.find_element('xpath','//*[@id="header"]/div/div[2]/a[1]/i')
            elem1.click()
            time.sleep(1)

            # 2. 검색어 입력
            elem2 = driver.find_element('xpath','//*[@id="query"]')
            elem2.send_keys(a_tot["아파트명"][s].replace(",", " "))
            driver.find_element('xpath','//*[@id="landSearchBtn"]/i').click()
            time.sleep(1)
            naver_url=driver.current_url

            complex_id = naver_url.strip("https://m.land.naver.com/complex/info/")
            complex_id = complex_id[0:8]
            complex_id = complex_id.strip("?")
            complex_id = complex_id.strip("?p")
            complex_id = complex_id.strip("?pt")
            get_apt_n(complex_id)
            apt_n_list.append(a)
            print(complex_id)

        else:
            print("NAVER검색결과 확인 " + str(notices[0]))
    except:
            try:
                driver.get("https://map.naver.com/v5/search/"+a_tot["주소"][s])
                time.sleep(5)
                elem3 = driver.find_element('xpath',' //*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/div/div[2]/div/div[1]/div[3]/div[2]/ul/li[1]/a/div')
                elem3.click()
                time.sleep(1)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                notices = soup.select('#app-root > div > div > div > div:nth-child(6) > div > div:nth-child(2) > div.place_section_content > ul > div:nth-child(4) > li > div > div')
                print(notices[0])
            except:
                print("실패")

                import requests

def get_apt_n(c_id):
        cookies = {
        'SHOW_FIN_BADGE': 'Y',
        'HT': 'HM',
        'NNB': 'NPDROTXIZK7GG',
        'JSESSIONID': '181A0ADBB296501B7A30A71659BB0E49',
        'REALESTATE': '1673448530993',
        'wcs_bt': '44058a670db444:1673448527',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'SHOW_FIN_BADGE=Y; HT=HM; NNB=NPDROTXIZK7GG; JSESSIONID=181A0ADBB296501B7A30A71659BB0E49; REALESTATE=1673448530993; wcs_bt=44058a670db444:1673448527',
            'Referer': 'https://m.land.naver.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
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

        type_cnt = len(temp["ptpMnexPtpAtclCntInfoList"])
        a=0
        for nt2 in range(type_cnt):        
            b=int(temp["ptpMnexPtpAtclCntInfoList"][nt2]["ptpInfo"]["ptybyTotHsehCnt"])
            a=a+b
        print("세대수는 "+str(a))
        return a
#매각결과
import requests

cookies = {
    'WMONID': 'N6AvbfdRfHJ',
    'realJiwonNm': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8',
    'daepyoSiguCd': '',
    'rd2Cd': '',
    'realVowel': '35207_45207',
    'daepyoSidoCd': '11',
    'rd1Cd': '11',
    'page': 'default40',
    'JSESSIONID': 'KBpjFL6xPOHo4sA6wAfqEkUa1X3AUER8KCtcZRm9vFiX5fcQbDAbYtQaHooE1VEw.amV1c19kb21haW4vYWlzMQ==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'WMONID=N6AvbfdRfHJ; realJiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8; daepyoSiguCd=; rd2Cd=; realVowel=35207_45207; daepyoSidoCd=11; rd1Cd=11; page=default40; JSESSIONID=KBpjFL6xPOHo4sA6wAfqEkUa1X3AUER8KCtcZRm9vFiX5fcQbDAbYtQaHooE1VEw.amV1c19kb21haW4vYWlzMQ==',
    'Origin': 'https://www.courtauction.go.kr',
    'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = 'bubwLocGubun=2&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=11&daepyoSiguCd=&daepyoDongCd=&rd1Cd=11&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&mgakAmtGuganMin=&mgakAmtGuganMax=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&mulStatcd=0001302&yuchalCntGuganMin=&yuchalCntGuganMax=&lclsUtilCd=0000802&mclsUtilCd=000080201&sclsUtilCd=00008020104&srnID=PNO102027&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102027&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102027&_NEXT_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_NEXT_SRNID=PNO102028&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'

response = requests.post(
    'https://www.courtauction.go.kr/RetrieveRealEstMgakGyulgwaMulList.laf',
    cookies=cookies,
    headers=headers,
    data=data,
    )

print(response.text)
html = response.content
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

import pandas as pd

trData=soup.find('tbody')
trData

rowList = []
columnList = []

auc_tbl = pd.DataFrame ()


#.replace("\n","").replace("\r","").replace("\t","")
trDataLen = len(trData.find_all('td'))
for i in range(0,trDataLen):
    element=trData.find_all('td')[i].text
    columnList.append(element)

trData_n = int(len(columnList)/7)
for k in range(0,trData_n):
    df=pd.DataFrame(columnList[0+7*k:7+7*k])   
    df=df.transpose()
    df.columns = ['체크','사건번호', '구분', '주소', '비고','가격', '정보']
    auc_tbl=pd.concat([auc_tbl, df], ignore_index=True)
    
a1=auc_tbl['사건번호'].str.split('\r\n\t\t\t', expand=True)      
a1=a1.drop(columns = [0,2,3])
a1=a1[1].str.split('\n', expand=True)        
a1=a1.drop(columns = [2])
a1.columns= ['법원','사건번호']

a2=auc_tbl['구분'].str.split('\r\n\t\t\t', expand=True)
a2=a2.drop(columns = [0])
a2.columns= ['구분']
a2['구분'] = a2.apply(lambda x : x.구분.replace("\n","") , axis = 1 )

a3=auc_tbl['주소'].str.split('\r\n\t\t\t', expand=True)
a3=a3.drop(columns = [0,2,4])
a3.columns= ["주소",'넓이']
a3['주소'] = a3.apply(lambda x : x.주소.replace("\n","").replace("\r","") , axis = 1 )
a3['넓이'] = a3.apply(lambda x : x.넓이.replace("\n","").replace("\r","").replace("[","").replace("]","") , axis = 1 )
a4=a3['주소'].str.split('(', expand=True).replace("\n",")")
a4.columns= ["주소","아파트명"]
a4["아파트명"] = a4.apply(lambda x : str(x.아파트명).replace(")","") , axis = 1 )
a3_1 = a3.drop(columns = ["주소"])

a5=auc_tbl['비고'].str.split('\r\n\t\t\t', expand=True)
a5=a5.drop(columns = [0])
a5.columns= ["비고"]
a5['비고'] = a5.apply(lambda x : str(x.비고).replace("\n","").replace("\t","").replace("\r","") , axis = 1 )

a6=auc_tbl['가격'].str.split('\r\n\t\t\t', expand=True)
a6=a6.drop(columns = [0,2,3])
a6=a6[1].str.split('\n\r\n\r\n\t\t', expand=True)
a6.columns= ["감정가","최저입찰가"]
a6['최저입찰가'] = a6.apply(lambda x : str(x.최저입찰가).replace("\t","").replace("\t1","").replace("\t2","") , axis = 1 )

a7=auc_tbl['정보'].str.split('\r\n\t\t\t', expand=True)
a7=a7.drop(columns = [0,2,4,6])
a7.columns= ["담당",'낙찰일','낙찰가']
a7['담당'] = a7.apply(lambda x : x.담당.replace("\r\n","") , axis = 1 )
a7['낙찰가'] = a7.apply(lambda x : x.낙찰가.replace("\t ","").replace("\t","").replace("매각","") , axis = 1 )

a_inf=pd.concat([a1,a2,a4, a3_1,a5,a6,a7], axis=1)

a_inf
