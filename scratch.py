from gm.api import *
import numpy as np
import pandas as pd
import datetime
set_token('bf794f5409a2c2711212dccff14c47653495d8e5')
day_time,hour_and_mins=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).split(" ")
symbol_list=pd.read_table("C:/Users\hp\Desktop/Table.txt")
symbol_list=symbol_list.index
symbol=[]
for i in symbol_list:
    symbol.append(i.replace('SZ','SZSE.').replace('SH','SHSE.'))
df = get_fundamentals_n(table="cashflow_statement", symbols=symbol, end_date=day_time, fields="FINCASHINFL",count=1, df=True)
total=pd.DataFrame()
total['代码名称']=symbol
total['筹资量']=df.FINCASHINFL
df = get_fundamentals_n(table="cashflow_statement", symbols=symbol, end_date=day_time, fields="FINNETCFLOW",count=1, df=True)
total['筹资活动产生的现金流量净额']=df.FINNETCFLOW
df = get_fundamentals_n(table="cashflow_statement", symbols=symbol, end_date=day_time, fields="INCRCASHPLED",count=1, df=True)

'272420ecb8e69d441ef029a57e709d4319ddc271793b8d8a7ee4b7ff'
