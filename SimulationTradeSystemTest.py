#!/usr/bin/python
# -*- coding: utf-8 -*-
#期货合约策略类

import unittest
import random
import json

from SimulationTradeSystem import *

#self.assertEqual(b, False)
#self.assertTrue(b)
#self.assertFalse(b)









class TestFutureAPIClient(unittest.TestCase):


    def setUp(self):
        self.ticker_infos = []
        ticker = {'symbol':'btc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'btc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'btc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt':100.0} # 8500
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'ltc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'ltc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'ltc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  140
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eth_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eth_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eth_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  720
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'etc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'etc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'etc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   18
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'bch_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'bch_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'bch_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} # 1300
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'xrp_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'xrp_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'xrp_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #  0.7
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eos_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eos_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'eos_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   14
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'btg_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'btg_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        self.ticker_infos.append(ticker)
        ticker = {'symbol':'btg_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'cont_min':1000, 'unit_amnt': 10.0} #   55
        self.ticker_infos.append(ticker)
        rand_int = random.randrange(len(self.ticker_infos))
        self.ticker_info = self.ticker_infos[rand_int]
        pass       

    def test_future_ticker(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        json_obj = future_api_client.future_ticker(self.ticker_info['symbol'], self.ticker_info['contract_type'])
        #print(json.dumps(json_obj, indent=4))
        self.assertGreater(int(json_obj["date"]), self.ticker_info['date_min'])
        self.assertGreater(float(json_obj["ticker"]["last"]), self.ticker_info['price_min'])
        self.assertGreater(float(json_obj["ticker"]["buy"]), self.ticker_info['price_min'])
        self.assertGreater(float(json_obj["ticker"]["sell"]), self.ticker_info['price_min'])
        self.assertGreater(float(json_obj["ticker"]["high"]), self.ticker_info['price_min'])
        self.assertGreater(float(json_obj["ticker"]["low"]), self.ticker_info['price_min'])
        self.assertLess(float(json_obj["ticker"]["last"]), self.ticker_info['price_max'])
        self.assertLess(float(json_obj["ticker"]["buy"]), self.ticker_info['price_max'])
        self.assertLess(float(json_obj["ticker"]["sell"]), self.ticker_info['price_max'])
        self.assertLess(float(json_obj["ticker"]["high"]), self.ticker_info['price_max'])
        self.assertLess(float(json_obj["ticker"]["low"]), self.ticker_info['price_max'])
        self.assertGreater(float(json_obj["ticker"]["vol"]), self.ticker_info['vol_min'])
        self.assertGreater(int(json_obj["ticker"]["contract_id"]), self.ticker_info['cont_min'])
        self.assertEqual(float(json_obj["ticker"]["unit_amount"]), self.ticker_info['unit_amnt'])
        pass
        
        
    def test_get_ticker(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        ticker = future_api_client.get_ticker(self.ticker_info['symbol'], self.ticker_info['contract_type'])
        s = ticker.get_str()
        self.assertNotEqual(s, '')
        self.assertGreater(len(s), 50)
        #print(s)
        self.assertEqual(ticker.symbol, self.ticker_info['symbol'])
        self.assertEqual(ticker.contract_type, self.ticker_info['contract_type'])
        self.assertGreater(int(ticker.date), self.ticker_info['date_min'])
        self.assertGreater(ticker.last, self.ticker_info['price_min'])
        self.assertGreater(ticker.buy, self.ticker_info['price_min'])
        self.assertGreater(ticker.sell, self.ticker_info['price_min'])
        self.assertGreater(ticker.high, self.ticker_info['price_min'])
        self.assertGreater(ticker.low, self.ticker_info['price_min'])
        self.assertLess(ticker.last, self.ticker_info['price_max'])
        self.assertLess(ticker.buy, self.ticker_info['price_max'])
        self.assertLess(ticker.sell, self.ticker_info['price_max'])
        self.assertLess(ticker.high, self.ticker_info['price_max'])
        self.assertLess(ticker.low, self.ticker_info['price_max'])
        self.assertGreater(ticker.vol, self.ticker_info['vol_min'])
        self.assertGreater(ticker.contract_id, self.ticker_info['cont_min'])
        self.assertEqual(ticker.unit_amount, self.ticker_info['unit_amnt'])       
        pass












class TestFuturePolicy(unittest.TestCase):

    def test_trade_open_buy(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次开多仓
        buy_amount = 1
        buy_price = 100.0
        open_date = 10000
        future_policy.trade_open_buy(buy_amount, buy_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 10000)
        # 第2次开多仓
        buy_amount = 3
        buy_price = 200.0
        open_date = 10100
        future_policy.trade_open_buy(buy_amount, buy_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 2)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 3)
        self.assertEqual(future_policy.open_buy_positions[1].buy_price, 200.0)
        self.assertEqual(future_policy.open_buy_positions[1].open_date, 10100)
        pass
    
    def test_is_need_close_buy(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        buy_amount = 1
        buy_price = 100.0
        open_date = 10000
        future_policy.trade_open_buy(buy_amount, buy_price, open_date)
        # 小幅波动
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 100.1)
        self.assertFalse(b)
        # 小幅波动
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 99.9)
        self.assertFalse(b)
        # 大幅波动
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 110.0)
        self.assertTrue(b)       
        # 大幅波动
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 90.0)
        self.assertTrue(b)

        # 未碰小止损，不执行小止盈
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 101.01)
        self.assertFalse(b)       
        # 碰到小止损
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 98.99)
        self.assertFalse(b)
        self.assertTrue(future_policy.open_buy_positions[0].is_need_mini_profit)        
        # 执行小止盈
        b = future_policy.is_need_close_buy(future_policy.open_buy_positions[0], 101.01)
        self.assertTrue(b)
        pass

    def test_trade_close_buy(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        self.assertEqual(len(future_policy.open_buy_positions), 0)
        self.assertEqual(len(future_policy.close_buy_positions), 0)
        # 开多仓1次，平多仓1次        
        buy_amount = 1
        buy_price = 100.0
        open_date = 10000
        future_policy.trade_open_buy(buy_amount, buy_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_buy_positions[0].sell_amount, 0)
        self.assertEqual(future_policy.open_buy_positions[0].sell_price, 0.0)
        self.assertEqual(future_policy.open_buy_positions[0].close_date, 0)
        self.assertEqual(future_policy.open_buy_positions[0].profit_percent, 0.0)
        sell_amount = 1
        sell_price = 90.0
        close_date = 10200
        future_policy.trade_close_buy(future_policy.open_buy_positions[0], sell_amount, sell_price, close_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_buy_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].sell_price, 90.0)
        self.assertEqual(future_policy.open_buy_positions[0].close_date, 10200)
        self.assertEqual(future_policy.open_buy_positions[0].profit_percent, -10.0)
        self.assertEqual(len(future_policy.close_buy_positions), 1)
        self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.close_buy_positions[0].open_date, 10000)
        self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].sell_price, 90.0)
        self.assertEqual(future_policy.close_buy_positions[0].close_date, 10200)
        self.assertEqual(future_policy.close_buy_positions[0].profit_percent, -10.0)
        pass        

    def test_del_pos_from_open_buy(self):
        # 开仓1次，然后删除
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.0
            open_date = 10000
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            future_policy.del_pos_from_open_buy(0)
            self.assertEqual(len(future_policy.open_buy_positions), 0)         
        # 开仓3次，删除第1个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 101.0
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 102.0
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 103.0
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            future_policy.del_pos_from_open_buy(0)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 2)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 102.0)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10002)
            self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 3)
            self.assertEqual(future_policy.open_buy_positions[1].buy_price, 103.0)
            self.assertEqual(future_policy.open_buy_positions[1].open_date, 10003)
        # 开仓3次，删除第2个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 101.0
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 102.0
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 103.0
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            future_policy.del_pos_from_open_buy(1)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 101.0)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 3)
            self.assertEqual(future_policy.open_buy_positions[1].buy_price, 103.0)
            self.assertEqual(future_policy.open_buy_positions[1].open_date, 10003)
        # 开仓3次，删除第3个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 101.0
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 102.0
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 103.0
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            future_policy.del_pos_from_open_buy(2)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 101.0)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 2)
            self.assertEqual(future_policy.open_buy_positions[1].buy_price, 102.0)
            self.assertEqual(future_policy.open_buy_positions[1].open_date, 10002)
        pass

    def test_scan_all_open_buy_positions(self):
        # 开仓1次，先不平仓，然后平仓
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.1
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            # 先不平仓
            last_deal_price = 100.101
            close_date = 11001
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 1)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10001)
            self.assertEqual(len(future_policy.close_buy_positions), 0)
            # 然后平仓
            last_deal_price = 110.0
            close_date = 11002
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 0)         
            self.assertEqual(len(future_policy.close_buy_positions), 1)
            self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.close_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].sell_price, 110.0)
            self.assertEqual(future_policy.close_buy_positions[0].close_date, 11002)
            self.assertEqual(future_policy.close_buy_positions[0].profit_percent, 9.89)
            
        # 开仓3次，不平仓，全都保留
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.1
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 100.2
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 100.3
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            last_deal_price = 100.2
            close_date = 11001
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 2)
            self.assertEqual(future_policy.open_buy_positions[1].buy_price, 100.2)
            self.assertEqual(future_policy.open_buy_positions[1].open_date, 10002)
            self.assertEqual(future_policy.open_buy_positions[2].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[2].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[2].buy_amount, 3)
            self.assertEqual(future_policy.open_buy_positions[2].buy_price, 100.3)
            self.assertEqual(future_policy.open_buy_positions[2].open_date, 10003)
            self.assertEqual(len(future_policy.close_buy_positions), 0)

        # 开仓3次，然后只平掉第1次的仓位，保留第2次和第3次（共3种情况，只测1种）
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.1
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 120.2
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 120.3
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            last_deal_price = 120.25
            close_date = 11001
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 2)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 120.2)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10002)
            self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 3)
            self.assertEqual(future_policy.open_buy_positions[1].buy_price, 120.3)
            self.assertEqual(future_policy.open_buy_positions[1].open_date, 10003)
            self.assertEqual(len(future_policy.close_buy_positions), 1)
            self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.close_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].sell_price, 120.25)
            self.assertEqual(future_policy.close_buy_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_buy_positions[0].profit_percent, 20.13)

        # 开仓3次，然后平掉后2次的仓位，只保留第1次的仓位（共3种情况，只测1种）
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.1
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 120.2
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 120.3
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            self.assertEqual(len(future_policy.close_buy_positions), 0)
            last_deal_price = 100.101
            close_date = 11001
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(len(future_policy.close_buy_positions), 1)
            last_deal_price = 100.102
            close_date = 11002
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 1)         
            self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.open_buy_positions[0].open_date, 10001)
            self.assertEqual(len(future_policy.close_buy_positions), 2)
            self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 2)
            self.assertEqual(future_policy.close_buy_positions[0].buy_price, 120.2)
            self.assertEqual(future_policy.close_buy_positions[0].open_date, 10002)
            self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 2)
            self.assertEqual(future_policy.close_buy_positions[0].sell_price, 100.101)
            self.assertEqual(future_policy.close_buy_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_buy_positions[0].profit_percent, -16.72)
            self.assertEqual(future_policy.close_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[1].buy_amount, 3)
            self.assertEqual(future_policy.close_buy_positions[1].buy_price, 120.3)
            self.assertEqual(future_policy.close_buy_positions[1].open_date, 10003)
            self.assertEqual(future_policy.close_buy_positions[1].sell_amount, 3)
            self.assertEqual(future_policy.close_buy_positions[1].sell_price, 100.102)
            self.assertEqual(future_policy.close_buy_positions[1].close_date, 11002)
            self.assertEqual(future_policy.close_buy_positions[1].profit_percent, -16.79)

        # 开仓3次，全都平仓，不保留
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            buy_amount = 1
            buy_price = 100.1
            open_date = 10001
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 2
            buy_price = 100.2
            open_date = 10002
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            buy_amount = 3
            buy_price = 100.3
            open_date = 10003
            future_policy.trade_open_buy(buy_amount, buy_price, open_date)
            self.assertEqual(len(future_policy.open_buy_positions), 3)         
            self.assertEqual(len(future_policy.close_buy_positions), 0)
            last_deal_price = 120.1
            close_date = 11001
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 2)         
            self.assertEqual(len(future_policy.close_buy_positions), 1)
            last_deal_price = 120.2
            close_date = 11002
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 1)         
            self.assertEqual(len(future_policy.close_buy_positions), 2)
            last_deal_price = 120.3
            close_date = 11003
            future_policy.scan_all_open_buy_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_buy_positions), 0)         
            self.assertEqual(len(future_policy.close_buy_positions), 3)
            self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.1)
            self.assertEqual(future_policy.close_buy_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_buy_positions[0].sell_price, 120.1)
            self.assertEqual(future_policy.close_buy_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_buy_positions[0].profit_percent, 19.98)
            self.assertEqual(future_policy.close_buy_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[1].buy_amount, 2)
            self.assertEqual(future_policy.close_buy_positions[1].buy_price, 100.2)
            self.assertEqual(future_policy.close_buy_positions[1].open_date, 10002)
            self.assertEqual(future_policy.close_buy_positions[1].sell_amount, 2)
            self.assertEqual(future_policy.close_buy_positions[1].sell_price, 120.2)
            self.assertEqual(future_policy.close_buy_positions[1].close_date, 11002)
            self.assertEqual(future_policy.close_buy_positions[1].profit_percent, 19.96)
            self.assertEqual(future_policy.close_buy_positions[2].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_buy_positions[2].contract_type, 'this_week')
            self.assertEqual(future_policy.close_buy_positions[2].buy_amount, 3)
            self.assertEqual(future_policy.close_buy_positions[2].buy_price, 100.3)
            self.assertEqual(future_policy.close_buy_positions[2].open_date, 10003)
            self.assertEqual(future_policy.close_buy_positions[2].sell_amount, 3)
            self.assertEqual(future_policy.close_buy_positions[2].sell_price, 120.3)
            self.assertEqual(future_policy.close_buy_positions[2].close_date, 11003)
            self.assertEqual(future_policy.close_buy_positions[2].profit_percent, 19.94)
        pass

    def test_build_open_buy_positions(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次开多仓
        last_deal_price = 100.0
        open_date = 1526877182
        future_policy.build_open_buy_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526877182)
        # 第2次开多仓，未开仓
        last_deal_price = 200.0
        open_date = 1526877183
        future_policy.build_open_buy_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526877182)
        # 第3次开多仓，开仓
        last_deal_price = 300.0
        open_date = 1526888888
        future_policy.build_open_buy_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_buy_positions), 2)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526877182)
        self.assertEqual(future_policy.open_buy_positions[1].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[1].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[1].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[1].buy_price, 300.0)
        self.assertEqual(future_policy.open_buy_positions[1].open_date, 1526888888)
        pass

    def test_do_open_close_buy_positions(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次报价：开多仓
        last_deal_price = 100.0
        ticker_date = 1526811118
        future_policy.do_open_close_buy_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.open_buy_positions[0].sell_amount, 0)
        self.assertEqual(future_policy.open_buy_positions[0].sell_price, 0.0)
        self.assertEqual(future_policy.open_buy_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_buy_positions), 0)
        # 第2次报价：持仓不动
        last_deal_price = 100.001
        ticker_date = 1526811188
        future_policy.do_open_close_buy_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.open_buy_positions[0].sell_amount, 0)
        self.assertEqual(future_policy.open_buy_positions[0].sell_price, 0.0)
        self.assertEqual(future_policy.open_buy_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_buy_positions), 0)
        # 第3次报价：平多仓
        last_deal_price = 200.0
        ticker_date = 1526811888
        future_policy.do_open_close_buy_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_buy_positions), 0)
        self.assertEqual(len(future_policy.close_buy_positions), 1)
        self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.close_buy_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].sell_price, 200.0)
        self.assertEqual(future_policy.close_buy_positions[0].close_date, 1526811888)
        self.assertEqual(future_policy.close_buy_positions[0].profit_percent, 100.0)
       # 第4次报价：开多仓
        last_deal_price = 210.0
        ticker_date = 1526818888
        future_policy.do_open_close_buy_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_buy_positions), 1)
        self.assertEqual(future_policy.open_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_buy_positions[0].buy_price, 210.0)
        self.assertEqual(future_policy.open_buy_positions[0].open_date, 1526818888)
        self.assertEqual(future_policy.open_buy_positions[0].sell_amount, 0)
        self.assertEqual(future_policy.open_buy_positions[0].sell_price, 0.0)
        self.assertEqual(future_policy.open_buy_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_buy_positions), 1)
        self.assertEqual(future_policy.close_buy_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_buy_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_buy_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].buy_price, 100.0)
        self.assertEqual(future_policy.close_buy_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.close_buy_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_buy_positions[0].sell_price, 200.0)
        self.assertEqual(future_policy.close_buy_positions[0].close_date, 1526811888)
        self.assertEqual(future_policy.close_buy_positions[0].profit_percent, 100.0)
        pass    




    def test_trade_open_sell(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次开多仓
        sell_amount = 1
        sell_price = 100.0
        open_date = 10000
        future_policy.trade_open_sell(sell_amount, sell_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 10000)
        # 第2次开多仓
        sell_amount = 3
        sell_price = 200.0
        open_date = 10100
        future_policy.trade_open_sell(sell_amount, sell_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 2)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 3)
        self.assertEqual(future_policy.open_sell_positions[1].sell_price, 200.0)
        self.assertEqual(future_policy.open_sell_positions[1].open_date, 10100)
        pass
    
    def test_is_need_close_sell(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        sell_amount = 1
        sell_price = 100.0
        open_date = 10000
        future_policy.trade_open_sell(sell_amount, sell_price, open_date)
        # 小幅波动
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 100.1)
        self.assertFalse(b)
        # 小幅波动
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 99.9)
        self.assertFalse(b)
        # 大幅波动
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 110.0)
        self.assertTrue(b)       
        # 大幅波动
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 90.0)
        self.assertTrue(b)       

        # 未碰小止损，不执行小止盈
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 98.99)
        self.assertFalse(b)       
        # 碰到小止损
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 101.01)
        self.assertFalse(b)
        self.assertTrue(future_policy.open_sell_positions[0].is_need_mini_profit)        
        # 执行小止盈
        b = future_policy.is_need_close_sell(future_policy.open_sell_positions[0], 98.99)
        self.assertTrue(b)
        pass

    def test_trade_close_sell(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        self.assertEqual(len(future_policy.open_sell_positions), 0)
        self.assertEqual(len(future_policy.close_sell_positions), 0)
        # 开多仓1次，平多仓1次        
        sell_amount = 1
        sell_price = 100.0
        open_date = 10000
        future_policy.trade_open_sell(sell_amount, sell_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_sell_positions[0].buy_amount, 0)
        self.assertEqual(future_policy.open_sell_positions[0].buy_price, 0.0)
        self.assertEqual(future_policy.open_sell_positions[0].close_date, 0)
        self.assertEqual(future_policy.open_sell_positions[0].profit_percent, 0.0)
        buy_amount = 1
        buy_price = 90.0
        close_date = 10200
        future_policy.trade_close_sell(future_policy.open_sell_positions[0], buy_amount, buy_price, close_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 10000)
        self.assertEqual(future_policy.open_sell_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].buy_price, 90.0)
        self.assertEqual(future_policy.open_sell_positions[0].close_date, 10200)
        self.assertEqual(future_policy.open_sell_positions[0].profit_percent, 10.0)
        self.assertEqual(len(future_policy.close_sell_positions), 1)
        self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.close_sell_positions[0].open_date, 10000)
        self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].buy_price, 90.0)
        self.assertEqual(future_policy.close_sell_positions[0].close_date, 10200)
        self.assertEqual(future_policy.close_sell_positions[0].profit_percent, 10.0)
        pass        

    def test_del_pos_from_open_sell(self):
        # 开仓1次，然后删除
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.0
            open_date = 10000
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            future_policy.del_pos_from_open_sell(0)
            self.assertEqual(len(future_policy.open_sell_positions), 0)         
        # 开仓3次，删除第1个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 101.0
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 102.0
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 103.0
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            future_policy.del_pos_from_open_sell(0)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 2)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 102.0)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10002)
            self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 3)
            self.assertEqual(future_policy.open_sell_positions[1].sell_price, 103.0)
            self.assertEqual(future_policy.open_sell_positions[1].open_date, 10003)
        # 开仓3次，删除第2个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 101.0
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 102.0
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 103.0
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            future_policy.del_pos_from_open_sell(1)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 101.0)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 3)
            self.assertEqual(future_policy.open_sell_positions[1].sell_price, 103.0)
            self.assertEqual(future_policy.open_sell_positions[1].open_date, 10003)
        # 开仓3次，删除第3个
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 101.0
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 102.0
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 103.0
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            future_policy.del_pos_from_open_sell(2)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 101.0)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 2)
            self.assertEqual(future_policy.open_sell_positions[1].sell_price, 102.0)
            self.assertEqual(future_policy.open_sell_positions[1].open_date, 10002)
        pass

    def test_scan_all_open_sell_positions(self):
        # 开仓1次，先不平仓，然后平仓
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.1
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            # 先不平仓
            last_deal_price = 100.101
            close_date = 11001
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 1)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10001)
            self.assertEqual(len(future_policy.close_sell_positions), 0)
            # 然后平仓
            last_deal_price = 110.0
            close_date = 11002
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 0)         
            self.assertEqual(len(future_policy.close_sell_positions), 1)
            self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.close_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].buy_price, 110.0)
            self.assertEqual(future_policy.close_sell_positions[0].close_date, 11002)
            self.assertEqual(future_policy.close_sell_positions[0].profit_percent, -9.89)
            
        # 开仓3次，不平仓，全都保留
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.1
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 100.2
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 100.3
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            last_deal_price = 100.2
            close_date = 11001
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 2)
            self.assertEqual(future_policy.open_sell_positions[1].sell_price, 100.2)
            self.assertEqual(future_policy.open_sell_positions[1].open_date, 10002)
            self.assertEqual(future_policy.open_sell_positions[2].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[2].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[2].sell_amount, 3)
            self.assertEqual(future_policy.open_sell_positions[2].sell_price, 100.3)
            self.assertEqual(future_policy.open_sell_positions[2].open_date, 10003)
            self.assertEqual(len(future_policy.close_sell_positions), 0)

        # 开仓3次，然后只平掉第1次的仓位，保留第2次和第3次（共3种情况，只测1种）
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.1
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 120.2
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 120.3
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            last_deal_price = 120.25
            close_date = 11001
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 2)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 120.2)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10002)
            self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 3)
            self.assertEqual(future_policy.open_sell_positions[1].sell_price, 120.3)
            self.assertEqual(future_policy.open_sell_positions[1].open_date, 10003)
            self.assertEqual(len(future_policy.close_sell_positions), 1)
            self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.close_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].buy_price, 120.25)
            self.assertEqual(future_policy.close_sell_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_sell_positions[0].profit_percent, -20.13)

        # 开仓3次，然后平掉后2次的仓位，只保留第1次的仓位（共3种情况，只测1种）
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.1
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 120.2
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 120.3
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            self.assertEqual(len(future_policy.close_sell_positions), 0)
            last_deal_price = 100.101
            close_date = 11001
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(len(future_policy.close_sell_positions), 1)
            last_deal_price = 100.102
            close_date = 11002
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 1)         
            self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.open_sell_positions[0].open_date, 10001)
            self.assertEqual(len(future_policy.close_sell_positions), 2)
            self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 2)
            self.assertEqual(future_policy.close_sell_positions[0].sell_price, 120.2)
            self.assertEqual(future_policy.close_sell_positions[0].open_date, 10002)
            self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 2)
            self.assertEqual(future_policy.close_sell_positions[0].buy_price, 100.101)
            self.assertEqual(future_policy.close_sell_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_sell_positions[0].profit_percent, 16.72)
            self.assertEqual(future_policy.close_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[1].sell_amount, 3)
            self.assertEqual(future_policy.close_sell_positions[1].sell_price, 120.3)
            self.assertEqual(future_policy.close_sell_positions[1].open_date, 10003)
            self.assertEqual(future_policy.close_sell_positions[1].buy_amount, 3)
            self.assertEqual(future_policy.close_sell_positions[1].buy_price, 100.102)
            self.assertEqual(future_policy.close_sell_positions[1].close_date, 11002)
            self.assertEqual(future_policy.close_sell_positions[1].profit_percent, 16.79)

        # 开仓3次，全都平仓，不保留
        if True:
            future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
            sell_amount = 1
            sell_price = 100.1
            open_date = 10001
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 2
            sell_price = 100.2
            open_date = 10002
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            sell_amount = 3
            sell_price = 100.3
            open_date = 10003
            future_policy.trade_open_sell(sell_amount, sell_price, open_date)
            self.assertEqual(len(future_policy.open_sell_positions), 3)         
            self.assertEqual(len(future_policy.close_sell_positions), 0)
            last_deal_price = 120.1
            close_date = 11001
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 2)         
            self.assertEqual(len(future_policy.close_sell_positions), 1)
            last_deal_price = 120.2
            close_date = 11002
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 1)         
            self.assertEqual(len(future_policy.close_sell_positions), 2)
            last_deal_price = 120.3
            close_date = 11003
            future_policy.scan_all_open_sell_positions(last_deal_price, close_date)
            self.assertEqual(len(future_policy.open_sell_positions), 0)         
            self.assertEqual(len(future_policy.close_sell_positions), 3)
            self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.1)
            self.assertEqual(future_policy.close_sell_positions[0].open_date, 10001)
            self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
            self.assertEqual(future_policy.close_sell_positions[0].buy_price, 120.1)
            self.assertEqual(future_policy.close_sell_positions[0].close_date, 11001)
            self.assertEqual(future_policy.close_sell_positions[0].profit_percent, -19.98)
            self.assertEqual(future_policy.close_sell_positions[1].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[1].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[1].sell_amount, 2)
            self.assertEqual(future_policy.close_sell_positions[1].sell_price, 100.2)
            self.assertEqual(future_policy.close_sell_positions[1].open_date, 10002)
            self.assertEqual(future_policy.close_sell_positions[1].buy_amount, 2)
            self.assertEqual(future_policy.close_sell_positions[1].buy_price, 120.2)
            self.assertEqual(future_policy.close_sell_positions[1].close_date, 11002)
            self.assertEqual(future_policy.close_sell_positions[1].profit_percent, -19.96)
            self.assertEqual(future_policy.close_sell_positions[2].symbol, 'ltc_usd')
            self.assertEqual(future_policy.close_sell_positions[2].contract_type, 'this_week')
            self.assertEqual(future_policy.close_sell_positions[2].sell_amount, 3)
            self.assertEqual(future_policy.close_sell_positions[2].sell_price, 100.3)
            self.assertEqual(future_policy.close_sell_positions[2].open_date, 10003)
            self.assertEqual(future_policy.close_sell_positions[2].buy_amount, 3)
            self.assertEqual(future_policy.close_sell_positions[2].buy_price, 120.3)
            self.assertEqual(future_policy.close_sell_positions[2].close_date, 11003)
            self.assertEqual(future_policy.close_sell_positions[2].profit_percent, -19.94)
        pass

    def test_build_open_sell_positions(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次开多仓
        last_deal_price = 100.0
        open_date = 1526877182
        future_policy.build_open_sell_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526877182)
        # 第2次开多仓，未开仓
        last_deal_price = 200.0
        open_date = 1526877183
        future_policy.build_open_sell_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526877182)
        # 第3次开多仓，开仓
        last_deal_price = 300.0
        open_date = 1526888888
        future_policy.build_open_sell_positions(last_deal_price, open_date)
        self.assertEqual(len(future_policy.open_sell_positions), 2)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526877182)
        self.assertEqual(future_policy.open_sell_positions[1].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[1].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[1].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[1].sell_price, 300.0)
        self.assertEqual(future_policy.open_sell_positions[1].open_date, 1526888888)
        pass

    def test_do_open_close_sell_positions(self):
        future_policy = FuturePolicy('ltc_usd', 'this_week', 15 * 60, 1.50, 3.00, 1.00, 1.00)
        # 第1次报价：开多仓
        last_deal_price = 100.0
        ticker_date = 1526811118
        future_policy.do_open_close_sell_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.open_sell_positions[0].buy_amount, 0)
        self.assertEqual(future_policy.open_sell_positions[0].buy_price, 0.0)
        self.assertEqual(future_policy.open_sell_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_sell_positions), 0)
        # 第2次报价：持仓不动
        last_deal_price = 100.001
        ticker_date = 1526811188
        future_policy.do_open_close_sell_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.open_sell_positions[0].buy_amount, 0)
        self.assertEqual(future_policy.open_sell_positions[0].buy_price, 0.0)
        self.assertEqual(future_policy.open_sell_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_sell_positions), 0)
        # 第3次报价：平多仓
        last_deal_price = 200.0
        ticker_date = 1526811888
        future_policy.do_open_close_sell_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_sell_positions), 0)
        self.assertEqual(len(future_policy.close_sell_positions), 1)
        self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.close_sell_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].buy_price, 200.0)
        self.assertEqual(future_policy.close_sell_positions[0].close_date, 1526811888)
        self.assertEqual(future_policy.close_sell_positions[0].profit_percent, -100.0)
       # 第4次报价：开多仓
        last_deal_price = 210.0
        ticker_date = 1526818888
        future_policy.do_open_close_sell_positions(last_deal_price, ticker_date)
        self.assertEqual(len(future_policy.open_sell_positions), 1)
        self.assertEqual(future_policy.open_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.open_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.open_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.open_sell_positions[0].sell_price, 210.0)
        self.assertEqual(future_policy.open_sell_positions[0].open_date, 1526818888)
        self.assertEqual(future_policy.open_sell_positions[0].buy_amount, 0)
        self.assertEqual(future_policy.open_sell_positions[0].buy_price, 0.0)
        self.assertEqual(future_policy.open_sell_positions[0].close_date, 0)
        self.assertEqual(len(future_policy.close_sell_positions), 1)
        self.assertEqual(future_policy.close_sell_positions[0].symbol, 'ltc_usd')
        self.assertEqual(future_policy.close_sell_positions[0].contract_type, 'this_week')
        self.assertEqual(future_policy.close_sell_positions[0].sell_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].sell_price, 100.0)
        self.assertEqual(future_policy.close_sell_positions[0].open_date, 1526811118)
        self.assertEqual(future_policy.close_sell_positions[0].buy_amount, 1)
        self.assertEqual(future_policy.close_sell_positions[0].buy_price, 200.0)
        self.assertEqual(future_policy.close_sell_positions[0].close_date, 1526811888)
        self.assertEqual(future_policy.close_sell_positions[0].profit_percent, -100.0)
        pass    


if __name__ == '__main__':
    unittest.main()


    
    
