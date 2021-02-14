# Update - I am not maintaining this project so if you have any problem please fork this project and try solving it yourselves.

# Yahoo Finance Python API

Due to rampant deprecation of all the stocks api like pandas_datareader etc, i have to created my own based on the yahoo api v8

The best thing about this api is that it support **Intraday Data** upto 1 minute granularity which a lots of free api doesn't support

## Usage

This command returns a dataframe which can be further modified to add new columns , exported to excel etc

``` python
tata_power = YahooFinance('TATAPOWER.NS', result_range='1mo', interval='15m', dropna='True').result
```


### Demo
![Alt Text](/res/demo.gif)

## Installation

``` bash
git clone https://github.com/mayankwadhwa/yahoo_finance_api.git
cd yahoo_finance_api
python setup.py install
```

### Requirements

- Pandas
- Request

### Note

Make sure to use TICKER symbol from yahoo finance website
https://in.finance.yahoo.com/ 
