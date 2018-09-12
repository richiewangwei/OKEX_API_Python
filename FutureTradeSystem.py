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
        self.ticker_infos_list = []
        self.ma_day_num_group_count = 100
        # btc
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'btc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        # ltc
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'ltc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        # bch
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'bch_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        # eth
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eth_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        # etc
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'etc_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        # eos
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'1hour', 'ma_day_num':(i + 1) * 1 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'30min', 'ma_day_num':(i + 1) * 2 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)
        self.ticker_infos = []
        for i in range(self.ma_day_num_group_count):
            ticker = { 'symbol':'eos_usd', 'contract':'quarter', 'type':'15min', 'ma_day_num':(i + 1) * 4 }
            self.ticker_infos.append(ticker)
        self.ticker_infos_list.append(self.ticker_infos)

        pass



    def trade_buy_for_one_contract(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        while True:
            for k in range(len(self.ticker_infos_list)):
                print('\n')
                time.sleep(1)
                self.ticker_infos = self.ticker_infos_list[k]
                symbol = self.ticker_infos[0]['symbol']
                contract_type = self.ticker_infos[0]['contract']
                type = self.ticker_infos[0]['type']
                klinelist = future_api_client.get_kline(symbol, contract_type, type)
                if len(klinelist.klinelist) < 10:
                    print(str(self.ticker_infos[0]) + '\tFuture_API_Client_ERROR!\n\n')
                    continue
                tech_indicat = FutureTechnicalIndicator(klinelist)

                obv_simple_list = []
                for i in range(len(self.ticker_infos)):
                    ma_day_num = self.ticker_infos[i]['ma_day_num']
                    obv_simple = OBV_Simple(tech_indicat.vol_list, tech_indicat.close_list, ma_day_num)
                    obv_simple_list.append(obv_simple)

                order_count_list = []
                for j in range(len(tech_indicat.close_list)):
                    order_count_list.append(0)
                    if j == 0:
                        continue
                    for i in range(len(obv_simple_list)):
                        if obv_simple_list[i].ma_obv_list[j] > obv_simple_list[i].ma_obv_list[j-1]:
                            order_count_list[j] += 1
                        else:
                            order_count_list[j] -= 1

                profit_sum = 0.0
                order_list = []
                for j in range(len(tech_indicat.close_list)):
                    for i in range(len(obv_simple_list)):
                        if i < len(obv_simple_list) - 1:
                            continue
                        else:
                            s = ''
                            s += str(self.ticker_infos[i])
                            s += ' close[%d]' % j
                            s += ' ma_day[%d]' % self.ticker_infos[i]['ma_day_num']
                            s += ' %.2f' % obv_simple_list[i].close_list[j]
                            s += ' %d' % (obv_simple_list[i].vol_list[j] / 10000)
                            s += ' %d' % (obv_simple_list[i].obv_list[j] / 10000)
                            s += ' %d' % (obv_simple_list[i].ma_obv_list[j] / 10000)
                            diff_order_count = 0
                            if j == 0:
                                diff_order_count = order_count_list[j]
                            else:
                                diff_order_count = order_count_list[j] - order_count_list[j-1]
                            s += ' %+2d' % order_count_list[j]
                            s += ' %+2d' % diff_order_count
                            stat_orders = Stat_Orders()
                            closed_profit = stat_orders.trade_orders(order_list, diff_order_count, obv_simple_list[i].close_list[j])
                            opened_profit = stat_orders.profit_opened_orders(order_list, obv_simple_list[i].close_list[j])
                            profit_sum += closed_profit                            
                            s += '\tclo_prof_one=\t%+6.2f' % closed_profit
                            s += '\tProfit_Sum=\t%+6.2f' % (profit_sum + opened_profit)
                            s += '\tclo_prof_all=\t%+6.2f' % profit_sum
                            s += '\topn_prof_one=\t%+6.2f' % opened_profit
                            #s += '\torder_list=%s' % str(order_list)
                            if j % 24 == 0:
                                print(s)
                            if j == len(tech_indicat.close_list) - 1:
                                print(s)
                    #print()

                print('----------------------------Game Over----------------------------\n\n')
            break
        
        pass
    



if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    future_trade_system = FutureTradeSystem()
    future_trade_system.trade_buy_for_one_contract()






