def calculate_structure_sum(*args):
    total_sum = 0

    def recursive_count(data):
        nonlocal total_sum
        if isinstance(data, dict):
            for key, value in data.items():
                recursive_count([key, value])
        elif isinstance(data, (list, tuple, set)):
            for i in data:
                recursive_count(i)
        elif isinstance(data, str):
            total_sum += len(data)
        elif isinstance(data, (int, float)):
            total_sum += data

    for j in args:
        recursive_count(j)

    return total_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


