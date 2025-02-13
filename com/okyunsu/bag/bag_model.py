from dataclasses import dataclass

@dataclass
class BagModel:
    capacity : int
    num_items : int
    weights : int
    profits : int
    total_value : int
    knapsack_contents : int


    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self._capacity = capacity

    @property
    def num_items(self) -> int:
        return self._num_items

    @num_items.setter
    def num_items(self, num_items: int):
        self._num_items = num_items

    @property
    def weights(self) -> int:
        return self._weights

    @weights.setter
    def weights(self, weights: int):
        self._weights = weights

    @property
    def profits(self) -> int:
        return self._profits

    @profits.setter
    def profits(self, profits: int):
        self._profits = profits

    
    @property
    def total_value(self) -> int:
        return self._total_value

    @total_value.setter
    def total_value(self, total_value: int):
        self._total_value = total_value

    @property
    def knapsack_contents(self) -> int: 
        return self._knapsack_contents

    @knapsack_contents.setter
    def knapsack_contents(self, knapsack_contents: int):
        self._knapsack_contents = knapsack_contents
