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
    
              

class Stat_Orders:
    def __init__(self):
        pass


    def trade_orders(self, order_list, diff_order_count, close_price):
        profit_sum = 0.0
        if diff_order_count == 0:
            return profit_sum
        
        if diff_order_count > 0:
            # Long_Order
            # empty list
            if len(order_list) == 0:
                # only open_order
                order_count = abs(diff_order_count)
                for i in range(order_count):
                    order_list.append(close_price)
                return profit_sum
            # len(order_list) > 0
            if order_list[-1] > 0:
                # only open_order
                order_count = abs(diff_order_count)
                for i in range(order_count):
                    order_list.append(close_price)
            elif order_list[-1] < 0:
                order_count = abs(diff_order_count)
                len_order_list = len(order_list)
                if order_count <= len_order_list:
                    # only close_order
                    for i in range(order_count):
                        open_price = order_list.pop()
                        profit_sum += abs(open_price) - abs(close_price)
                elif order_count > len_order_list:
                    # close_order + open_order
                    for i in range(len_order_list):
                        open_price = order_list.pop()
                        profit_sum += abs(open_price) - abs(close_price)
                    order_count -= len_order_list
                    for i in range(order_count):
                        order_list.append(close_price)
            return profit_sum

        if diff_order_count < 0:
            # Short_Order
            # empty list
            if len(order_list) == 0:
                # only open_order
                order_count = abs(diff_order_count)
                for i in range(order_count):
                    order_list.append(-close_price)
                return profit_sum
            # len(order_list) > 0
            if order_list[-1] < 0:
                # only open_order
                order_count = abs(diff_order_count)
                for i in range(order_count):
                    order_list.append(-close_price)
            elif order_list[-1] > 0:
                order_count = abs(diff_order_count)
                len_order_list = len(order_list)
                if order_count <= len_order_list:
                    # only close_order
                    for i in range(order_count):
                        open_price = order_list.pop()
                        profit_sum += abs(close_price) - abs(open_price)
                elif order_count > len_order_list:
                    # close_order + open_order
                    for i in range(len_order_list):
                        open_price = order_list.pop()
                        profit_sum += abs(close_price) - abs(open_price)
                    order_count -= len_order_list
                    for i in range(order_count):
                        order_list.append(-close_price)                
            return profit_sum
        pass


    def profit_opened_orders(self, order_list, close_price):
        profit_sum = 0.0
        if len(order_list) == 0:
            return profit_sum
        if order_list[-1] > 0:
            # Long_Order
            for i in range(len(order_list)):
                open_price = order_list[i]
                profit_sum += abs(close_price) - abs(open_price)
            return profit_sum
        elif order_list[-1] < 0:
            # Short_Order
            for i in range(len(order_list)):
                open_price = order_list[i]
                profit_sum += abs(open_price) - abs(close_price)
            return profit_sum
        pass   



class Open_Close_Diff:
    def __init__(self, open_list, close_list):
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



