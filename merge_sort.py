import random



def mergSort(arr=[]):
	if len(arr)<2:
		return arr

	n = len(arr)//2
	leftArr = mergSort(arr[0:n])
	rightArr = mergSort(arr[n:len(arr)])

	result = []
	i = 0
	j = 0

	while i<len(leftArr) and j<len(rightArr):
		if leftArr[i] <= rightArr[j]:
			result.append(leftArr[i])
			i += 1
		else:
			result.append(rightArr[j])
			j += 1

	if i < len(leftArr):
		result += leftArr[i:]
	if j < len(rightArr):
		result += rightArr[j:]

	return result




#main block of the program
a = []
for _ in range(0,10):
	a.append(random.randint(0,10))

print("the array without sort :\n")
print(a)
print("\nthe array with sort :\n")
sortArr = mergSort(a)
print(sortArr)



