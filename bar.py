# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:55:19 2018

@author: Sugar2
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:27:25 2018

@author: Sugar2
"""


import pandas as pd
import os
import glob
import time
import numpy as np
from datetime import date, timedelta, datetime
from time import gmtime, strftime
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from dateutil import tz
import pdb

chrome_options = Options()
#chrome_options.add_argument("--headless")

#Road to 4 bonds maturing in 2023-2024 are closed as there's empty range before. To get my results, run the code once with 2022-12-14 - 2025-01-01 range. I'll figure out
#better way to handle ranges :)

# Set the time interval

def main():

    #the driver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(20)
    
    
    urls=["Golomt","https://www.golomtbank.com/en/exchange",
           "Khaan", "https://www.khanbank.com/mn/personal/currency-rate",
           "TDB", "http://www.tdbm.mn/en/exchange",
           "Xac", "https://www.xacbank.mn/calculator/rates?lang=en",
           # "UBCB", "http://www.ubcbank.mn/index.php?con=rate",
           "State", "https://statebank.mn/pages/exchange"]
    
    tables=["//*[@id='__next']/div[2]/section[1]/div/div/div[2]/table/tbody/tr[1]/td[1]",
            "/html/body/app-root/app-site-container/app-currency-rate-page/section/div/div[3]/div/div[2]/table/tbody/tr[1]/td[1]",
            "//*[@id='exchange-table-result']/table/tbody/tr[3]/td[1]",
            "//*[@id='rate_table']/tbody/tr[1]/td[1]",
            # "//*[@id='liRateHist']/div/table/tbody/tr[4]/td[1]", 
            "/html/body/div[3]/div/div[1]/table/tbody/tr[1]/td[1]"]

    df=pd.DataFrame({'Валютын код': [],'(C)ash/(N)on(C)ash': [],'(B)uy/(S)ell': []})
    for bank in range(0,len(urls)//2):
        gg=urls[2*bank+1]
        ggt=tables[bank]
        lggt=list(ggt)
        lrc=lggt[0:len(lggt)-9]
        lrc="".join(lrc)
        lcc=lggt[0:len(lggt)-3]
        lcc="".join(lcc)
        if bank == 2:
            mag1=2
            mag2=0
        else:
            mag1=0
            mag2=0
        

        driver.get(gg)
        #pdb.set_trace()
        rc=len(driver.find_elements_by_xpath(lrc))-mag2
        #if bank ==0:
            #driver.find_element_by_xpath("//*[@id='__next']/div[2]/section[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[7]").click()
            #driver.find_element_by_xpath("//*[@id='__next']/div[2]/section[1]/div/div/div[1]/div/div[1]/div/input").clear()
            #driver.find_element_by_xpath("//*[@id='__next']/div[2]/section[1]/div/div/div[1]/div/div[1]/div/input").send_keys("11/14/2020")
        cc=len(driver.find_elements_by_xpath(lcc))
        
        print("Bank number: ", bank)
        #pdb.set_trace()
        my_list=[]
        currency_code=[]
        for n in range(1+mag1,rc+1):        
            for m in range(cc-3,cc+1):
                lggt[len(ggt)-8]=str(n)
                lggt[len(ggt)-2]=str(m)
                path="".join(lggt)
                lggt[len(ggt)-2]=str(1) if bank != 0 else str(3)
                #c_path="".join(lggt)
                c_path="".join(lggt) if bank != 0 else "".join(lggt)
                # + '/strong'
                table_data=driver.find_element_by_xpath(path).text.replace(",","")
                if table_data=="-":
                    table_data=0
                else:
                    table_data=float(table_data)
                #pdb.set_trace()
                cur_code=driver.find_element_by_xpath(c_path).text
                    
                my_list.append(table_data)
                currency_code.append(cur_code)
                # print(table_data,end=" ")
            # print("")
        # fetch_time=str(datetime.datetime.now()+timedelta(hours=6))[0:19]
        # fetch_time = [fetch_time]*4*(rc-mag1)
        side=['B','S']*2*(rc-mag1)
        if bank in (2,4):   
            tip=['NC','NC','C','C']*(rc-mag1)
        else: 
            tip=['C','C','NC','NC']*(rc-mag1)
            
#        bank=['1']*4*(rc-mag1)
        mdat=pd.DataFrame({"Валютын код": currency_code,'(C)ash/(N)on(C)ash': tip, '(B)uy/(S)ell': side, urls[2*bank]: my_list})
#        mdat=pd.DataFrame({'Time': fetch_time,'currency': currency_code,'tip': tip, 'side': side,'rates': my_list,'bank': bank})
        df = pd.merge(df, mdat, how='outer', on=["Валютын код",'(C)ash/(N)on(C)ash','(B)uy/(S)ell'])
        df.fillna(0)
        df[urls[2*bank]]=pd.to_numeric(df[urls[2*bank]])
        # print(df)     
    driver.close()
    return df
    time.sleep(1)
 
if __name__ == "__main__":
    main()