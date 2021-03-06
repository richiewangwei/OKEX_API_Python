#!/usr/bin/python
# -*- coding: utf-8 -*-
#期货合约策略类

from datetime import datetime, date, time
import random
from HttpMD5Util import buildMySign,httpGet,httpPost,printJson
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

class BuyPosition:
    def __init__(self, symbol, contract_type):
        self.symbol = symbol
        self.contract_type = contract_type
        self.buy_amount = 0
        self.buy_price = 0.0
        self.open_date = 0
        self.sell_amount = 0
        self.sell_price = 0.0
        self.close_date = 0
        self.profit_percent = 0.0

class SellPosition:
    def __init__(self, symbol, contract_type):
        self.symbol = symbol
        self.contract_type = contract_type
        self.sell_amount = 0
        self.sell_price = 0.0
        self.open_date = 0
        self.buy_amount = 0
        self.buy_price = 0.0
        self.close_date = 0
        self.profit_percent = 0.0

        
class FuturePolicy:

    def __init__(self, symbol, contract_type, open_date_diff, stop_profit_percent, stop_loss_percent):
        self.symbol = symbol
        self.contract_type = contract_type
        self.open_buy_positions = []
        self.close_buy_positions = []
        self.open_sell_positions = []
        self.close_sell_positions = []
        self.last_open_buy_date = 0
        self.last_open_sell_date = 0
        self.open_date_diff = open_date_diff
        self.stop_profit_percent = stop_profit_percent
        self.stop_loss_percent   = stop_loss_percent
        self.open_positions_max_num = 10000
        self.open_pos_diff_max_num = 10000



    # 多单的开仓与平仓
    # 下单-开多仓
    def trade_open_buy(self, buy_amount, buy_price, open_date):
        open_buy_position = BuyPosition(self.symbol, self.contract_type)
        open_buy_position.buy_amount = buy_amount
        open_buy_position.buy_price = buy_price
        open_buy_position.open_date = open_date
        self.open_buy_positions.append(open_buy_position)
        return True

    # 判断是否符合平仓条件
    def is_need_close_buy(self, open_buy_position, last_deal_price):
        # 止损
        if last_deal_price < open_buy_position.buy_price * (1 - self.stop_loss_percent / 100):
            return True
        # 止盈
        if last_deal_price > open_buy_position.buy_price * (1 + self.stop_profit_percent / 100):
            return True
        return False

    # 下单-平多仓
    def trade_close_buy(self, open_buy_position, sell_amount, sell_price, close_date):
        close_buy_position = open_buy_position
        close_buy_position.sell_amount = sell_amount
        close_buy_position.sell_price = sell_price
        close_buy_position.close_date = close_date
        close_buy_position.profit_percent = round((close_buy_position.sell_price / close_buy_position.buy_price - 1.0) * 100.0, 2)
        self.close_buy_positions.append(close_buy_position)
        return True

    # 将仓位从 开仓队列 删除
    def del_pos_from_open_buy(self, need_close_pos_num):
        open_buy_position = self.open_buy_positions.pop(need_close_pos_num)
        return True

    # 遍历所有持有的多头仓位，或者保留，或者平仓
    # ret=0 持仓不动，未平仓
    # ret=1 执行平仓成功
    def scan_all_open_buy_positions(self, last_deal_price, close_date):
        need_close_pos_num = -1
        for i in range(len(self.open_buy_positions)):
            # 判断是否平仓
            if  (not (self.is_need_close_buy(self.open_buy_positions[i], last_deal_price)) ) and    \
                (not (i == 0 and len(self.open_buy_positions) > len(self.open_sell_positions) + self.open_pos_diff_max_num) ):
                continue
            # 平仓
            sell_amount = self.open_buy_positions[i].buy_amount
            sell_price = last_deal_price
            b = self.trade_close_buy(self.open_buy_positions[i], sell_amount, sell_price, close_date)
            need_close_pos_num = i
            break
        if need_close_pos_num >= 0 and need_close_pos_num < len(self.open_buy_positions):
            b = self.del_pos_from_open_buy(need_close_pos_num)
            return 1
        return 0

    # 建立多头仓位
    # ret=0 持仓不动，未开仓
    # ret=1 执行开仓成功
    def build_open_buy_positions(self, last_deal_price, open_date):
        if open_date - self.last_open_buy_date < self.open_date_diff:
            return 0
        if len(self.open_buy_positions) >= self.open_positions_max_num:
            return 0
        buy_amount = 1
        buy_price = last_deal_price
        self.trade_open_buy(buy_amount, buy_price, open_date)
        if self.last_open_buy_date > 0:
            self.last_open_buy_date = open_date
        else:
            rand_int = random.randrange(self.open_date_diff)
            self.last_open_buy_date = open_date + rand_int
        return 1

    # 执行一次完整的 先平仓后开仓 的过程
    # ret=0 持仓不动，没有平仓或开仓
    # ret=1 执行平仓或开仓成功
    def do_open_close_buy_positions(self, last_deal_price, ticker_date):
        ret = self.scan_all_open_buy_positions(last_deal_price, ticker_date)
        if ret == 1:
            return 1
        ret = self.build_open_buy_positions(last_deal_price, ticker_date)
        if ret == 1:
            return 1
        return 0



    # 空单的开仓与平仓
    # 下单-开空仓
    def trade_open_sell(self, sell_amount, sell_price, open_date):
        open_sell_position = SellPosition(self.symbol, self.contract_type)
        open_sell_position.sell_amount = sell_amount
        open_sell_position.sell_price = sell_price
        open_sell_position.open_date = open_date
        self.open_sell_positions.append(open_sell_position)
        return True

    # 判断是否符合平仓条件
    def is_need_close_sell(self, open_sell_position, last_deal_price):
        # 止损
        if last_deal_price > open_sell_position.sell_price * (1 + self.stop_loss_percent / 100):
            return True
        # 止盈
        if last_deal_price < open_sell_position.sell_price * (1 - self.stop_profit_percent / 100):
            return True
        return False

    # 下单-平空仓
    def trade_close_sell(self, open_sell_position, buy_amount, buy_price, close_date):
        close_sell_position = open_sell_position
        close_sell_position.buy_amount = buy_amount
        close_sell_position.buy_price = buy_price
        close_sell_position.close_date = close_date
        close_sell_position.profit_percent = round((1.0 - close_sell_position.buy_price / close_sell_position.sell_price) * 100.0, 2)
        self.close_sell_positions.append(close_sell_position)
        return True

    # 将仓位从 开仓队列 删除
    def del_pos_from_open_sell(self, need_close_pos_num):
        open_sell_position = self.open_sell_positions.pop(need_close_pos_num)
        return True

    # 遍历所有持有的空头仓位，或者保留，或者平仓
    # ret=0 持仓不动，未平仓
    # ret=1 执行平仓成功
    def scan_all_open_sell_positions(self, last_deal_price, close_date):
        need_close_pos_num = -1
        for i in range(len(self.open_sell_positions)):
            # 判断是否平仓
            if  (not (self.is_need_close_sell(self.open_sell_positions[i], last_deal_price)) ) and  \
                (not (i == 0 and len(self.open_sell_positions) > len(self.open_buy_positions) + self.open_pos_diff_max_num) ):
                continue
            # 平仓
            buy_amount = self.open_sell_positions[i].sell_amount
            buy_price = last_deal_price
            b = self.trade_close_sell(self.open_sell_positions[i], buy_amount, buy_price, close_date)
            need_close_pos_num = i
            break
        if need_close_pos_num >= 0 and need_close_pos_num < len(self.open_sell_positions):
            b = self.del_pos_from_open_sell(need_close_pos_num)
            return 1
        return 0

    # 建立空头仓位
    # ret=0 持仓不动，未开仓
    # ret=1 执行开仓成功
    def build_open_sell_positions(self, last_deal_price, open_date):
        if open_date - self.last_open_sell_date < self.open_date_diff:
            return 0
        if len(self.open_sell_positions) >= self.open_positions_max_num:
            return 0
        sell_amount = 1
        sell_price = last_deal_price
        self.trade_open_sell(sell_amount, sell_price, open_date)
        if self.last_open_sell_date > 0:
            self.last_open_sell_date = open_date
        else:
            rand_int = random.randrange(self.open_date_diff)
            self.last_open_sell_date = open_date + rand_int
        return 1

    # 执行一次完整的 先平仓后开仓 的过程
    # ret=0 持仓不动，没有平仓或开仓
    # ret=1 执行平仓或开仓成功
    def do_open_close_sell_positions(self, last_deal_price, ticker_date):
        ret = self.scan_all_open_sell_positions(last_deal_price, ticker_date)
        if ret == 1:
            return 1
        ret = self.build_open_sell_positions(last_deal_price, ticker_date)
        if ret == 1:
            return 1
        return 0



    # 输出：所有仓位的情况
    def print_all_positions(self, last_deal_price):
        s = ''
        all_positions_profit_percent_sum = 0.0
        buy_positions_profit_percent_sum = 0.0
        sell_positions_profit_percent_sum = 0.0
        success_num = 0
        fail_num = 0
        open_buy_profit_percent_sum = 0.0
        open_sell_profit_percent_sum = 0.0
        open_success_num = 0
        open_fail_num = 0
        # 输出：当前持仓，多头
        for i in range(len(self.open_buy_positions)):
            s += 'buy__price\t%.2f' % self.open_buy_positions[i].buy_price
            s += '\topen_date='
            if self.open_buy_positions[i].open_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.open_buy_positions[i].open_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += '\tbuy_amount='
            s += str(self.open_buy_positions[i].buy_amount)
            s += '\tsell_price='
            s += str(self.open_buy_positions[i].sell_price)
            s += '\tclose_date='
            if self.open_buy_positions[i].close_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.open_buy_positions[i].close_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += '\tsell_amount='
            s += str(self.open_buy_positions[i].sell_amount)
            s += '\topen_buy[%d]' % i
            s += ' symbol='
            s += self.open_buy_positions[i].symbol
            s += ' contract='
            s += self.open_buy_positions[i].contract_type
            s += '\n'
        # 输出：当前持仓，空头
        for i in range(len(self.open_sell_positions)):
            s += 'sell__price\t%.2f' % self.open_sell_positions[i].sell_price
            s += '\topen_date='
            if self.open_sell_positions[i].open_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.open_sell_positions[i].open_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += '\tsell_amount='
            s += str(self.open_sell_positions[i].sell_amount)
            s += '\tbuy_price='
            s += str(self.open_sell_positions[i].buy_price)
            s += '\tclose_date='
            if self.open_sell_positions[i].close_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.open_sell_positions[i].close_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += '\tbuy_amount='
            s += str(self.open_sell_positions[i].buy_amount)
            s += '\topen_sell[%d]' % i
            s += ' symbol='
            s += self.open_sell_positions[i].symbol
            s += ' contract='
            s += self.open_sell_positions[i].contract_type
            s += '\n'
        # 输出：已平仓位，多头
        for i in range(len(self.close_buy_positions)):
            s += 'prof_%= '
            s += '%+.2f' % self.close_buy_positions[i].profit_percent
            s += '%'
            s += ' =' + str(self.close_buy_positions[i].sell_price) + '/' + str(self.close_buy_positions[i].buy_price) + '-1'
            s += '  buy_price='
            s += str(self.close_buy_positions[i].buy_price)
            s += '  open_date='
            if self.close_buy_positions[i].open_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.close_buy_positions[i].open_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += ' buy_amount='
            s += str(self.close_buy_positions[i].buy_amount)
            s += ' sell_price='
            s += str(self.close_buy_positions[i].sell_price)
            s += '  close_date='
            if self.close_buy_positions[i].close_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.close_buy_positions[i].close_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += ' sell_amount='
            s += str(self.close_buy_positions[i].sell_amount)
            s += ' close_buy[%d]' % i
            s += ' symbol='
            s += self.close_buy_positions[i].symbol
            s += ' contract='
            s += self.close_buy_positions[i].contract_type
            s += '\n'
        # 输出：已平仓位，空头
        for i in range(len(self.close_sell_positions)):
            s += 'prof_%= '
            s += '%+.2f' % self.close_sell_positions[i].profit_percent
            s += '%'
            s += ' =1-' + str(self.close_sell_positions[i].buy_price) + '/' + str(self.close_sell_positions[i].sell_price)
            s += '  sell_price='
            s += str(self.close_sell_positions[i].sell_price)
            s += '  open_date='
            if self.close_sell_positions[i].open_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.close_sell_positions[i].open_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += ' sell_amount='
            s += str(self.close_sell_positions[i].sell_amount)
            s += ' buy_price='
            s += str(self.close_sell_positions[i].buy_price)
            s += '  close_date='
            if self.close_sell_positions[i].close_date > 10 ** 9:
                dt = datetime.fromtimestamp(self.close_sell_positions[i].close_date)
                s += dt.isoformat(' ')
            else:
                s += '0'
            s += ' buy_amount='
            s += str(self.close_sell_positions[i].buy_amount)
            s += ' close_sell[%d]' % i
            s += ' symbol='
            s += self.close_sell_positions[i].symbol
            s += ' contract='
            s += self.close_sell_positions[i].contract_type
            s += '\n'
        # 输出：所有已平仓位 收益率总和
        for i in range(len(self.close_buy_positions)):
            buy_positions_profit_percent_sum += self.close_buy_positions[i].profit_percent
            if self.close_buy_positions[i].profit_percent > 0:
                success_num += 1
            else:
                fail_num += 1
        for i in range(len(self.close_sell_positions)):
            sell_positions_profit_percent_sum += self.close_sell_positions[i].profit_percent
            if self.close_sell_positions[i].profit_percent > 0:
                success_num += 1
            else:
                fail_num += 1
        # 输出：所有持有仓位 收益率总和
        for i in range(len(self.open_buy_positions)):
            per = round((last_deal_price / self.open_buy_positions[i].buy_price - 1.0) * 100.0, 2)
            open_buy_profit_percent_sum += per
            if per > 0:
                open_success_num += 1
            else:
                open_fail_num += 1
        for i in range(len(self.open_sell_positions)):
            per = round((1.0 - last_deal_price / self.open_sell_positions[i].sell_price) * 100.0, 2)
            open_sell_profit_percent_sum += per
            if per > 0:
                open_success_num += 1
            else:
                open_fail_num += 1
        # 输出：所有仓位的手续费预估（包括已平仓和未平仓）
        fees = -1.5 * round((len(self.open_buy_positions) + len(self.open_sell_positions)) * 0.1 + (len(self.close_buy_positions) + len(self.close_sell_positions)) * 0.1, 2)
        # 输出：所有仓位全部平仓以后的收益率总和预估
        all_positions_profit_percent_sum = buy_positions_profit_percent_sum + sell_positions_profit_percent_sum + open_buy_profit_percent_sum + open_sell_profit_percent_sum + fees
        s += 'prof_sum= '
        s += '%+.2f' % all_positions_profit_percent_sum
        s += '%\tclose_buy_sell= '
        s += '%+.2f' % buy_positions_profit_percent_sum
        s += '% : '
        s += '%+.2f' % sell_positions_profit_percent_sum
        s += '%  open_buy_sell= '
        s += '%+.2f' % open_buy_profit_percent_sum
        s += '% : '
        s += '%+.2f' % open_sell_profit_percent_sum
        s += '%  fees= '
        s += '%.2f' % fees
        s += '%'
        s += '  close_succ_fail= %d : ' % success_num
        s += '%d' % fail_num
        s += '  open_succ_fail= %d : ' % open_success_num
        s += '%d' % open_fail_num
        s += '  sym='
        s += self.symbol
        s += ' con='
        s += self.contract_type
        s += ' open_diff=%d' % (self.open_date_diff / 60)
        s += ' prof=%.2f' % self.stop_profit_percent
        s += ' loss=%.2f' % self.stop_loss_percent
        s += '\n\n'
        print(s)


























    
    
