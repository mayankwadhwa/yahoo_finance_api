name = "python_finance_api"


import pandas as pd
import time  as _time
import requests


class YahooFinance:
    def __init__(self, ticker, result_range='1mo', start=None, end=None, interval='15m', dropna=True):
        """
        Return the stock data of the specified range and interval

        Note - Either Use result_range parameter or use start and end
        Note - Intraday data cannot extend last 60 days
        :param ticker:  Trading Symbol of the stock should correspond with yahoo website
        :param result_range: Valid Ranges "1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"
        :param start: Starting Date
        :param end: End Date
        :param interval:Valid Intervals - Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

        :return:
        """
        if result_range is None:
            start = int(_time.mktime(_time.strptime(start, '%d-%m-%Y')))
            end = int(_time.mktime(_time.strptime(end, '%d-%m-%Y')))
            # defining a params dict for the parameters to be sent to the API
            params = {'period1': start, 'period2': end, 'interval': interval}

        else:
            params = {'range': result_range, 'interval': interval}

        # sending get request and saving the response as response object
        url = "https://query1.finance.yahoo.com/v8/finance/chart/{}".format(ticker)
        r = requests.get(url=url, params=params)
        data = r.json()
        # Getting data from json
        error = data['chart']['error']
        if error:
            raise ValueError(error['description'])
        self._result = self._parsing_json(data)
        if dropna:
            self._result.dropna(inplace=True)

    @property
    def result(self):
        return self._result

    def _parsing_json(self, data):
        timestamps = data['chart']['result'][0]['timestamp']
        # Formatting date from epoch to local time
        timestamps = [_time.strftime('%a, %d %b %Y %H:%M:%S', _time.localtime(x)) for x in timestamps]
        volumes = data['chart']['result'][0]['indicators']['quote'][0]['volume']
        opens = data['chart']['result'][0]['indicators']['quote'][0]['open']
        opens = self._round_of_list(opens)
        closes = data['chart']['result'][0]['indicators']['quote'][0]['close']
        closes = self._round_of_list(closes)
        lows = data['chart']['result'][0]['indicators']['quote'][0]['low']
        lows = self._round_of_list(lows)
        highs = data['chart']['result'][0]['indicators']['quote'][0]['high']
        highs = self._round_of_list(highs)
        df_dict = {'Open': opens, 'High': highs, 'Low': lows, 'Close': closes, 'Volume': volumes}
        df = pd.DataFrame(df_dict, index=timestamps)
        df.index = pd.to_datetime(df.index)
        return df

    def _round_of_list(self, xlist):
        temp_list = []
        for x in xlist:
            if isinstance(x, float):
                temp_list.append(round(x, 2))
            else:
                temp_list.append(pd.np.nan)
        return temp_list

    def to_csv(self, file_name):
        self.result.to_csv(file_name)

