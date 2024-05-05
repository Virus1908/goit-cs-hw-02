## Результати

### Test1 - sorted list, 100 items

	type:merge      result:0.1823
	type:insertion  result:0.0146
	type:tim        result:0.0010

### Test2 - sorted in reverse order list, 100 items

	type:merge      result:0.1812
	type:insertion  result:0.6493
	type:tim        result:0.0011

### Test3 - list after shuffle, 100 items

	type:merge      result:0.1994
	type:insertion  result:0.3496
	type:tim        result:0.0030

### Test4 - list after shuffle, 1000 items

	type:merge      result:2.7054
	type:insertion  result:35.2331
	type:tim        result:0.0776

## Висновок

В всіх випадках алгоритм timsort показав себе значно ефективнішим за два інших, а сортування вставками навпаки, найменш
ефективне\
При зміні розміру масиву з 100 до 1000 можна побачити, що час роботи алгоритму виріс в: 
- 14 разів для сортування злиттям
- 25 разів для timsort
- 103 рази для сортування вставками

Отже, можна зробити висновок, що сортування злиттям і timsort мають складність O (n log n), а сортування вставками O (n^2)



