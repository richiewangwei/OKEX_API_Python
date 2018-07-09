#!/usr/bin/python
# -*- coding: utf-8 -*-
# 期货合约 程序化交易系统

import time
from FutureConfigure import *
from FutureAPIClient import Ticker, FutureAPIClient
from FutureTechnicalIndicator import *


class FutureTradeSystem:
    def __init__(self):
        self.ticker_infos = []
        self.ma_day_num_group_count = 100
        # btc
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # ltc
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # bch
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # eth
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # etc
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # eos
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract_type':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract_type':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract_type':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)

        pass


    def trade_buy_for_one_contract(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        while True:
            for i in range(len(self.ticker_infos)):
                if (i % self.ma_day_num_group_count) == 0:
                    print ('\n')
                symbol = self.ticker_infos[i]['symbol']
                contract_type = self.ticker_infos[i]['contract_type']
                type = self.ticker_infos[i]['type']
                klinelist = future_api_client.get_kline(symbol, contract_type, type)
                if len(klinelist.klinelist) < 10:
                    print(str(self.ticker_infos[i]) + '\tFuture_API_Client_ERROR!')
                    continue
                tech_indicat = FutureTechnicalIndicator(klinelist)
                ma_day_num = self.ticker_infos[i]['ma_day_num']
                obv_simple = OBV_Simple(tech_indicat.vol_list, tech_indicat.close_list, ma_day_num)
                buy_count = 0
                buy_price_sum = 0.0
                last_buy_price = 0.0
                sell_count = 0
                sell_price_sum = 0.0
                last_sell_price = 0.0
                profit_sum = 0.0
                for j in range(len(tech_indicat.close_list)):
                    s = ''
                    s += '[%d]' % j
                    s += '\t\t%.2f' % obv_simple.close_list[j]
                    s += '\t\t%d' % (obv_simple.vol_list[j] / 10000)
                    s += '\t\t%d' % (obv_simple.obv_list[j] / 10000)
                    s += '\t\t%d' % (obv_simple.ma_obv_list[j] / 10000)
                    if obv_simple.ma_obv_list[j] > obv_simple.ma_obv_list[j-1]:
                        s += '\t\t     +++++'
                        if j - 2 >= 0 and obv_simple.ma_obv_list[j-1] < obv_simple.ma_obv_list[j-2]:
                            s += '\t\tBuy'
                            last_buy_price = obv_simple.close_list[j]
                            if last_sell_price > 0:
                                sell_count += 1
                                sell_price_sum += last_sell_price
                                buy_count += 1
                                buy_price_sum += obv_simple.close_list[j]
                                s += '\t\t%+.2f' % (last_sell_price - last_buy_price)
                                s += ' =%.2f-%.2f' % (last_sell_price, last_buy_price)
                                profit_sum += last_sell_price - last_buy_price
                                s += '\t\tsum= %+.2f' % profit_sum
                                #print(s)
                    else:
                        s += '\t\t-----     '
                        if j - 2 >= 0 and obv_simple.ma_obv_list[j-1] > obv_simple.ma_obv_list[j-2]:
                            s += '\t\tSell'
                            last_sell_price = obv_simple.close_list[j]
                            if last_buy_price > 0:
                                buy_count += 1
                                buy_price_sum += last_buy_price
                                sell_count += 1
                                sell_price_sum += obv_simple.close_list[j]
                                s += '\t\t%+.2f' % (last_sell_price - last_buy_price)
                                s += ' =%.2f-%.2f' % (last_sell_price, last_buy_price)
                                profit_sum += last_sell_price - last_buy_price
                                s += '\t\tsum= %+.2f' % profit_sum
                                #print(s)
                        
                    #print(s)
                s = ''
                s += str(self.ticker_infos[i])
                s += '\tProfit_Sum=\t%+6.2f' % profit_sum
                s += '\tProfit_Per=\t%+.2f' % (profit_sum / (buy_price_sum / buy_count) * 100)
                s += '%'
                s += '\tBUY_Trade = %3d * %6.2f' % (buy_count, buy_price_sum / buy_count)
                s += '\tSELL_Trade = %3d * %6.2f' % (sell_count, sell_price_sum / sell_count)
                                
                print(s)

                time.sleep(0.5)
            break
        
        pass
    


    def check_Open_Close_Diff(self):
        # init
        self.check_open_close_diff_infos = []
        type_list = ['1week', '3day', '1day', '12hour', '6hour', '4hour', '2hour', '1hour', '30min', '15min', '5min', '3min', '1min']
        # btc
        for type in type_list:
            ticker = { 'symbol':'btc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # ltc
        for type in type_list:
            ticker = { 'symbol':'ltc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # bch
        for type in type_list:
            ticker = { 'symbol':'bch_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # eth
        for type in type_list:
            ticker = { 'symbol':'eth_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # etc
        for type in type_list:
            ticker = { 'symbol':'etc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # eos
        for type in type_list:
            ticker = { 'symbol':'eos_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)

        # Check
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        while True:
            for i in range(len(self.check_open_close_diff_infos)):
                if i % len(type_list) == 0:
                    print('\n\n\n\n\n')
                symbol = self.check_open_close_diff_infos[i]['symbol']
                contract_type = self.check_open_close_diff_infos[i]['contract_type']
                type = self.check_open_close_diff_infos[i]['type']
                klinelist = future_api_client.get_kline(symbol, contract_type, type)
                if len(klinelist.klinelist) < 10:
                    print(str(self.check_open_close_diff_infos[i]) + '\tFuture_API_Client_ERROR!')
                    continue
                tech_indicat = FutureTechnicalIndicator(klinelist)
                open_close_diff = Open_Close_Diff(tech_indicat.open_list, tech_indicat.close_list)
                
                s = ''
                s += str(self.check_open_close_diff_infos[i])
                s += '\nclose_price_count= %d' % len(tech_indicat.close_list)
                s += '\top_cl_same_count= %d' % open_close_diff.open_close_same_count
                s += '\top_cl_diff_count= %d' % open_close_diff.open_close_diff_count
                s += '\tsame_diff_sum= %d' % (open_close_diff.open_close_same_count + open_close_diff.open_close_diff_count)
                s += '\nop_cl_all_same= %d' % open_close_diff.open_close_all_same_count
                s += '\top_cl_all_diff= %d' % open_close_diff.open_close_all_diff_count
                s += '\tprof_all_same= %.2f' % open_close_diff.profit_all_same
                s += '\tprofit_all_diff  = %.2f' % open_close_diff.profit_all_diff
                s += '\tprof_diff/same= %.2f' % (open_close_diff.profit_all_diff / open_close_diff.profit_all_same * 100)
                s += '%'
                s += '\tprof_diff-same= %.2f' % (open_close_diff.profit_all_diff - open_close_diff.profit_all_same)
                s += '\tclose_avg= %.2f' % (sum(tech_indicat.close_list) / len(tech_indicat.close_list))
                s += '\tprofit_percent= %.2f' % ((open_close_diff.profit_all_diff - open_close_diff.profit_all_same) / (sum(tech_indicat.close_list) / len(tech_indicat.close_list)) * 100)
                s += '%'
                s += '\n'
                print(s)

                time.sleep(1)
            break
        
        pass

        


if __name__ == '__main__':
    future_trade_system = FutureTradeSystem()
    future_trade_system.trade_buy_for_one_contract()


    # Check Open_Close_Diff
    #future_trade_system.check_Open_Close_Diff()


            
            
