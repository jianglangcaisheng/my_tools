
import tushare as ts

ts.set_token('fc03c47e5211620b6c3df5720f13493e6e36d020fb411866d33a8556')

pro = ts.pro_api()

# df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')

df = pro.btc_marketcap(start_date='20210101', end_date='20210107')

data = ts.get_today_all()

df = pro.query('daily_basic', ts_code='', trade_date='20180726',
               fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')

dlt = 0
