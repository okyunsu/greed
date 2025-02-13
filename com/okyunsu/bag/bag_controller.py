from com.okyunsu.bag.bag_model import BagModel
from com.okyunsu.bag.bag_service import BagService


class BagController:
    def __init__(self, **kwargs):
        self.capacity = kwargs.get("capacity")
        self.num_items = kwargs.get("num_items")
        self.weights = kwargs.get("weights")
        self.profits = kwargs.get("profits")
        print(self.capacity, self.num_items, self.weights, self.profits)

    def getResult(self) -> BagModel:
        bag = BagModel()
        service = BagService()

        bag.capacity = self.capacity
        bag.num_items = self.num_items
        bag.weights = self.weights
        bag.profits = self.profits
        
        return service.excute(bag) 