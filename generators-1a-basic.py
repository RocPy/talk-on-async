
def numbers():
	print('hi')
	nums = [1,2,3]
	for num in nums:
		yield num

print('Begin output')
for n in numbers():
	print(n)