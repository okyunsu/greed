
from com.okyunsu.exchange.exchange_model import ExchangeModel
from com.okyunsu.exchange.exchange_service import ExchangeService


class ExchangeController:
    def __init__(self, **kwargs):
        self.price = kwargs.get("price")
        self.paid = kwargs.get("paid")
        self.change = kwargs.get("change") 
        self.currency = kwargs.get("currency")

    def getResult(self) -> ExchangeModel:
        service = ExchangeService()
        exchange = ExchangeModel()
        exchange.paid = self.paid
        exchange.price = self.price
        exchange.change = self.change
        exchange.currency = self.currency
        
        return service.excute(exchange)