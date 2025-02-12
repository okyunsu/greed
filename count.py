class Count:
    def get_unit_count(self, change , money_list):
        amount = change 
        money_dict = {}
        
        for money in money_list:
            money_dict[money] = amount//money
            amount %= money
        return money_dict