from com.okyunsu.bag.bag_model import BagModel


class BagService:
    def __init__(self):
        pass

    def excute(self, bag: BagModel) -> BagModel:
        capacity = bag.capacity
        num_items = bag.num_items
        weights_str = bag.weights
        profits_str = bag.profits
    
    
        weights_list = self.clean_and_convert(weights_str)
        profits_list = self.clean_and_convert(profits_str)
        
        items = self.get_items(weights_list, profits_list)
        
        print(capacity, num_items, weights_str, profits_str)

        items = self.sort_items_by_ratio(items) 

        total_value = 0 
        knapsack_contents = [] 

        for weight, profit, ratio in items:
            if capacity >= weight:  
                total_value += profit
                capacity -= weight
                knapsack_contents.append((weight, profit, 1.0))  
                print(f"전부 다 들어간다")
            else:  
                fraction = capacity / weight
                total_value += profit * fraction
                knapsack_contents.append((weight, profit, fraction))  
                print("일부만 들어간다")
                break  
                

        bag.total_value = total_value
        bag.knapsack_contents = knapsack_contents

        return bag

    def get_items(self, weights, profits):
        return [(w, p, p / w) for w, p in zip(weights, profits)]

    def clean_and_convert(self, value):

        if not value:  
            return []

        if isinstance(value, str):  # 문자열이면 쉼표 제거 후 변환
            return list(map(int, value.replace(" ", "").split(",")))

        return value  # 이미 리스트라면 변환 없이 그대로 반환
    
    def sort_items_by_ratio(self, items):
   
        items_with_key = [(item[2], item) for item in items]  # (비율, 원본 튜플) 리스트 생성
        r = len(items_with_key)

        for i in range(r):  
            for j in range(i + 1, r): 
                if items_with_key[i][0] < items_with_key[j][0]:  
                    items_with_key[i], items_with_key[j] = items_with_key[j], items_with_key[i]  

        for i in range(r):
            print("🐈🐶", i)
      
        sorted_items = [item for _, item in items_with_key]
        return sorted_items
    
    capacity1 = 10 
    profit1 = 16
    profit2 = 4
    profit3 = 12
    profit4 = 15
    weight1 = 4
    weight2 = 2
    weight3 = 4
    weight4 = 3
    profit_per_weight = [profit1/weight1, profit2/weight2, profit3/weight3, profit4/weight4]


    item1 = {"name":"item1", "profit":profit1, "weight":weight1, "profit_per_weight":profit_per_weight[0]}
    item2 = {"name":"item2", "profit":profit2, "weight":weight2, "profit_per_weight":profit_per_weight[1]}
    item3 = {"name":"item3", "profit":profit3, "weight":weight3, "profit_per_weight":profit_per_weight[2]}
    item4 = {"name":"item4", "profit":profit4, "weight":weight4, "profit_per_weight":profit_per_weight[3]}

    items = [item1, item2, item3, item4]
    
    
        

    for i in range(4):  
        for j in range(i+1, 4): 
            if items[i].get("profit_per_weight") < items [ j ].get("profit_per_weight"): 
                items[i], items[j] = items[j], items[i] 

    for i in items:
        print("🐶🐶🐺", i.get("name"))
       

    result = 0

    for i in range(4):
        if items[i].get("weight") <= capacity1:
            capacity1 -= items[i].get("weight")
            result += items[i].get("profit")
            print(result)
        else:
            fraction = capacity1 / items[i].get("weight")
            result += items[i].get("profit") * fraction
            print("끝", result)
           
            break
    print("🐮🐮🐮", result)


