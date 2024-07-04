def sort_dict_by_values(d:dict):
    return dict(sorted(d.items(), key=lambda x: x[1]))

original_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
sorted_dict = sort_dict_by_values(original_dict)
print(sorted_dict)