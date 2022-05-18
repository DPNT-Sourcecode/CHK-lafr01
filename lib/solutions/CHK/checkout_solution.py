from functools import partial
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    def n_items_for_p(n, p, n2, p2, item):
        batches_of_n = item["count"] // n
        remaining = item["count"] % n

        if n2 and p2:
            batches_of_n2 = remaining // n2
            remaining = remaining  % n2
            return batches_of_n * p + batches_of_n2*p2 + remaining*item["price"]

        return batches_of_n * p + remaining*item["price"]
    
    def free_X_for_nY(X, n, Y):
        freeXs = items[Y]["count"] // n
        items[X]["count"] = max(items[X]["count"]-freeXs, 0)
    
    def buy_n_get_1_free(n, X):
        print(n, X)
        if items[X]["count"] >= n+1:
            free = items[X]["count"] // (n+1)
            items[X]["count"] -= free
            print(free)


    items = { 
        "A": {"price": 50, "count": 0, "offer": n_items_for_p, "args":(5, 200, 3, 130)},
        "B": {"price": 30, "count": 0, "offer": n_items_for_p, "args":(2, 45, 0, 0)},
        "C": {"price": 20, "count": 0},
        "D": {"price": 15, "count": 0},
        "E": {"price": 40, "count": 0, "offer": free_X_for_nY, "args":("B", 2 , "E")},
        "F": {"price": 10, "count": 0, "offer": buy_n_get_1_free, "args": (2, "F")},
        "G": {"price": 20, "count": 0},
        "H": {"price": 10, "count": 0, "offer": n_items_for_p, "args":(10, 80, 5, 45)},
        "I": {"price": 35, "count": 0},
        "J": {"price": 60, "count": 0},
        "K": {"price": 80, "count": 0, "offer": n_items_for_p, "args":(2, 150, 0, 0)},
        "L": {"price": 90, "count": 0},
        "M": {"price": 15, "count": 0},
        "N": {"price": 40, "count": 0, "offer": free_X_for_nY, "args": ("M", 3, "N")},
        "O": {"price": 10, "count": 0},
        "P": {"price": 50, "count": 0, "offer": n_items_for_p, "args":(5, 200, 0, 0)},
        "Q": {"price": 30, "count": 0, "offer": n_items_for_p, "args":(3, 80, 0, 0)},
        "R": {"price": 50, "count": 0, "offer": free_X_for_nY, "args":("Q", 3, "R")},
        "S": {"price": 30, "count": 0},
        "T": {"price": 20, "count": 0},
        "U": {"price": 40, "count": 0, "offer": buy_n_get_1_free, "args": (3, "U")},
        "V": {"price": 50, "count": 0, "offer": n_items_for_p, "args":(3, 130, 2, 90)},
        "W": {"price": 20, "count": 0},
        "X": {"price": 90, "count": 0},
        "Y": {"price": 10, "count": 0},
        "Z": {"price": 50, "count": 0},

    }
    for item in skus:
        if item not in items: return -1
        items[item]["count"] += 1

    for item in items.values():
        if "offer" in item and item["offer"] != n_items_for_p:
            item["offer"](*item["args"])


    subtotal = 0
    for item in items.values():
        if item.get("offer") == n_items_for_p:
            subtotal += n_items_for_p(*item["args"], item)
        else:
            subtotal += item["price"]*item["count"]

    return int(subtotal)

