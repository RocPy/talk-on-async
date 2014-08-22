
def numbers():
	print('hi')
	nums = [1,2,3]
	for num in nums:
		yield num

numberGenerator = numbers()
print('Begin output')
print(next(numberGenerator))
print(next(numberGenerator))
print(next(numberGenerator))