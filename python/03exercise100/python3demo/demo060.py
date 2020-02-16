# Python 移除字典点键值(key/value)对
test_dict = {"1": 1, "2": 2}
del test_dict["2"]
test_dict.pop("2")
new_dict = {key: val for key, val in test_dict.items() if key != "2"}
