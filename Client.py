#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from HttpMD5Util import printJson
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

#初始化apikey，secretkey,url
apikey = '5fc4e0bf-b96a-426f-8cc6-a7aa20235963'
secretkey = '233F2C5E0137E84F414B3B75082E07F1'
okcoinRESTURL = 'www.okb.com'   #请求注意：国内账号需要 修改为 www.okex.com www.okex.cn www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

#print (u' 现货行情 ')
#print (okcoinSpot.ticker('btc_cny'))

#print (u' 现货深度 ')
#print (okcoinSpot.depth('btc_cny'))

#print (u' 现货历史交易信息 ')
#print (okcoinSpot.trades())

#print (u' 用户现货账户信息 ')
#print (okcoinSpot.userinfo())

#print (u' 现货下单 ')
#print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

#print (u' 现货订单信息查询 ')
#print (okcoinSpot.orderinfo('ltc_usd','18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))



# 行情 API
#print (u'(1) 期货行情信息')
#printJson (okcoinFuture.future_ticker('ltc_usd','this_week'))

#print (u'(2) 期货市场深度信息')
#printJson (okcoinFuture.future_depth('ltc_usd','this_week','3'))

#print (u'(3) 期货交易记录信息') 
#printJson (okcoinFuture.future_trades('btc_usd','this_week'))

#print (u'(4) 期货指数信息')
#printJson (okcoinFuture.future_index('btc_usd'))

#print (u'(5) 美元人民币汇率')
#printJson (okcoinFuture.exchange_rate())

#print (u'(6) 获取预估交割价') 
#printJson (okcoinFuture.future_estimated_price('btc_usd'))



# 交易 API
#print (u'(1) 获取全仓账户信息')
#printJson (okcoinFuture.future_userinfo())

#print (u'(2) 获取全仓持仓信息')
#printJson (okcoinFuture.future_position('btc_usd','this_week'))

#print (u'(3) 期货下单')
#printJson (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

#print (u'(5) 期货批量下单')
#printJson (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'(6) 期货取消订单')
#printJson (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

#print (u'(7) 期货获取订单信息')
#printJson (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))
#printJson (okcoinFuture.future_orderinfo('btc_usd','this_week', orderId='-1', status='1',currentPage='0',pageLength='10')) # 所有 未完成的订单
#printJson (okcoinFuture.future_orderinfo('btc_usd','this_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单
#printJson (okcoinFuture.future_orderinfo('btc_usd','next_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单
#printJson (okcoinFuture.future_orderinfo('eth_usd','this_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单
#printJson (okcoinFuture.future_orderinfo('eth_usd','next_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单
#printJson (okcoinFuture.future_orderinfo('bch_usd','this_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单
#printJson (okcoinFuture.future_orderinfo('bch_usd','next_week', orderId='-1', status='2',currentPage='0',pageLength='10')) # 所有 已经完成的订单

#print (u'(9) 期货逐仓账户信息')
#printJson (okcoinFuture.future_userinfo_4fix())

#print (u'(10) 期货逐仓持仓信息')
#printJson (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))

   
