#!/usr/bin/python
# -*- coding: utf-8 -*-
#期货合约策略类

import unittest
import random
import json

from FutureConfigure import *
from FutureAPIClient import Ticker, FutureAPIClient

class TestFutureAPIClient_Ticker(unittest.TestCase):


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




class TestFutureAPIClient_KLine(unittest.TestCase):


    def setUp(self):
        self.kline_infos = []
        kline = {'symbol':'btc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'type':'1hour'} # 8500
        self.kline_infos.append(kline)
        kline = {'symbol':'btc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'type':'15min'} # 8500
        self.kline_infos.append(kline)
        kline = {'symbol':'btc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':850.0, 'price_max':85000.0, 'vol_min':1000.0, 'type':'1day' } # 8500
        self.kline_infos.append(kline)
        kline = {'symbol':'ltc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'type':'1hour'} #  140
        self.kline_infos.append(kline)
        kline = {'symbol':'ltc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'type':'15min'} #  140
        self.kline_infos.append(kline)
        kline = {'symbol':'ltc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':14.0,  'price_max':1400.0,  'vol_min':1000.0, 'type':'1day' } #  140
        self.kline_infos.append(kline)
        kline = {'symbol':'eth_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'type':'1hour'} #  720
        self.kline_infos.append(kline)
        kline = {'symbol':'eth_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'type':'15min'} #  720
        self.kline_infos.append(kline)
        kline = {'symbol':'eth_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':72.0,  'price_max':7200.0,  'vol_min':1000.0, 'type':'1day' } #  720
        self.kline_infos.append(kline)
        kline = {'symbol':'etc_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'type':'1hour'} #   18
        self.kline_infos.append(kline)
        kline = {'symbol':'etc_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'type':'15min'} #   18
        self.kline_infos.append(kline)
        kline = {'symbol':'etc_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.8,   'price_max':180.0,   'vol_min':1000.0, 'type':'1day' } #   18
        self.kline_infos.append(kline)
        kline = {'symbol':'bch_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'type':'1hour'} # 1300
        self.kline_infos.append(kline)
        kline = {'symbol':'bch_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'type':'15min'} # 1300
        self.kline_infos.append(kline)
        kline = {'symbol':'bch_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':130.0, 'price_max':13000.0, 'vol_min':1000.0, 'type':'1day' } # 1300
        self.kline_infos.append(kline)
        kline = {'symbol':'xrp_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'type':'1hour'} #  0.7
        self.kline_infos.append(kline)
        kline = {'symbol':'xrp_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'type':'15min'} #  0.7
        self.kline_infos.append(kline)
        kline = {'symbol':'xrp_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':0.07,  'price_max':7.0,     'vol_min':1000.0, 'type':'1day' } #  0.7
        self.kline_infos.append(kline)
        kline = {'symbol':'eos_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'type':'1hour'} #   14
        self.kline_infos.append(kline)
        kline = {'symbol':'eos_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'type':'15min'} #   14
        self.kline_infos.append(kline)
        kline = {'symbol':'eos_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':1.4,   'price_max':140.0,   'vol_min':1000.0, 'type':'1day' } #   14
        self.kline_infos.append(kline)
        kline = {'symbol':'btg_usd', 'contract_type':'this_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'type':'1hour'} #   55
        self.kline_infos.append(kline)
        kline = {'symbol':'btg_usd', 'contract_type':'next_week', 'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'type':'15min'} #   55
        self.kline_infos.append(kline)
        kline = {'symbol':'btg_usd', 'contract_type':'quarter',   'date_min':1526877182, 'price_min':5.5,   'price_max':550.0,   'vol_min':1000.0, 'type':'1day' } #   55
        self.kline_infos.append(kline)
        rand_int = random.randrange(len(self.kline_infos))
        self.kline_info = self.kline_infos[rand_int]
        pass       

    def test_future_kline(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        json_obj = future_api_client.future_kline(self.kline_info['symbol'], self.kline_info['contract_type'], self.kline_info['type'])
        self.assertGreater(len(json_obj), 50)
        #print(json.dumps(json_obj[:3], indent=4))
        #print(json.dumps(json_obj[-3:], indent=4))
        last_kline = json_obj[-2]
        self.assertGreater(int(last_kline[0]), self.kline_info['date_min'])
        self.assertGreater(float(last_kline[1]), self.kline_info['price_min'])
        self.assertGreater(float(last_kline[2]), self.kline_info['price_min'])
        self.assertGreater(float(last_kline[3]), self.kline_info['price_min'])
        self.assertGreater(float(last_kline[4]), self.kline_info['price_min'])
        self.assertLess(float(last_kline[1]), self.kline_info['price_max'])
        self.assertLess(float(last_kline[2]), self.kline_info['price_max'])
        self.assertLess(float(last_kline[3]), self.kline_info['price_max'])
        self.assertLess(float(last_kline[4]), self.kline_info['price_max'])
        self.assertGreater(float(last_kline[5]), self.kline_info['vol_min'])
        pass
        
        
    def test_get_kline(self):
        future_api_client = FutureAPIClient(Future_REST_URL, Future_Api_Key, Future_Secret_Key)
        kline = future_api_client.get_kline(self.kline_info['symbol'], self.kline_info['contract_type'], self.kline_info['type'])
        s = kline.get_str()
        self.assertNotEqual(s, '')
        self.assertGreater(len(s), 50)
        #print(s[:400])
        #print(s[-400:])
        self.assertEqual(kline.symbol, self.kline_info['symbol'])
        self.assertEqual(kline.contract_type, self.kline_info['contract_type'])
        self.assertEqual(kline.type, self.kline_info['type'])
        self.assertGreater(len(kline.klinelist), 50)
        last_kline = kline.klinelist[-2]
        self.assertGreater(int(last_kline.date), self.kline_info['date_min'])
        self.assertGreater(last_kline.open, self.kline_info['price_min'])
        self.assertGreater(last_kline.high, self.kline_info['price_min'])
        self.assertGreater(last_kline.low, self.kline_info['price_min'])
        self.assertGreater(last_kline.close, self.kline_info['price_min'])
        self.assertLess(last_kline.open, self.kline_info['price_max'])
        self.assertLess(last_kline.high, self.kline_info['price_max'])
        self.assertLess(last_kline.low, self.kline_info['price_max'])
        self.assertLess(last_kline.close, self.kline_info['price_max'])
        self.assertGreater(last_kline.vol, self.kline_info['vol_min'])
        pass


if __name__ == '__main__':
    unittest.main()

