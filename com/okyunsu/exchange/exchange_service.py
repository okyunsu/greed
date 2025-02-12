from com.okyunsu.exchange.exchange_model import ExchangeModel


class ExchangeService:
    def __init__(self):
        pass

    def excute(self, exchange : ExchangeModel) -> ExchangeModel:
        price = exchange.price
        paid = exchange.paid
        change = paid - price

        currency_list = []
        currency_unit = ""

        if exchange.currency == "USD":
            doller_list = self.get_doller_list()
            currency_list = doller_list
            currency_unit = '달러'
            page = "exchange/exchange_doller.html"
            print("달러")
        elif exchange.currency == "WON": 
            won_list = self.get_won_list()
            currency_list = won_list
            currency_unit = '원'
            page = "exchange/exchange_won.html"

            print("원")
        else:
            print("잘못된 화폐단위입니다.")

        
      
        currency_dict = self.get_currency_dict(change, currency_list)
        self.get_print(currency_dict)
        print("🐕",currency_unit)
        exchange.result =  self.format_currency_count(currency_dict, currency_unit)
        exchange.page = page    
         
        return exchange

    def get_print(self, currency_dict):
        print("--------거스름돈--------")
        for won, count in currency_dict.items():
            print(f"{won}원: {count}개")
        print("-----------끝-----------")

    def get_currency_dict(self, change , currency_list)->dict:
        
        amount = change 
        currency_dict = {}
        
        for currency in currency_list:
            currency_dict[currency] = amount//currency
            amount %= currency
        return currency_dict


    def get_won_list(self):
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        won_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500, 
                      WON_100, WON_50, WON_10]
                      
        return won_list

    def format_currency_count(self, currency_dict, currency_unit):
        temp = ''
        for currency, count in currency_dict.items():
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp
    
    def get_doller_list(self):
        Doller_100 = 100
        Doller_50 = 50
        Doller_20 = 20
        Doller_10 = 10
        Doller_5 = 5
        Doller_2 = 2
        Doller_1 = 1

        doller_list = [Doller_100, Doller_50, Doller_20, Doller_10,
                        Doller_5, Doller_2, Doller_1]
                    
        return doller_list