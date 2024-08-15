def print_params(a=1, b='строка', c=True):
    print(a, b, c)
values_list = ['раз', True, 26]
values_dict = {'a': 12.3, 'b': 'привет', 'c': 456 }
values_list_2 = [True, 'пока']

print_params()
print_params(5, b=25, c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)