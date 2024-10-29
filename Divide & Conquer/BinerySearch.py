def BinerySearch(mylist, low, top, x):
	if top >= low:

		mid = (top + low) // 2

		if mylist[mid] > x:
			return BinerySearch(mylist, low, mid - 1, x)
			
		elif mylist[mid] == x:
			return mid

		else:
			return BinerySearch(mylist, mid + 1, top, x)

	else:
		return -1

mylist = list(map(int, input().split()))
	
x = int(input())

result = BinerySearch(mylist, 0, len(mylist)-1, x)

if result != -1:
	print(x)
else:
	print("Not Found")
