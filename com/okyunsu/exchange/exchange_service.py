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
        page = ""

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
        elif exchange.currency == "YEN": 
            yen_list = self.get_yen_list()
            currency_list = yen_list
            currency_unit = '엔'
            page = "exchange/exchange_yen.html"
            print("엔")
        else:
            print("잘못된 화폐단위입니다.")

        
      
        currency_dict = self.get_currency_dict(change, currency_list)
        self.get_print(currency_dict)
        exchange.result =  self.format_currency_count(currency_dict, currency_unit)
        print(f"🐕{currency_unit}")
        print(f"🐶{currency_list}")
        print(f"😽{currency_dict}")

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
    
    def get_yen_list(self):
        yen_10000 = 100000
        yen_5000 = 5000
        yen_1000 = 1000
        yen_500 = 500
        yen_100 = 100
        yen_50 = 50
        yen_10 = 10
        yen_5 = 5
        yen_1 = 1

        yen_list = [yen_10000, yen_5000, yen_1000, yen_500,
                        yen_100, yen_50, yen_10, yen_5, yen_1]
                    
        return yen_list