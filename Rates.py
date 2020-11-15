from send_email import send
import pandas as pd
import bar
import time
import Rates
from datetime import date, timedelta, datetime
import datetime
import pdb



def main():
    start_time = time.time()
    df_old = pd.read_pickle('last_data')
    t0=df_old.iloc[0,0]
    t1=str(datetime.datetime.now())[0:19]
    df_new=bar.main()
    #df_new = df_old.drop('Time',axis=1)
    #pdb.set_trace()
    names=['Golomt','Khaan','TDB','Xac','State']
    df_diff=df_new[names]-df_old[names]
    if True:
    #if df_diff[names].sum().sum()!=0:
        df_new.insert(loc=0, column='Time', value=t1)
        df_to_save=df_new.copy()
        df_send=df_new.copy()
        cnames = [name + " Change" for name in names]
        df_send[cnames]=df_diff[names]
        send(df_send,t0,t1)  
        df_to_save.to_pickle('last_data')
        dfbase = pd.read_pickle('historical_data')
        dfbase=dfbase.append(df_to_save,sort=False,ignore_index=True)
        dfbase.to_pickle('historical_data')          
    print("--- %s seconds ---" % (time.time() - start_time))
    # time.sleep(60*1)
    # Rates.main()


if __name__ == "__main__":
    main()    

# import pandas as pd
# df_new.insert(loc=0, column='Time', value=t1)
# df_new.to_pickle('last_data')
# df_new.to_pickle('historical_data') 
# dfbase = pd.read_pickle('last_data')
# dfbase = pd.read_pickle('historical_data')
# import pandas as pd
# from send_email import send
# df=pd.DataFrame({'meow': [10,20],'bibi': [23,27]})    

