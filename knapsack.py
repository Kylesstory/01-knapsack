class Item(object): # An item object 
	"""docstring for Item"""
	def __init__(self, weight, value):
		super(Item, self).__init__()
		self.weight = weight
		self.value = value

def knapsack(items, capacity): 
	## the knapsack algorithm based on dynamic programming for higher item numbers or higher weight capacity
	array = [0] * (capacity + 1)
	items.sort(key = lambda t: t.weight) # sort for better performance
	for t in items:
		for j in range(capacity, t.weight - 1, -1):
			if array[j - t.weight] + t.value > array[j]: array[j] = array[j - t.weight] + t.value
	return(array[capacity])

def check(choices, items): 
	## given a binary series, it returns the sum of weights and values
	totalWeights = totalValues = 0
	for i in range(len(choices)):
		if choices[i] == '1':
			totalWeights += items[i].weight
			totalValues += items[i].value
	return totalWeights, totalValues

def bruteForce(items, capacity): 
	## the brute force solution for less item numbers and less weight capacity
	length = len(items)
	_max = 0
	for index in range(2**length):
		choices = bin(index)[2:].zfill(length)
		weight, value = check(choices, items)
		if weight <= capacity and value > _max: _max = value
	return _max

## the main entry point of the program
items = [] # the whole items
capacity = -1
with open('./your-input-file.txt', 'r') as f: # enter your file path which might be located at the same directory as to the program file
	# format like: capacity \n weight_1 \t value_1 \n weight_2 \t value_2 \n ... 
	line = f.readline()
	while len(line): # data read and regulation
		if line[0] != '#' and line != '\n': # sentence begins with # will be omitted
			if capacity == -1: capacity = int(line.replace('\n', '')) # initialize the capacity
			else:
				st = line.split(', ') 
				items.append(Item(int(st[0]), float(st[1].replace('\n', '')))) # the value might be modified to int for some integer cases
		line = f.readline()

# the item selection: knapsack algorithm for many items; or brute force for less items.
print("The highest value among %d items with capacity %d is %.4f." % (len(items), capacity, (knapsack(items, capacity) if ( (2 ** len(items)) > capacity ) else bruteForce(items, capacity))))