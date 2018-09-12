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
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # ltc
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # bch
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # eth
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # etc
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        # eos
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)

        pass


    def trade_buy_for_one_contract(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        while True:
            for i in range(len(self.ticker_infos)):
                if (i % self.ma_day_num_group_count) == 0:
                    print ('\n')
                symbol = self.ticker_infos[i]['symbol']
                contract_type = self.ticker_infos[i]['contract']
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
                    s += str(self.ticker_infos[i])
                    s += ' close[%d]' % j
                    s += ' ma_day[%d]' % self.ticker_infos[i]['ma_day_num']
                    s += ' %.2f' % obv_simple.close_list[j]
                    s += ' %d' % (obv_simple.vol_list[j] / 10000)
                    s += ' %d' % (obv_simple.obv_list[j] / 10000)
                    s += ' %d' % (obv_simple.ma_obv_list[j] / 10000)
                    if obv_simple.ma_obv_list[j] > obv_simple.ma_obv_list[j-1]:
                        s += '\t     ++++'
                        if j - 2 >= 0 and obv_simple.ma_obv_list[j-1] < obv_simple.ma_obv_list[j-2]:
                            s += '  Buy'
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
                        s += '\t----     '
                        if j - 2 >= 0 and obv_simple.ma_obv_list[j-1] > obv_simple.ma_obv_list[j-2]:
                            s += '  Sell'
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
                s += '\tDiff_Trade=\t%+6.2f' % (sell_price_sum - buy_price_sum)
                s += '\tBUY_Trade=\t%3d\t* %6.2f' % (buy_count, buy_price_sum / buy_count)
                s += '\tSELL_Trade=\t%3d\t* %6.2f' % (sell_count, sell_price_sum / sell_count)
                                
                print(s)

                time.sleep(0.5)
            break
        
        pass
    



if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    future_trade_system = FutureTradeSystem()
    future_trade_system.trade_buy_for_one_contract()






