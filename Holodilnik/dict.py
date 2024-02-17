import pickle

goods = {}
with open("dict.txt", "rb+") as f:
    pickle.dump(goods, f)
