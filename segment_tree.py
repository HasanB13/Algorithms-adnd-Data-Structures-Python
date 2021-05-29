#Problem's variables 
size = int(1e5+5)
numbers = []


def initialize_array(siz, arr=[]):
	for i in range(0,siz):
		arr.append(0)



#Function to build segment tree
def build(position, left, right):
	if left==right:
		segment_tree[position] = numbers[left]
		return

	mid = (left+right)//2
	build(2*position, left, mid)
	build(2*position+1, mid+1, right)

	segment_tree[position] = segment_tree[2*position] + segment_tree[2*position+1]



#Function to update the numbers array and the segment tree
def update(position, left, right, idx, value):
	if left == right:
		numbers[idx] = value
		segment_tree[position] = value
		return

	mid = (left+right)//2
	if idx <= mid:
		update(2*position, left, mid, idx, value)
	else:
		update(2*position+1, mid+1, right, idx, value)

	segment_tree[position] = segment_tree[2*position] + segment_tree[2*position+1]



#Function to return the answer of the query
# in thist example the query is the sum of subset of the numbers array
def query(position, left, right, query_left, query_right):
	if query_left<=left and right<=query_right:
		return segment_tree[position]

	if right<query_left or left>query_right:
		return 0

	mid = (left+right)//2
	return query(2*position, left, mid, query_left, query_right)+query(2*position+1, mid+1, right, query_left, query_right)




global segment_tree
segment_tree = []
initialize_array(4*size, segment_tree)

#the inputs
numbers = [int(x) for x in input().split()]
number_of_querys = int(input())

#build the sement tree
build(1,0,len(numbers)-1)
for i in range(number_of_querys):
	#there is two type of querys: 1 for get the sum and 0 for update
    input_query = [int(x) for x in input().split()]
    query_type = input_query[0]
    if input_query[0]==1:
    	query_left = input_query[1] - 1
    	query_right = input_query[2] -1
    	print(query(1, 0, len(numbers)-1, query_left, query_right))
    
    else:
    	query_index = input_query[1] - 1
    	query_value = input_query[2]
    	update(1, 0, len(numbers)-1, query_index, query_value)



#Sample input:
# 1 2 3 4 5 6
# 3
# 1 2 5
# 0 2 0
# 1 2 5

#Sample output:
# 14
# 12