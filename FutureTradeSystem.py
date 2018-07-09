#!/usr/bin/python
# -*- coding: utf-8 -*-
# 期货合约 程序化交易系统

import time
from FutureConfigure import *
from FutureAPIClient import Ticker, FutureAPIClient
from FutureTechnicalIndicator import *


class FutureTradeSystem:
    def __init__(self):
        self.check_open_close_diff_infos = []
        self.type_list = ['1week', '3day', '1day', '12hour', '6hour', '4hour', '2hour', '1hour', '30min', '15min', '5min', '3min', '1min']
        # btc
        for type in self.type_list:
            ticker = { 'symbol':'btc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # ltc
        for type in self.type_list:
            ticker = { 'symbol':'ltc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # bch
        for type in self.type_list:
            ticker = { 'symbol':'bch_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # eth
        for type in self.type_list:
            ticker = { 'symbol':'eth_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # etc
        for type in self.type_list:
            ticker = { 'symbol':'etc_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)
        # eos
        for type in self.type_list:
            ticker = { 'symbol':'eos_usd', 'contract_type':'quarter', 'type':type}
            self.check_open_close_diff_infos.append(ticker)

        pass




    def check_Open_Close_Diff(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        while True:
            for i in range(len(self.check_open_close_diff_infos)):
                if i % len(self.type_list) == 0:
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
                s += '\n'
                s += 'close_price_count= %d' % len(tech_indicat.close_list)
                s += '\top_cl_same_count= %d' % open_close_diff.open_close_same_count
                s += '\top_cl_diff_count= %d' % open_close_diff.open_close_diff_count
                s += '\tsame_diff_sum= %d' % (open_close_diff.open_close_same_count + open_close_diff.open_close_diff_count)
                s += '\n'
                s += 'op_cl_all_same= %d' % open_close_diff.open_close_all_same_count
                s += '\top_cl_all_diff= %d' % open_close_diff.open_close_all_diff_count
                s += '\tprof_all_same= %.2f' % open_close_diff.profit_all_same
                s += '\tprof_all_diff  = %.2f' % open_close_diff.profit_all_diff
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

    # Check Open_Close_Diff
    future_trade_system.check_Open_Close_Diff()


            
            
