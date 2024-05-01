## Результати

### Test1 - sorted list, 100 items

	type:merge      result:1.7216
	type:insertion  result:0.1416
	type:tim        result:0.0080

### Test2 - sorted in reverse order list, 100 items

	type:merge      result:1.7576
	type:insertion  result:0.1425
	type:tim        result:0.0080

### Test3 - list after shuffle, 100 items

	type:merge      result:1.9616
	type:insertion  result:0.1422
	type:tim        result:0.0088

### Test4 - list after shuffle, 1000 items

	type:merge      result:33.6486
	type:insertion  result:2.2144
	type:tim        result:0.1442

## Висновок

В всіх випадках алгоритм timsort показав себе значно ефективнішим за два інших\
При зміні розміру масиву з 100 до 1000 можна побачити, що в кожного алгоритму час виріс в ~15 разів, отже можна зробити
висновок, що в всіх них складність O(n log n).   