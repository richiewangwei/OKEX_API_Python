#!/usr/bin/python
# -*- coding: utf-8 -*-
# 期货合约 程序化交易系统

import time
from FutureConfigure import *
from FutureAPIClient import Ticker, FutureAPIClient
from FuturePolicy import BuyPosition, FuturePolicy


class FutureTradeSystem:
    def __init__(self):
        self.ticker_infos = []
        #ticker = {'symbol':'btc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'btc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'btc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'ltc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'ltc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'ltc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'eth_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'eth_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'eth_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'etc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'etc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'etc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'bch_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'bch_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'bch_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'xrp_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'xrp_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'xrp_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'eos_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'eos_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        #self.ticker_infos.append(ticker)
        ticker = {'symbol':'eos_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        self.ticker_infos.append(ticker)
        #ticker = {'symbol':'btg_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'btg_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        #self.ticker_infos.append(ticker)
        #ticker = {'symbol':'btg_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        #self.ticker_infos.append(ticker)

        self.policy_infos = []
        #   05   10   20   30
        # 0.75 1.00 1.25 1.50
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':0.75, 'stop_loss_percent':0.75 * 3.0}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.00, 'stop_loss_percent':1.00 * 3.0}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.25, 'stop_loss_percent':1.25 * 3.0}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.50, 'stop_loss_percent':1.50 * 3.0}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':0.75 * 3.0, 'stop_loss_percent':0.75}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.00 * 3.0, 'stop_loss_percent':1.00}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.25 * 3.0, 'stop_loss_percent':1.25}
        self.policy_infos.append(policy)
        policy = {'open_date_diff':  5 * 60, 'stop_profit_percent':1.50 * 3.0, 'stop_loss_percent':1.50}
        self.policy_infos.append(policy)
        '''
        policy = {'open_date_diff': 10 * 60, 'stop_profit_percent':0.75}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 10 * 60, 'stop_profit_percent':1.00}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 10 * 60, 'stop_profit_percent':1.25}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 10 * 60, 'stop_profit_percent':1.50}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 20 * 60, 'stop_profit_percent':0.75}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 20 * 60, 'stop_profit_percent':1.00}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 20 * 60, 'stop_profit_percent':1.25}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 20 * 60, 'stop_profit_percent':1.50}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 30 * 60, 'stop_profit_percent':0.75}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 30 * 60, 'stop_profit_percent':1.00}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 30 * 60, 'stop_profit_percent':1.25}
        self.policy_infos.append(policy)
        policy = {'open_date_diff': 30 * 60, 'stop_profit_percent':1.50}
        self.policy_infos.append(policy)
        '''
        pass


    def trade_buy_for_one_contract(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        future_policy_list = []
        for i in range(len(self.ticker_infos)):
            symbol = self.ticker_infos[i]['symbol']
            contract_type = self.ticker_infos[i]['contract_type']
            future_policy_grp = []
            for policy in self.policy_infos:
                future_policy = FuturePolicy(symbol, contract_type, policy['open_date_diff'], policy['stop_profit_percent'], policy['stop_loss_percent'])
                future_policy_grp.append(future_policy)
            future_policy_list.append(future_policy_grp)
        count_print = 0
        while True:
            for i in range(len(self.ticker_infos)):
                symbol = self.ticker_infos[i]['symbol']
                contract_type = self.ticker_infos[i]['contract_type']
                ticker = future_api_client.get_ticker(symbol, contract_type)
                if int(ticker.date) < 10 ** 9:
                    print('Future API Client ERROR!\n\n')
                    continue
                for future_policy in future_policy_list[i]:
                    future_policy.do_open_close_buy_positions(ticker.last, int(ticker.date))
                    future_policy.do_open_close_sell_positions(ticker.last, int(ticker.date))
                    if count_print % (10 * 60 / 6) == 0:
                        print(ticker.get_str())
                        future_policy.print_all_positions(ticker.last)
                if count_print % (10 * 60 / 6) == 0:
                    print('\n\n\n')
                time.sleep(1)
            count_print += 1
        pass



if __name__ == '__main__':
    future_trade_system = FutureTradeSystem()
    future_trade_system.trade_buy_for_one_contract()


            
            
