from dataclasses import dataclass

@dataclass
class ExchangeModel:

    price : int
    paid : int
    change : int
    result : int
    currency : str
    page : str

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, price: int):
        self._price = price

    @property
    def paid(self) -> int:
        return self._paid

    @paid.setter
    def paid(self, paid: int):
        self._paid = paid

    @property
    def change(self) -> int:
        return self._change

    @change.setter
    def change(self, change: int):
        self._change = change

    @property
    def result(self) -> int:
        return self._result

    @result.setter
    def result(self, result: int):
        self._result = result

        
    @property
    def currency(self) -> str:
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        self._currency = currency

    @property
    def page(self) -> str:
        return self._page

    @page.setter
    def page(self, page: str):
        self._page = page


    