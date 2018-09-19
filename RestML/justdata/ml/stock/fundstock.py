import pandas as pd
import quandl
from justdata.ml.stock.quandl_api_key import MyQuandlKey 
import matplotlib.pyplot as plt



class FundaHelper:


    def __init__(self,ticker='AAPL'):
        self.ticker = ticker 
        quandl.ApiConfig.api_key = MyQuandlKey.api_key



    def get_zack_funda(self):
        funda_pd = quandl.get_table('ZACKS/CP', ticker=self.ticker)
        return funda_pd.to_json(orient='records')


# funda_list_cols= ['comp_name','pe_ratio_f1','pe_ratio_12m','curr_ratio_q0','quick_ratio_q0',
# 'debt_to_comm_equ_q0','eps_act_fr0','shares_out','zacks_oper_margin_q0']

# #test


# quandl.ApiConfig.api_key = MyQuandlKey.api_key

# tck= 'IBM'
# ticker_pd = quandl.get_table('ZACKS/FR',ticker=tck,paginate=True)
# funda_pd = quandl.get_table('ZACKS/CP', ticker=tck)

#print(funda_pd)
# print(funda_pd[funda_list_cols])
# print(funda_pd[['per_end_date_qr0','pe_ratio_f1','debt_to_comm_equ_q0']])
#print(ticker_pd.head(10))
# json_f = funda_pd.to_json(orient='records')
# print(json_f)
# print(ticker_pd.columns)
# ticker_pd = ticker_pd.set_index(['per_end_date'])

# print(ticker_pd)
# y_q_pd = ticker_pd.loc[ticker_pd['per_fisc_year'].isin([2017,2018])]

# y_q_pd.sort_index(inplace=True)
# print(y_q_pd[['tot_debt_tot_equity','profit_margin','free_cash_flow','book_val_per_share']])

# print(y_q_pd['tot_debt_tot_equity'])
# print(y_q_pd['free_cash_flow'])
# print(y_q_pd['book_val_per_share'])
# print(y_q_pd['profit_margin'])

# plt.figure(1)
# y_q_pd['tot_debt_tot_equity'].plot()
# plt.show()
# plt.figure(2)
# y_q_pd['free_cash_flow'].plot()
# plt.show()
# plt.figure(3)
# y_q_pd['book_val_per_share'].plot()
# plt.show()
# plt.figure(4)
# y_q_pd['profit_margin'].plot()
# plt.show()