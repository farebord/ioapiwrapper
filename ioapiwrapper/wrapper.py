import requests


class IOBase:
    URL_ACCOUNT_STATE = "/api/v2/estadocuenta"
    URL_MARKET_RATES = "/api/v2/Cotizaciones/{instrument}/{panel}/{country}"
    URL_MUTUAL_FUND = "/api/v2/Titulos/FCI/{symbol}"
    URL_MUTUAL_FUND_IN_MARKET = "/api/v2/{market}/Titulos/{symbol}"
    URL_MUTUAL_FUND_OPTIONS = "/api/v2/{market}/Titulos/{symbol}/Opciones"
    URL_MUTUAL_FUNDS = "/api/v2/Titulos/FCI"
    URL_MUTUAL_FUNDS_ADMINS = "/api/v2/Titulos/FCI/Administradoras"
    URL_MUTUAL_FUNDS_BY_ADMIN_AND_TYPE = "/api/v2/Titulos/FCI/Administradoras/{admin}/TipoFondos/{fcitype}"
    URL_MUTUAL_FUNDS_TYPES = "/api/v2/Titulos/FCI/TipoFondos"
    URL_MUTUAL_FUNDS_TYPES_BY_ADMIN = "/api/v2/Titulos/FCI/Administradoras/{admin}/TipoFondos"
    URL_INSTRUMENT = "/api/v2/{country}/Titulos/Cotizacion/Paneles/{instrument}"
    URL_INSTRUMENTS = "/api/v2/{country}/Titulos/Cotizacion/Instrumentos"
    URL_OPERATE_BUY = "/api/v2/operar/Comprar"
    URL_OPERATE_SELL = "/api/v2/operar/Vender"
    URL_OPERATE_SUBSCRIBE = "/api/v2/operar/suscripcion/fci"
    URL_OPERATE_RESCUE = "/api/v2/operar/rescate/fci"
    URL_OPERATION = "/api/v2/operaciones/{number}"
    URL_OPERATIONS = "/api/v2/operaciones/"
    URL_OPERATIONS_DELETE = "/api/v2/operaciones/{number}"
    URL_PORTFOLIO = "/api/v2/portafolio/{country}"
    URL_STOCK = "/api/v2/{market}/Titulos/{symbol}/Cotizacion"
    URL_STOCK_HISTORY = "/api/v2/{market}/Titulos/{symbol}/Cotizacion/seriehistorica/{date_from}/{date_to}/{fit}"
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

    def buy(self, market, symbol, amount, price, valid_date, term):
        payload = {
            "mercado": market,
            "simbolo": symbol,
            "cantidad": amount,
            "precio": price,
            "validez": valid_date,
            "plazo": term
        }
        request = requests.post(self.api + self.URL_OPERATE_BUY, json=payload, headers=self._get_bearer_header())
        return request.json()

    def delete_operation(self, number):
        request = requests.delete(self.api + self.URL_OPERATIONS_DELETE.format(number),
                                  headers=self._get_bearer_header())
        return request.json()

    def get_account_state(self):
        request = requests.get(self.api + self.URL_ACCOUNT_STATE, headers=self._get_bearer_header())
        return request.json()

    def get_instrument(self, country, instrument):
        request = requests.get(self.api + self.URL_INSTRUMENT.format(country=country, instrument=instrument),
                               headers=self._get_bearer_header())
        return request.json()

    def get_instruments(self, country):
        request = requests.get(self.api + self.URL_INSTRUMENTS.format(country=country),
                               headers=self._get_bearer_header())
        return request.json()

    def get_market_rates(self, instrument, panel, country):
        request = requests.get(self.api + self.URL_MARKET_RATES.format(instrument=instrument, panel=panel,
                                                                       country=country),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund(self, symbol):
        request = requests.get(self.api + self.URL_MUTUAL_FUND.format(symbol=symbol),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_options(self, market, symbol):
        request = requests.get(self.api + self.URL_MUTUAL_FUND_OPTIONS.format(market=market, symbol=symbol),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_in_market(self, market, symbol):
        request = requests.get(self.api + self.URL_MUTUAL_FUND_IN_MARKET.format(market=market, symbol=symbol),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_types(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_TYPES, headers=self._get_bearer_header())
        return request

    def get_mutual_funds(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS, headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_admins(self):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_ADMINS, headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_types_by_admin(self, admin):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_TYPES_BY_ADMIN.format(admin=admin),
                               headers=self._get_bearer_header())
        return request.json()

    def get_mutual_fund_by_admin_and_type(self, admin, fcitype):
        request = requests.get(self.api + self.URL_MUTUAL_FUNDS_BY_ADMIN_AND_TYPE.format(admin=admin, fcitype=fcitype),
                               headers=self._get_bearer_header())
        return request.json()

    def get_portfolio(self, country):
        request = requests.get(self.api + self.URL_PORTFOLIO.format(country=country), headers=self._get_bearer_header())
        return request.json()

    def get_operation(self, number):
        request = requests.get(self.api + self.URL_OPERATION.format(number=number), headers=self._get_bearer_header())
        return request

    def get_operations(self):
        request = requests.get(self.api + self.URL_OPERATIONS, headers=self._get_bearer_header())
        return request.json()

    def get_stock(self, market, symbol):
        request = requests.get(self.api + self.URL_STOCK.format(market=market, symbol=symbol),
                               headers=self._get_bearer_header())
        return request.json()

    def get_stock_history(self, market, symbol, date_from, date_to, fit):
        request = requests.get(self.api + self.URL_STOCK_HISTORY.format(market=market, symbol=symbol,
                                                                        date_from=date_from, date_to=date_to, fit=fit),
                               headers=self._get_bearer_header())
        return request.json()

    def get_token(self, username=None, password=None, refresh_token=None, grant_type="password"):
        payload = {}
        if grant_type == "password":
            payload = {"username": username, "password": password, "grant_type": grant_type}
        elif grant_type == "refresh_token":
            payload = {"refresh_token": refresh_token, "grant_type": grant_type}
        
        response = requests.post(self.api + self.URL_TOKEN, json=payload)
        self._store_token_info(response.json())
        return response.json()

    def rescue(self, symbol, amount, validate=None):
        payload = {
            "simbolo": symbol,
            "cantidad": amount,
            "soloValidar": validate
        }
        request = requests.post(self.api + self.URL_OPERATE_RESCUE, json=payload, headers=self._get_bearer_header())
        return request.json()

    def sell(self, market, symbol, amount, price, valid_date, term=None):
        payload = {
            "mercado": market,
            "simbolo": symbol,
            "cantidad": amount,
            "precio": price,
            "validez": valid_date,
            "plazo": term
        }
        request = requests.post(self.api + self.URL_OPERATE_SELL, json=payload, headers=self._get_bearer_header())
        return request.json()

    def subscribe(self, symbol, amount, validate):
        payload = {
            "simbolo": symbol,
            "cantidad": amount,
            "soloValidar": validate
        }
        request = requests.post(self.api + self.URL_OPERATE_SUBSCRIBE, json=payload, headers=self._get_bearer_header())
        return request.json()


class IOService(IOWrapper):
    def __init__(self):
        super().__init__()
        self.api = "https://api.invertironline.com"
