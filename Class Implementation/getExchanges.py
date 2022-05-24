import refinitiv.dataplatform as rdp


def get_exchanges(asset):

    response = rdp.Search.search(
        query=asset,
        filter="SearchAllCategory eq 'Options' and Periodicity eq 'Monthly' ",
        select=' RIC, DocumentTitle, UnderlyingQuoteRIC,Periodicity, ExchangeCode',
        navigators="ExchangeCode",
        top=10000
    )
    result = response.data.raw["Navigators"]["ExchangeCode"]

    exchange_codes = []
    for i in range(len(result['Buckets'])):
        code = result['Buckets'][i]['Label']
        exchange_codes.append(code)
    return exchange_codes
