import requests

class IOBase:
    URL_ACCOUNT_STATE = "/api/v2/estadocuenta"
    URL_MARKET_RATES = "/api/v2/Cotizaciones/{instrument}/{panel}/{country}"
    URL_MUTUAL_FUND = "/api/v2/Titulos/FCI/{symbol}"
    URL_MUTUAL_FUNDS = "/api/v2/Titulos/FCI"
    URL_MUTUAL_FUNDS_ADMINS = "/api/v2/Titulos/FCI/Administradoras"
    URL_MUTUAL_FUNDS_TYPES = "/api/v2/Titulos/FCI/TipoFondos"
    URL_OPERATIONS = "/api/v2/operaciones/"
    URL_PORTFOLIO = "/api/v2/portafolio/{country}"
    URL_TOKEN = "/token"


class IOWrapper(IOBase):
    def __init__(self):
        self.api = ""
        self.access_token = ""
        self.refresh_token = ""
        self.token_issued = ""
        self.token_expires = ""

    def _get_bearer_header(self):
        return {"Authorization": "Bearer " + self.access_token}

    def _store_token_info(self, response):
        self.access_token = response.get('access_token')
        self.refresh_token = response.get('refresh_token')
        self.token_issued = response.get('.issued')
        self.token_expires = response.get('.expires') 
       
    def get_account_state(self):
        request = requests.get(self.api + self.URL_ACCOUNT_STATE, headers=self._get_bearer_header())
        return request.json()

    def get_market_rates(self, instrument, panel, country):
        request = requests.get(self.api + self.URL_MARKET_RATES.format(instrument=instrument, panel=panel, country=country),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund(self, symbol):
        request = requests.get(self.api + self.URL_MUTUAL_FUND.format(symbol=symbol),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_funds(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS, headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_admins(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_ADMINS, headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_types(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_TYPES, headers=self._get_bearer_header())
        return request

    def get_portfolio(self, country):
        request = requests.get(self.api + self.URL_PORTFOLIO.format(country=country), headers=self._get_bearer_header())
        return request.json()

    def get_operations(self):
        request = requests.get(self.api + self.URL_OPERATIONS, headers=self._get_bearer_header())
        return request.json()

    def get_token(self, username=None, password=None, refresh_token=None, grant_type="password"):
        if grant_type == "password":
            payload = {"username": username, "password": password, "grant_type": grant_type}
        elif grant_type == "refresh_token":
            payload = {"refresh_token": refresh_token, "grant_type": grant_type}
        
        response = requests.post(self.api + self.URL_TOKEN, data=payload)
        self._store_token_info(response.json())
        return response.json()


class IOService(IOWrapper):
    def __init__(self):
        super().__init__()
        self.api = "https://api.invertironline.com"