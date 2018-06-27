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
            ma_simple = MA_Simple(short_day_num, long_day_num, tech_indicat.close_list)
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
            ma_simple = MA_Simple(short_day_num, long_day_num, tech_indicat.close_list)
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
    


if __name__ == '__main__':
    unittest.main()


    
    
