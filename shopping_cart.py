class ShoppingCart():
    # write your code here
    def __init__(self, emp_discount=None):
        self._total = 0
        self._employee_discount = emp_discount
        self._items = []

    def add_item(self, name, price, quantity=1):
        self._items.append({"name": name, "price": price})
        self._total += price
        return self.total
