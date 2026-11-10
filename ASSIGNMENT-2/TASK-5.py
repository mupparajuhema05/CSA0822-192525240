def add_buggy(item, order=[]):
    order.append(item)
return order
def add_correct(item, order=None):
    if order is None:
        order = []
    order.append(item)
return order
print("Buggy   :", add_buggy("Tea"), add_buggy("Vada"))
print("Correct :", add_correct("Tea"), add_correct("Vada"))
