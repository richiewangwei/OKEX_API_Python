#!/usr/bin/python
# -*- coding: utf-8 -*-
#期货合约策略类

import random
from HttpMD5Util import buildMySign,httpGet,httpPost,printJson
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture


class MA_Simple:
    def __init__(self, original_value_list, short_day_num, long_day_num):
        self.original_value_list = original_value_list
        self.short_day_num = short_day_num
        self.long_day_num = long_day_num
        self.ma_short_list = []
        self.ma_long_list = []

        for i in range(len(self.original_value_list)):
            ma_short = 0.0
            ma_long = 0.0
            if i < self.short_day_num:
                # i
                # 0: [0:1] / 1
                # 1: [0:2] / 2
                # 2: [0:3] / 3
                # 3: [0:4] / 4
                # 4: [0:5] / 5
                ma_short = sum(self.original_value_list[0 : i + 1]) / (i + 1)
            else:
                # 5: [1:6] / 5
                # 6: [2:7] / 5
                ma_short = sum(self.original_value_list[i + 1 - self.short_day_num : i + 1]) / self.short_day_num
                
            if i < self.long_day_num:
                # i
                # 0: [0:1] / 1
                # 1: [0:2] / 2
                # 2: [0:3] / 3
                # 3: [0:4] / 4
                # 4: [0:5] / 5
                ma_long = sum(self.original_value_list[0 : i + 1]) / (i + 1)
            else:
                # 5: [1:6] / 5
                # 6: [2:7] / 5
                ma_long = sum(self.original_value_list[i + 1 - self.long_day_num : i + 1]) / self.long_day_num

            self.ma_short_list.append(ma_short)
            self.ma_long_list.append(ma_long)
            
        pass



class OBV_Simple:
    def __init__(self, vol_list, close_list, ma_day_num, since = ''):
        self.vol_list = vol_list
        self.close_list = close_list
        self.ma_day_num = ma_day_num
        self.since = since
        self.obv_list = []
        self.ma_obv_list = []

        self.obv_list.append(self.vol_list[0])
        self.ma_obv_list.append(self.vol_list[0])
        
        for i in range(1, len(self.vol_list)):
            obv = 0.0
            ma_obv = 0.0
            if self.close_list[i] > self.close_list[i-1]:
                obv = self.obv_list[i-1] + self.vol_list[i]
            else:
                obv = self.obv_list[i-1] - self.vol_list[i]
            self.obv_list.append(obv)
                
            if i < self.ma_day_num:
                ma_obv = sum(self.obv_list[0 : i + 1]) / (i + 1)
            else:
                ma_obv = sum(self.obv_list[i + 1 - self.ma_day_num : i + 1]) / self.ma_day_num
            self.ma_obv_list.append(ma_obv)

        pass
    
              
        
        
class FutureTechnicalIndicator:

    def __init__(self, klinelist):
        self.klinelist = klinelist
        self.open_list = []
        self.high_list = []
        self.low_list = []
        self.close_list = []
        self.vol_list = []
        for klinesingle in self.klinelist.klinelist:
            self.open_list.append(klinesingle.open)
            self.high_list.append(klinesingle.high)
            self.low_list.append(klinesingle.low)
            self.close_list.append(klinesingle.close)
            self.vol_list.append(klinesingle.vol)
        pass



