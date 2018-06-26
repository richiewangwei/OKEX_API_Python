#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 期货REST API
from datetime import datetime, date, time
from HttpMD5Util import buildMySign,httpGet,httpPost,printJson

class Ticker:
    def __init__(self):
        self.symbol = ""
        self.contract_type = ""
        self.date = ""
        self.last = 0.0
        self.buy = 0.0
        self.sell = 0.0
        self.high = 0.0
        self.low = 0.0
        self.vol = 0.0
        self.contract_id = 0
        self.unit_amount = 0.0

    def get_str(self):
        s = ''
        s += 'last_price\t%.2f' % self.last
        s += '\ttick_date='
        if int(self.date) > 10 ** 9:
            dt = datetime.fromtimestamp(int(self.date))
            s += dt.isoformat(' ')
        else:
            s += '0'
        s += '\tbuy='
        s += str(self.buy)
        s += ' (%.2f' % (abs(self.last - self.buy)/self.last * 100.0)
        s += '%)'
        s += '  sell='
        s += str(self.sell)
        s += ' (%.2f' % (abs(self.last - self.sell)/self.last * 100.0)
        s += '%)'
        s += '  high='
        s += str(self.high)
        s += '  low='
        s += str(self.low)
        s += '  vol='
        s += str(self.vol)
        s += ' contract_id='
        s += str(self.contract_id)
        s += ' unit='
        s += str(self.unit_amount)
        s += ' symbol='
        s += self.symbol
        s += ' contract='
        s += self.contract_type
        return s


class KLineSingle:
    def __init__(self):
        self.date = ""
        self.open = 0.0
        self.high = 0.0
        self.low  = 0.0
        self.close= 0.0
        self.vol  = 0.0
        self.convertBTC = 0.0

        
class KLineList:
    def __init__(self):
        self.symbol = ""
        self.contract_type = ""
        self.type = ""
        self.size = ""
        self.since = ""
        self.klinelist = []
        
    def get_str(self):
        s = ''
        s += 'KLine\tCount=%d' % len(self.klinelist)
        s += '\tLastKLine='
        for klinesinge in self.klinelist:
            s += '\n'
            s += 'date='
            if int(klinesinge.date) > 10 ** 9:
                dt = datetime.fromtimestamp(int(klinesinge.date))
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += '  open=%.3f' % klinesinge.open
            s += '  high=%.3f' % klinesinge.high
            s += '  low=%.3f' % klinesinge.low
            s += '  close=%.3f' % klinesinge.close
            s += '  vol=%d' % klinesinge.vol
            s += '\tconv_vol=%d' % klinesinge.convertBTC
        return s

    

class FutureAPIClient:

    def __init__(self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    #OKCOIN期货行情信息
    def future_ticker(self,symbol,contractType):
        FUTURE_TICKER_RESOURCE = "/api/v1/future_ticker.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' +symbol
        if contractType:
            params += '&contract_type=' + contractType if params else 'contract_type=' + contractType
        return httpGet(self.__url,FUTURE_TICKER_RESOURCE,params)

    def get_ticker(self,symbol,contractType):
        ticker = Ticker()
        ticker.symbol = symbol
        ticker.contract_type = contractType
        ticker.date = "0"
        try:
            json_obj = self.future_ticker(symbol,contractType)            
            ticker.date = json_obj["date"]
            ticker.last = float(json_obj["ticker"]["last"])
            ticker.buy = float(json_obj["ticker"]["buy"])
            ticker.sell = float(json_obj["ticker"]["sell"])
            ticker.high = float(json_obj["ticker"]["high"])
            ticker.low = float(json_obj["ticker"]["low"])
            ticker.vol = float(json_obj["ticker"]["vol"])
            ticker.contract_id = int(json_obj["ticker"]["contract_id"])
            ticker.unit_amount = float(json_obj["ticker"]["unit_amount"])
        except:
            pass
        return ticker



    #获取OKEx合约K线信息
    def future_kline(self, symbol, contractType, type, size='', since=''): 
        FUTURE_KLINE_RESOURCE = "/api/v1/future_kline.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' + symbol
        if contractType:
            params += '&contract_type=' + contractType if params else 'contract_type=' + contractType
        if type:
            params += '&type=' + type if params else 'type=' + type
        if size:
            params += '&size=' + size if params else 'size=' + size
        if since:
            params += '&since=' + since if params else 'since=' + since
        return httpGet(self.__url,FUTURE_KLINE_RESOURCE,params)

    
    def get_kline(self, symbol, contractType, type, size='', since=''):
        klinelist = KLineList()
        klinelist.symbol = symbol
        klinelist.contract_type = contractType
        klinelist.type = type
        klinelist.size = size
        klinelist.since = since
        try:
            json_obj = self.future_kline(symbol, contractType, type, size, since)
            for item in json_obj:
                klinesingle = KLineSingle()
                klinesingle.date = int(item[0] / 1000)
                klinesingle.open = item[1]
                klinesingle.high = item[2]
                klinesingle.low = item[3]
                klinesingle.close = item[4]
                klinesingle.vol = item[5]
                klinesingle.convertBTC = item[6]
                klinelist.klinelist.append(klinesingle)
        except:
            pass
        return klinelist
                
        

    

