#!/usr/bin/python
# -*- coding: utf-8 -*-
#期货合约策略类

import unittest

from FutureAPIClient import *
from FutureTechnicalIndicator import *

#self.assertEqual(b, False)
#self.assertTrue(b)
#self.assertFalse(b)

class TestFutureTechnicalIndicator(unittest.TestCase):

    def test_MA_Simple(self):
        klinelist = KLineList()
        for i in range(10):
            klinesingle = KLineSingle()
            klinelist.klinelist.append(klinesingle)

        # 收盘价全都相等的情况
        if True:
            for i in range(10):
                klinelist.klinelist[i].close = 100.0
            tech_indicat = FutureTechnicalIndicator(klinelist)
            for i in range(10):
                self.assertEqual(tech_indicat.close_list[i], 100.0)
                
            short_day_num = 5
            long_day_num = 10
            ma_simple = MA_Simple(tech_indicat.close_list, short_day_num, long_day_num)
            self.assertEqual(ma_simple.short_day_num, 5)
            self.assertEqual(ma_simple.long_day_num, 10)
            self.assertEqual(len(ma_simple.ma_short_list), 10)
            self.assertEqual(len(ma_simple.ma_long_list), 10)
            
            self.assertEqual(ma_simple.ma_short_list[0], 100.0)
            self.assertEqual(ma_simple.ma_short_list[1], 100.0)
            self.assertEqual(ma_simple.ma_short_list[2], 100.0)
            self.assertEqual(ma_simple.ma_short_list[3], 100.0)
            self.assertEqual(ma_simple.ma_short_list[4], 100.0)
            self.assertEqual(ma_simple.ma_short_list[5], 100.0)
            self.assertEqual(ma_simple.ma_short_list[6], 100.0)
            self.assertEqual(ma_simple.ma_short_list[7], 100.0)
            self.assertEqual(ma_simple.ma_short_list[8], 100.0)
            self.assertEqual(ma_simple.ma_short_list[9], 100.0)
            self.assertEqual(ma_simple.ma_long_list[0], 100.0)
            self.assertEqual(ma_simple.ma_long_list[1], 100.0)
            self.assertEqual(ma_simple.ma_long_list[2], 100.0)
            self.assertEqual(ma_simple.ma_long_list[3], 100.0)
            self.assertEqual(ma_simple.ma_long_list[4], 100.0)
            self.assertEqual(ma_simple.ma_long_list[5], 100.0)
            self.assertEqual(ma_simple.ma_long_list[6], 100.0)
            self.assertEqual(ma_simple.ma_long_list[7], 100.0)
            self.assertEqual(ma_simple.ma_long_list[8], 100.0)
            self.assertEqual(ma_simple.ma_long_list[9], 100.0)
           
        # 收盘价不相等的情况
        if True:
            klinelist.klinelist[0].close = 100.0
            klinelist.klinelist[1].close =  50.0
            klinelist.klinelist[2].close = 100.0
            klinelist.klinelist[3].close =  60.0
            klinelist.klinelist[4].close = 100.0
            klinelist.klinelist[5].close =  70.0
            klinelist.klinelist[6].close = 100.0
            klinelist.klinelist[7].close =  80.0
            klinelist.klinelist[8].close = 100.0
            klinelist.klinelist[9].close =  90.0
            tech_indicat = FutureTechnicalIndicator(klinelist)      # sum5  sum10
            self.assertEqual(tech_indicat.close_list[0], 100.0)     # 100   100
            self.assertEqual(tech_indicat.close_list[1],  50.0)     # 150   150
            self.assertEqual(tech_indicat.close_list[2], 100.0)     # 250   250
            self.assertEqual(tech_indicat.close_list[3],  60.0)     # 310   310
            self.assertEqual(tech_indicat.close_list[4], 100.0)     # 410   410
            self.assertEqual(tech_indicat.close_list[5],  70.0)     ##380   480
            self.assertEqual(tech_indicat.close_list[6], 100.0)     # 430   580
            self.assertEqual(tech_indicat.close_list[7],  80.0)     # 410   660
            self.assertEqual(tech_indicat.close_list[8], 100.0)     # 450   760
            self.assertEqual(tech_indicat.close_list[9],  90.0)     # 440   850
            
            short_day_num = 5
            long_day_num = 10
            ma_simple = MA_Simple(tech_indicat.close_list, short_day_num, long_day_num)
            self.assertEqual(ma_simple.short_day_num, 5)
            self.assertEqual(ma_simple.long_day_num, 10)
            self.assertEqual(len(ma_simple.ma_short_list), 10)
            self.assertEqual(len(ma_simple.ma_long_list), 10)
            
            self.assertEqual(ma_simple.ma_short_list[0], 100.0 / 1)
            self.assertEqual(ma_simple.ma_short_list[1], 150.0 / 2)
            self.assertEqual(ma_simple.ma_short_list[2], 250.0 / 3)
            self.assertEqual(ma_simple.ma_short_list[3], 310.0 / 4)
            self.assertEqual(ma_simple.ma_short_list[4], 410.0 / 5)
            self.assertEqual(ma_simple.ma_short_list[5], 380.0 / 5)
            self.assertEqual(ma_simple.ma_short_list[6], 430.0 / 5)
            self.assertEqual(ma_simple.ma_short_list[7], 410.0 / 5)
            self.assertEqual(ma_simple.ma_short_list[8], 450.0 / 5)
            self.assertEqual(ma_simple.ma_short_list[9], 440.0 / 5)
            
            self.assertEqual(ma_simple.ma_long_list[0],  100.0 / 1)
            self.assertEqual(ma_simple.ma_long_list[1],  150.0 / 2)
            self.assertEqual(ma_simple.ma_long_list[2],  250.0 / 3)
            self.assertEqual(ma_simple.ma_long_list[3],  310.0 / 4)
            self.assertEqual(ma_simple.ma_long_list[4],  410.0 / 5)
            self.assertEqual(ma_simple.ma_long_list[5],  480.0 / 6)
            self.assertEqual(ma_simple.ma_long_list[6],  580.0 / 7)
            self.assertEqual(ma_simple.ma_long_list[7],  660.0 / 8)
            self.assertEqual(ma_simple.ma_long_list[8],  760.0 / 9)
            self.assertEqual(ma_simple.ma_long_list[9],  850.0 /10)          
        
        pass




    def test_OBV_Simple(self):
        klinelist = KLineList()
        for i in range(10):
            klinesingle = KLineSingle()
            klinelist.klinelist.append(klinesingle)

        # 收盘价一直上涨的情况
        if True:
            for i in range(10):
                klinelist.klinelist[i].close = (i + 1) + 100
                klinelist.klinelist[i].vol = (i + 1) * 100
            tech_indicat = FutureTechnicalIndicator(klinelist)
            for i in range(10):
                self.assertEqual(tech_indicat.close_list[i], (i + 1) + 100)
                self.assertEqual(tech_indicat.vol_list[i], (i + 1) * 100)
                
            ma_day_num = 5
            obv_simple = OBV_Simple(tech_indicat.vol_list, tech_indicat.close_list, ma_day_num)
            self.assertEqual(obv_simple.ma_day_num, 5)
            self.assertEqual(len(obv_simple.obv_list), 10)
            self.assertEqual(len(obv_simple.ma_obv_list), 10)
            
            self.assertEqual(obv_simple.obv_list[0], 100.0)
            self.assertEqual(obv_simple.obv_list[1], 300.0)
            self.assertEqual(obv_simple.obv_list[2], 600.0)
            self.assertEqual(obv_simple.obv_list[3],1000.0)
            self.assertEqual(obv_simple.obv_list[4],1500.0)
            self.assertEqual(obv_simple.obv_list[5],2100.0)
            self.assertEqual(obv_simple.obv_list[6],2800.0)
            self.assertEqual(obv_simple.obv_list[7],3600.0)
            self.assertEqual(obv_simple.obv_list[8],4500.0)
            self.assertEqual(obv_simple.obv_list[9],5500.0)
            self.assertEqual(obv_simple.ma_obv_list[0],  100.0 / 1)
            self.assertEqual(obv_simple.ma_obv_list[1],  400.0 / 2)
            self.assertEqual(obv_simple.ma_obv_list[2], 1000.0 / 3)
            self.assertEqual(obv_simple.ma_obv_list[3], 2000.0 / 4)
            self.assertEqual(obv_simple.ma_obv_list[4], 3500.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[5], 5500.0 / 5) #
            self.assertEqual(obv_simple.ma_obv_list[6], 8000.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[7],11000.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[8],14500.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[9],18500.0 / 5)

        # 收盘价一直下跌的情况
        if True:
            for i in range(10):
                klinelist.klinelist[i].close = 100 - (i + 1)
                klinelist.klinelist[i].vol = i * 100
            tech_indicat = FutureTechnicalIndicator(klinelist)
            for i in range(10):
                self.assertEqual(tech_indicat.close_list[i], 100 - (i + 1))
                self.assertEqual(tech_indicat.vol_list[i], i * 100)
                
            ma_day_num = 5
            obv_simple = OBV_Simple(tech_indicat.vol_list, tech_indicat.close_list, ma_day_num)
            self.assertEqual(obv_simple.ma_day_num, 5)
            self.assertEqual(len(obv_simple.obv_list), 10)
            self.assertEqual(len(obv_simple.ma_obv_list), 10)
            
            self.assertEqual(obv_simple.obv_list[0],    0.0)
            self.assertEqual(obv_simple.obv_list[1], -100.0)
            self.assertEqual(obv_simple.obv_list[2], -300.0)
            self.assertEqual(obv_simple.obv_list[3], -600.0)
            self.assertEqual(obv_simple.obv_list[4],-1000.0)
            self.assertEqual(obv_simple.obv_list[5],-1500.0)
            self.assertEqual(obv_simple.obv_list[6],-2100.0)
            self.assertEqual(obv_simple.obv_list[7],-2800.0)
            self.assertEqual(obv_simple.obv_list[8],-3600.0)
            self.assertEqual(obv_simple.obv_list[9],-4500.0)
            self.assertEqual(obv_simple.ma_obv_list[0],     0.0 / 1)
            self.assertEqual(obv_simple.ma_obv_list[1],  -100.0 / 2)
            self.assertEqual(obv_simple.ma_obv_list[2],  -400.0 / 3)
            self.assertEqual(obv_simple.ma_obv_list[3], -1000.0 / 4)
            self.assertEqual(obv_simple.ma_obv_list[4], -2000.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[5], -3500.0 / 5) #
            self.assertEqual(obv_simple.ma_obv_list[6], -5500.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[7], -8000.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[8],-11000.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[9],-14500.0 / 5)

        # 收盘价有涨有跌的情况
        if True:
            klinelist.klinelist[0].close = 100.0
            klinelist.klinelist[1].close =  50.0
            klinelist.klinelist[2].close = 100.0
            klinelist.klinelist[3].close =  60.0
            klinelist.klinelist[4].close =  70.0
            klinelist.klinelist[5].close =  80.0
            klinelist.klinelist[6].close = 100.0
            klinelist.klinelist[7].close =  90.0
            klinelist.klinelist[8].close =  80.0
            klinelist.klinelist[9].close =  70.0
            for i in range(10):
                klinelist.klinelist[i].vol = (i + 1) * 100
            tech_indicat = FutureTechnicalIndicator(klinelist)
            self.assertEqual(tech_indicat.close_list[0], 100.0)
            self.assertEqual(tech_indicat.close_list[1],  50.0)
            self.assertEqual(tech_indicat.close_list[2], 100.0)
            self.assertEqual(tech_indicat.close_list[3],  60.0)
            self.assertEqual(tech_indicat.close_list[4],  70.0)
            self.assertEqual(tech_indicat.close_list[5],  80.0)
            self.assertEqual(tech_indicat.close_list[6], 100.0)
            self.assertEqual(tech_indicat.close_list[7],  90.0)
            self.assertEqual(tech_indicat.close_list[8],  80.0)
            self.assertEqual(tech_indicat.close_list[9],  70.0)
            for i in range(10):
                self.assertEqual(tech_indicat.vol_list[i], (i + 1) * 100)
                
            ma_day_num = 5
            obv_simple = OBV_Simple(tech_indicat.vol_list, tech_indicat.close_list, ma_day_num)
            self.assertEqual(obv_simple.ma_day_num, 5)
            self.assertEqual(len(obv_simple.obv_list), 10)
            self.assertEqual(len(obv_simple.ma_obv_list), 10)
            
            self.assertEqual(obv_simple.obv_list[0],  100.0) #  +100 
            self.assertEqual(obv_simple.obv_list[1], -100.0) #  -200
            self.assertEqual(obv_simple.obv_list[2],  200.0) #  +300
            self.assertEqual(obv_simple.obv_list[3], -200.0) #  -400
            self.assertEqual(obv_simple.obv_list[4],  300.0) #  +500
            self.assertEqual(obv_simple.obv_list[5],  900.0) #  +600
            self.assertEqual(obv_simple.obv_list[6], 1600.0) #  +700
            self.assertEqual(obv_simple.obv_list[7],  800.0) #  -800
            self.assertEqual(obv_simple.obv_list[8], -100.0) #  -900
            self.assertEqual(obv_simple.obv_list[9],-1100.0) # -1000
            self.assertEqual(obv_simple.ma_obv_list[0],  100.0 / 1)
            self.assertEqual(obv_simple.ma_obv_list[1],    0.0 / 2)
            self.assertEqual(obv_simple.ma_obv_list[2],  200.0 / 3)
            self.assertEqual(obv_simple.ma_obv_list[3],    0.0 / 4)
            self.assertEqual(obv_simple.ma_obv_list[4],  300.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[5], 1100.0 / 5) #
            self.assertEqual(obv_simple.ma_obv_list[6], 2800.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[7], 3400.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[8], 3500.0 / 5)
            self.assertEqual(obv_simple.ma_obv_list[9], 2100.0 / 5)


        pass



if __name__ == '__main__':
    unittest.main()






    
    
