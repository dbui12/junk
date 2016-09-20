import tia.bbg.datamgr as dm
from tia.bbg import LocalTerminal as lt
import pandas as pd
import numpy as np
import datetime


# Create a DataManager for simpler api access
mgr = dm.BbgDataManager()

## Fetch Data
# MSCI USA
MXUS = mgr['MXUS Index']

#Index member names to members tickers
dirty_member_list = MXUS['INDX_MEMBERS']
dirty_member_list['Member Ticker and Exchange Code'] = dirty_member_list['Member Ticker and Exchange Code'].map(lambda x: str(x)[:-2] + 'US Equity') #Clean the tickers
member_list = np.asarray(dirty_member_list)     #Change list in array
member_list = [l[0] for l in member_list]       #remove double brackets
l = mgr[member_list]                            #MXUS tickers in Data manager

##member_list_arr = np.asarray(member_list)

#Index tickers and weights
dirty_index_weight = MXUS['INDX_MWEIGHT']
dirty_index_weight['Member Ticker and Exchange Code'] = dirty_index_weight['Member Ticker and Exchange Code'].map(lambda x: str(x)[:-2] + 'US Equity')
dirty_index_weight['Percentage Weight'] = dirty_index_weight['Percentage Weight']/100
index_weight = np.asarray(dirty_index_weight)[:,1]
##index_list = np.asarray(dirty_index_list)

#GICS sectors and industries
Sector = l['GICS_SECTOR']
Industry = l['GICS_INDUSTRY_GROUP']

#Price and Full Names
SecName = l['NAME']
Price = l['PX_CLOSE_1D']
if sum(np.asarray(Price)) > 0:
    Price = l['PX_LAST']

#Dividends
now = datetime.datetime.now()
dvd_years = np.arange(now.year-10, now.year-1, 1)
for y in dvd_years:
    datetime.datetime(dvd_years[y],12,31)
