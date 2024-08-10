grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = sorted(list(students))
g_1 = sum(grades[0])/len(grades[0])
g_2 = sum(grades[1])/len(grades[1])
g_3 = sum(grades[2])/len(grades[2])
g_4 = sum(grades[3])/len(grades[3])
g_5 = sum(grades[4])/len(grades[4])
summa = {a[0]: g_1, a[1]: g_2, a[2]: g_3, a[3]: g_4, a[4]: g_5}
print(summa)
