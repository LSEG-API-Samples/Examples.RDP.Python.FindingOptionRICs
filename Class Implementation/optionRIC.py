import refinitiv.dataplatform as rdp
import pandas as pd
from datetime import datetime
from getExchanges import get_exchanges
from checkRIC import check_ric


class Option_RIC:

    def __init__(self, asset, maturity, strike, opt_type):
        if '.' not in asset:
            asset = rdp.convert_symbols(
                asset, from_symbol_type="ISIN", to_symbol_types="RIC")['RIC'][0]
        self.asset = asset
        self.maturity = pd.Timestamp(maturity)
        self.strike = strike
        self.opt_type = opt_type
        self.exchange = get_exchanges(self.asset)

    def getAssetAndExchange(self):
        asset_in_ric = {'SSMI': {'EUX': 'OSMI'}, 'GDAXI': {'EUX': 'GDAX'}, 'ATX': {'EUX': 'FATXA'}, 'STOXX50E': {'EUX': 'STXE'},
                        'FTSE': {'IEU': 'LFE', 'EUX': 'OTUK'}, 'N225': {'OSA': 'JNI'}, 'TOPX': {'OSA': 'JTI'}}

        asset_exchange = {}
        if self.asset[0] != '.':
            asset = self.asset.split('.')[0]
        else:
            asset = self.asset[1:]
        for exch in self.exchange:
            if asset in asset_in_ric:
                asset_exchange[exch] = asset_in_ric[asset][exch]
            else:
                asset_exchange[exch] = asset
        return asset_exchange

    def getStrike(self, exch):

        if exch == 'OPQ':
            if type(self.strike) == float:
                int_part = int(self.strike)
                dec_part = str(str(self.strike).split('.')[1])
            else:
                int_part = int(self.strike)
                dec_part = '00'
            if int(self.strike) < 10:
                strike_ric = '00' + str(int_part) + dec_part
            elif int_part >= 10 and int_part < 100:
                strike_ric = '0' + str(int_part) + dec_part
            elif int_part >= 100 and int_part < 1000:
                strike_ric = str(int_part) + dec_part
            elif int_part >= 1000 and int_part < 10000:
                strike_ric = str(int_part) + '0'
            elif int_part >= 10000 and int_part < 20000:
                strike_ric = 'A' + str(int_part)[-4:]
            elif int_part >= 20000 and int_part < 30000:
                strike_ric = 'B' + str(int_part)[-4:]
            elif int_part >= 30000 and int_part < 40000:
                strike_ric = 'C' + str(int_part)[-4:]
            elif int_part >= 40000 and int_part < 50000:
                strike_ric = 'D' + str(int_part)[-4:]

        elif exch == 'HKG' or exch == 'HFE':
            if self.asset[0] == '.':
                strike_ric = str(int(self.strike))
            else:
                strike_ric = str(int(self.strike * 100))

        elif exch == 'OSA':
            strike_ric = str(self.strike)[:3]

        elif exch == 'EUX' or exch == 'IEU':
            if type(self.strike) == float and len(str(int(self.strike))) == 1:
                int_part = int(self.strike)
                dec_part = str(str(self.strike).split('.')[1])[0]
                strike_ric = '0' + str(int_part) + dec_part
            elif (len(str(int(self.strike))) > 1 and exch == 'EUX'):
                strike_ric = str(int(self.strike)) + '0'
            elif (len(str(int(self.strike))) == 2 and exch == 'IEU'):
                strike_ric = '0' + str(int(self.strike))
            elif len(str(int(self.strike))) > 2 and exch == 'IEU':
                strike_ric = str(int(self.strike))

        return strike_ric

    def get_exp_month(self, exchange):
        ident_opra = {'1': {'exp': 'A', 'C_bigStrike': 'a', 'C_smallStrike': 'A', 'P_bigStrike': 'm', 'P_smallStrike': 'M'},
                      '2': {'exp': 'B', 'C_bigStrike': 'b', 'C_smallStrike': 'B', 'P_bigStrike': 'n', 'P_smallStrike': 'N'},
                      '3': {'exp': 'C', 'C_bigStrike': 'c', 'C_smallStrike': 'C', 'P_bigStrike': 'o', 'P_smallStrike': 'O'},
                      '4': {'exp': 'D', 'C_bigStrike': 'd', 'C_smallStrike': 'D', 'P_bigStrike': 'p', 'P_smallStrike': 'P'},
                      '5': {'exp': 'E', 'C_bigStrike': 'e', 'C_smallStrike': 'E', 'P_bigStrike': 'q', 'P_smallStrike': 'Q'},
                      '6': {'exp': 'F', 'C_bigStrike': 'f', 'C_smallStrike': 'F', 'P_bigStrike': 'r', 'P_smallStrike': 'R'},
                      '7': {'exp': 'G', 'C_bigStrike': 'g', 'C_smallStrike': 'G', 'P_bigStrike': 's', 'P_smallStrike': 'S'},
                      '8': {'exp': 'H', 'C_bigStrike': 'h', 'C_smallStrike': 'H', 'P_bigStrike': 't', 'P_smallStrike': 'T'},
                      '9': {'exp': 'I', 'C_bigStrike': 'i', 'C_smallStrike': 'I', 'P_bigStrike': 'u', 'P_smallStrike': 'U'},
                      '10': {'exp': 'J', 'C_bigStrike': 'j', 'C_smallStrike': 'J', 'P_bigStrike': 'v', 'P_smallStrike': 'V'},
                      '11': {'exp': 'K', 'C_bigStrike': 'k', 'C_smallStrike': 'K', 'P_bigStrike': 'w', 'P_smallStrike': 'W'},
                      '12': {'exp': 'L', 'C_bigStrike': 'l', 'C_smallStrike': 'L', 'P_bigStrike': 'x', 'P_smallStrike': 'X'}}

        ident_all = {'1': {'exp': 'A', 'C': 'A', 'P': 'M'},  '2': {'exp': 'B', 'C': 'B', 'P': 'N'},
                     '3': {'exp': 'C', 'C': 'C', 'P': 'O'}, '4': {'exp': 'D', 'C': 'D', 'P': 'P'},
                     '5': {'exp': 'E', 'C': 'E', 'P': 'Q'}, '6': {'exp': 'F', 'C': 'F', 'P': 'R'},
                     '7': {'exp': 'G', 'C': 'G', 'P': 'S'}, '8': {'exp': 'H', 'C': 'H', 'P': 'T'},
                     '9': {'exp': 'I', 'C': 'I', 'P': 'U'}, '10': {'exp': 'J', 'C': 'J', 'P': 'V'},
                     '11': {'exp': 'K', 'C': 'K', 'P': 'W'}, '12': {'exp': 'L', 'C': 'L', 'P': 'X'}}

        if exchange == 'OPQ':
            if self.strike > 999.999:
                exp_month_code = ident_opra[str(
                    self.maturity.month)][self.opt_type + '_bigStrike']
            else:
                exp_month_code = ident_opra[str(
                    self.maturity.month)][self.opt_type + '_smallStrike']
        else:
            exp_month_code = ident_all[str(self.maturity.month)][self.opt_type]

        if self.maturity < datetime.now():
            expired = '^' + \
                ident_all[str(self.maturity.month)]['exp'] + \
                str(self.maturity.year)[-2:]
        else:
            expired = ''

        return exp_month_code, expired

    def ric_prices(self, ric, ric_prices):
        ric, prices = check_ric(ric, self.maturity)
        if prices is not None:
            valid_ric = {ric: prices}
            ric_prices['valid_ric'].append(valid_ric)
        else:
            ric_prices['potential_rics'].append(ric)

        return ric_prices

    def constructRIC(self):
        asset_exchange = self.getAssetAndExchange()
        supported_exchanges = ['OPQ', 'IEU', 'EUX', 'HKG', 'HFE', 'OSA']
        ric_prices = {'valid_ric': [], 'potential_rics': []}
        for exchange, asset in asset_exchange.items():
            if exchange in supported_exchanges:
                strike_ric = self.getStrike(exchange)
                exp_month_code, expired = self.get_exp_month(exchange)

                if exchange == 'OPQ':
                    ric = asset + exp_month_code + \
                        str(self.maturity.day) + \
                        str(self.maturity.year)[-2:] + \
                        strike_ric + '.U' + expired
                    ric_prices = self.ric_prices(ric, ric_prices)

                elif exchange == 'HKG' or exchange == 'HFE':
                    gen_len = ['0', '1', '2', '3']
                    if exchange == 'HFE':
                        gen_len = ['']
                    for i in gen_len:
                        exchs = {'HKG': {'exch_code': '.HK', 'gen': str(i)}, 'HFE': {
                            'exch_code': '.HF', 'gen': ''}}
                        ric = asset + strike_ric + exchs[exchange]['gen'] + exp_month_code + str(
                            self.maturity.year)[-1:] + exchs[exchange]['exch_code'] + expired
                        ric_prices = self.ric_prices(ric, ric_prices)

                elif exchange == 'OSA':
                    for jnet in ['', 'L', 'R']:
                        if self.asset[0] == '.':
                            ric = asset + jnet + strike_ric + exp_month_code + \
                                str(self.maturity.year)[-1:] + '.OS' + expired
                            ric_prices = self.ric_prices(ric, ric_prices)
                        else:
                            for gen in ['Y', 'Z', 'A', 'B', 'C']:
                                ric = asset + jnet + gen + strike_ric + exp_month_code + \
                                    str(self.maturity.year)[-1:] + \
                                    '.OS' + expired
                                ric_prices = self.ric_prices(ric, ric_prices)

                elif exchange == 'EUX' or exchange == 'IEU':
                    exchs = {'EUX': '.EX', 'IEU': '.L'}
                    for gen in ['', 'a', 'b', 'c', 'd']:
                        ric = asset + strike_ric + gen + exp_month_code + \
                            str(self.maturity.year)[-1:] + \
                            exchs[exchange] + expired
                        ric_prices = self.ric_prices(ric, ric_prices)
            else:
                print(f'The {exchange} exchange is not supported yet')
        return ric_prices
