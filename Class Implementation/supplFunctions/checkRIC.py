import refinitiv.dataplatform as rdp
import pandas as pd
from datetime import timedelta
from datetime import datetime


def check_ric(ric, maturity):
    exp_date = pd.Timestamp(maturity)

    if pd.Timestamp(maturity) < datetime.now():
        sdate = (exp_date - timedelta(90)).strftime('%Y-%m-%d')
        edate = exp_date.strftime('%Y-%m-%d')
    else:
        sdate = (datetime.now() - timedelta(90)).strftime('%Y-%m-%d')
        edate = datetime.now().strftime('%Y-%m-%d')

    if ric.split('.')[1][0] == 'U':
        prices = rdp.get_historical_price_summaries(ric,  start=sdate, end=edate, interval=rdp.Intervals.DAILY,
                                                    fields=['BID', 'ASK', 'TRDPRC_1'])
    else:
        prices = rdp.get_historical_price_summaries(ric,  start=sdate, end=edate, interval=rdp.Intervals.DAILY,
                                                    fields=['BID', 'ASK', 'TRDPRC_1', 'SETTLE'])
    return ric, prices
