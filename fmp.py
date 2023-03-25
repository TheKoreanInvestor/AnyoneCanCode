import secret
import pandas as pd
from urllib.request import urlopen
import json


# api/v3/income-statement/AAPL?period=quarter&limit=400&apikey=099dec1066802f1bf4a1942f672d8500
base_url = 'https://financialmodelingprep.com/'


def get_data_from_fmp(url):
    response = urlopen(url)
    data = response.read().decode('utf-8')
    data = json.loads(data)
    df = pd.DataFrame(data)
    return df


def save_quarterly_data_for_company(symbol='AAPL'):
    income_statement_url = base_url + 'api/v3/{}/{}?period={}&limit={}&apikey={}'.format('income-statement', symbol, 'quarter', 400, secret.fmp_api_key)
    income_statement = get_data_from_fmp(income_statement_url)
    income_statement.to_csv('{}_quarterly_income_statement.csv'.format(symbol))


save_quarterly_data_for_company('MSFT')
