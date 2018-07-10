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



    def Check_Open_Close_Diff(self):
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



    def Simple_Open_Close_Policy_V1(self, open_list, close_list):
        self.open_list = open_list
        self.close_list = close_list
        self.open_close_same_count = 0
        self.open_close_diff_count = 0
        self.open_close_all_same_count = 0
        self.open_close_all_diff_count = 0
        self.profit_all_same = 0.0
        self.profit_all_diff = 0.0

        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]) or \
               (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                self.open_close_same_count += 1
            else:
                self.open_close_diff_count += 1

        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i] and self.open_list[i] > self.close_list[i-1]) or \
               (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i] and self.open_list[i] < self.close_list[i-1]):
                self.open_close_all_same_count += 1
                self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
            else:
                self.open_close_all_diff_count += 1
                self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
                
        s = ''
        s += 'close_price_count= %d' % len(self.close_list)
        s += '\top_cl_same_count= %d' % self.open_close_same_count
        s += '\top_cl_diff_count= %d' % self.open_close_diff_count
        s += '\tsame_diff_sum= %d' % (self.open_close_same_count + self.open_close_diff_count)
        s += '\n'
        s += 'op_cl_all_same= %d' % self.open_close_all_same_count
        s += '\top_cl_all_diff= %d' % self.open_close_all_diff_count
        s += '\tprof_all_same= %.2f' % self.profit_all_same
        s += '\tprof_all_diff  = %.2f' % self.profit_all_diff
        s += '\tprof_diff/same= %.2f' % (self.profit_all_diff / self.profit_all_same * 100)
        s += '%'
        s += '\tprof_diff-same= %.2f' % (self.profit_all_diff - self.profit_all_same)
        s += '\tclose_avg= %.2f' % (sum(self.close_list) / len(self.close_list))
        s += '\tprofit_percent= %.2f' % ((self.profit_all_diff - self.profit_all_same) / (sum(self.close_list) / len(self.close_list)) * 100)
        s += '%'
        s += '\n'

        return s



    def Simple_Open_Close_System_V1(self):
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

                s = ''
                s += str(self.check_open_close_diff_infos[i])
                s += '\n'                
                tech_indicat = FutureTechnicalIndicator(klinelist)
                s += self.Simple_Open_Close_Policy_V1(tech_indicat.open_list, tech_indicat.close_list)
                
                print(s)

                time.sleep(1)
            break
        
        pass
        


    def Simple_Open_Close_Policy(self, open_list, close_list):
        self.open_list = open_list
        self.close_list = close_list
        self.open_close_same_count = 0
        self.open_close_diff_count = 0
        self.open_close_all_same_count = 0
        self.open_close_all_diff_count = 0
        self.profit_all_same = 0.0
        self.profit_all_diff = 0.0
        self.DIFF_COUNT = 0
        self.DIFF_PROFIT = 0.0
        self.COUNT = [0, 0, 0, 0, 0, 0 ,0]
        self.PROFIT = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.PERCENT = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]) or \
               (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                self.open_close_same_count += 1
            else:
                self.open_close_diff_count += 1

        '''
        # V1
        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i] and self.open_list[i] > self.close_list[i-1]) or \
               (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i] and self.open_list[i] < self.close_list[i-1]):
                self.open_close_all_same_count += 1
                self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
            else:
                self.open_close_all_diff_count += 1
                self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
        '''
        '''
        # V2.1
        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                if (self.open_list[i] > self.close_list[i-1]):
                    # Sell 亏
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Buy 盈
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
            elif (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                if (self.open_list[i] < self.close_list[i-1]):
                    # Buy 亏
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Sell 盈
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
            else:
                self.DIFF_COUNT += 1
                self.DIFF_PROFIT += abs(self.close_list[i] - self.open_list[i])
        # V2.2
        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                if (self.open_list[i] > self.close_list[i-1]):
                    # Sell 亏
                    self.COUNT[0] += 1
                    self.PROFIT[0] += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Buy 盈
                    self.COUNT[1] += 1
                    self.PROFIT[1] += abs(self.close_list[i] - self.open_list[i])
            elif (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                if (self.open_list[i] < self.close_list[i-1]):
                    # Buy 亏
                    self.COUNT[2] += 1
                    self.PROFIT[2] += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Sell 盈
                    self.COUNT[3] += 1
                    self.PROFIT[3] += abs(self.close_list[i] - self.open_list[i])
            else:
                self.COUNT[4] += 1
                self.PROFIT[4] += abs(self.close_list[i] - self.open_list[i])
        '''
        '''
        # V3.1
        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                if (self.open_list[i] > self.close_list[i-1]):
                    # Sell 亏
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Buy 盈
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
            elif (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                if (self.open_list[i] < self.close_list[i-1]):
                    # Buy 亏
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])
                else:
                    # Sell 盈
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])
            else:
                self.DIFF_COUNT += 1
                self.DIFF_PROFIT += abs(self.close_list[i] - self.open_list[i])
        # V3.2
        for i in range(1, len(self.close_list)):
            if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                if (self.open_list[i] > self.close_list[i-1]):
                    # Sell 亏
                    self.COUNT[0] += 1
                    self.PROFIT[0] += abs(self.close_list[i] - self.open_list[i])
                    self.PERCENT[0] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
                elif (self.open_list[i] < self.close_list[i-1]):
                    # Buy 盈
                    self.COUNT[1] += 1
                    self.PROFIT[1] += abs(self.close_list[i] - self.open_list[i])
                    self.PERCENT[1] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
                else:
                    self.COUNT[2] += 1
                    self.PROFIT[2] += abs(self.close_list[i] - self.open_list[i])                    
                    self.PERCENT[2] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
            elif (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                if (self.open_list[i] < self.close_list[i-1]):
                    # Buy 亏
                    self.COUNT[3] += 1
                    self.PROFIT[3] += abs(self.close_list[i] - self.open_list[i])
                    self.PERCENT[3] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
                elif (self.open_list[i] > self.close_list[i-1]):
                    # Sell 盈
                    self.COUNT[4] += 1
                    self.PROFIT[4] += abs(self.close_list[i] - self.open_list[i])
                    self.PERCENT[4] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
                else:
                    self.COUNT[5] += 1
                    self.PROFIT[5] += abs(self.close_list[i] - self.open_list[i])                    
                    self.PERCENT[5] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
            else:
                self.COUNT[6] += 1
                self.PROFIT[6] += abs(self.close_list[i] - self.open_list[i])
                self.PERCENT[6] += abs(self.close_list[i] - self.open_list[i]) / self.open_list[i] * 100
        '''

        '''
        # V4.1
        for i in range(1, len(self.close_list)):
            if (self.open_list[i] > self.close_list[i-1]):
                # Sell
                if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])     # 盈
            else:
                # Buy
                if (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])     # 盈
        # V4.2
        for i in range(1, len(self.close_list)):
            if (self.open_list[i] > self.close_list[i-1]):
                # Sell
                if (self.close_list[i] > self.close_list[i-1] and self.close_list[i] > self.open_list[i]):
                    self.COUNT[0] += 1
                    self.PROFIT[0] += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.COUNT[3] += 1
                    self.PROFIT[3] += abs(self.close_list[i] - self.open_list[i])     # 盈
            else:
                # Buy
                if (self.close_list[i] < self.close_list[i-1] and self.close_list[i] < self.open_list[i]):
                    self.COUNT[2] += 1
                    self.PROFIT[2] += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.COUNT[1] += 1
                    self.PROFIT[1] += abs(self.close_list[i] - self.open_list[i])     # 盈
        '''
        
        # V5
        for i in range(1, len(self.close_list)):
            if (self.open_list[i] >= self.close_list[i-1]):
                # Sell
                # open[i] == close[i-1] 归为 Sell
                if (self.close_list[i] > self.open_list[i]):
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])     # 盈
            else:
                # Buy
                if (self.close_list[i] < self.open_list[i]):
                    self.open_close_all_same_count += 1
                    self.profit_all_same += abs(self.close_list[i] - self.open_list[i])     # 亏
                else:
                    self.open_close_all_diff_count += 1
                    self.profit_all_diff += abs(self.close_list[i] - self.open_list[i])     # 盈
        
                
        s = ''
        s += 'close_price_count= %d' % len(self.close_list)
        s += '\top_cl_same_count= %d' % self.open_close_same_count
        s += '\top_cl_diff_count= %d' % self.open_close_diff_count
        s += '\tsame_diff_sum= %d' % (self.open_close_same_count + self.open_close_diff_count)
        s += '\n'
        s += 'op_cl_all_same= %d' % self.open_close_all_same_count
        s += '\top_cl_all_diff= %d' % self.open_close_all_diff_count
        s += '\tprof_all_same= %.2f' % self.profit_all_same
        s += '\tprof_all_diff  = %.2f' % self.profit_all_diff
        s += '\tprof_diff/same= %.2f' % (self.profit_all_diff / self.profit_all_same * 100)
        s += '%'
        s += '\tprof_diff-same= %.2f' % (self.profit_all_diff - self.profit_all_same)
        s += '\nclose_avg= %.2f' % (sum(self.close_list) / len(self.close_list))
        s += '\tprofit_percent= %.2f' % ((self.profit_all_diff - self.profit_all_same) / (sum(self.close_list) / len(self.close_list)) * 100)
        s += '%'
        s += '\tDIFF_COUNT= %d' % self.DIFF_COUNT
        s += '\tDIFF_PROFIT= %.2f' % self.DIFF_PROFIT
        # For V3
        s += '\n'
        s += 'COUNT[]=     \t%d\t%d\t%d\t\t\t%d\t%d\t%d\t\t\t%d' % (self.COUNT[0], self.COUNT[1], self.COUNT[2], self.COUNT[3], self.COUNT[4], self.COUNT[5], self.COUNT[6])
        s += '\nPROFIT[]=  \t%d\t%d\t%d\t\t\t%d\t%d\t%d\t\t\t%d' % (self.PROFIT[0], self.PROFIT[1], self.PROFIT[2], self.PROFIT[3], self.PROFIT[4], self.PROFIT[5], self.PROFIT[6])
        s += '\nPERCENT[]= \t%d\t%d\t%d\t\t\t%d\t%d\t%d\t\t\t%d' % (self.PERCENT[0], self.PERCENT[1], self.PERCENT[2], self.PERCENT[3], self.PERCENT[4], self.PERCENT[5], self.PERCENT[6])
        s += '\nCOUNT_sum=   \t%d' % (abs(self.COUNT[0] + self.COUNT[3] - self.COUNT[1] - self.COUNT[4]) + abs(self.COUNT[2] - self.COUNT[5]))
        s += '\nPROFIT_sum=  \t%d' % (abs(self.PROFIT[0] + self.PROFIT[3] - self.PROFIT[1] - self.PROFIT[4]) + abs(self.PROFIT[2] - self.PROFIT[5]))
        s += '\nPERCENT_sum= \t%d' % (abs(self.PERCENT[0] + self.PERCENT[3] - self.PERCENT[1] - self.PERCENT[4]) + abs(self.PERCENT[2] - self.PERCENT[5]))
        s += '\n'

        return s



    def Simple_Open_Close_System(self):
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

                s = ''
                s += str(self.check_open_close_diff_infos[i])
                s += '\n'                
                tech_indicat = FutureTechnicalIndicator(klinelist)
                s += self.Simple_Open_Close_Policy(tech_indicat.open_list, tech_indicat.close_list)
                
                print(s)

                time.sleep(1)
            break
        
        pass
        



if __name__ == '__main__':
    future_trade_system = FutureTradeSystem()

    # Check Open_Close_Diff as Test Benchmark
    #future_trade_system.Check_Open_Close_Diff()

    # Simple Open Close Policy V1
    #future_trade_system.Simple_Open_Close_System_V1()

    # Simple Open Close Policy
    future_trade_system.Simple_Open_Close_System()

    pass




