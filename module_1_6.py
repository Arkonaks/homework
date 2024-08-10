my_dict = {'Misha': 1998, 'Anton': 2001, 'Efim': 2000}
print(my_dict)
print(my_dict['Misha'])
print(my_dict.get('Oleg'))
my_dict.update({'Alex': 1980,
                'Petya': 2002})
a = my_dict.pop('Misha')
print(a)
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 1.1, 'Misha', 'Misha'}
print(my_set)
my_set.add(15.2)
my_set.add('apple')
my_set.discard('Misha')
print(my_set)
