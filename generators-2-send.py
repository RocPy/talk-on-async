
def numbers():
	print('hi')
	nums = [1,2,3]
	for num in nums:
		sentValue = yield num
		print("Look ma I'm back: {}".format(sentValue))

print('')
numberGenerator = numbers()
print('A) Begin output')
yieldedValue = next(numberGenerator)
print('Generator yeilded: ' + str(yieldedValue))
print('')
print('B) Send value to generator')
yieldedValue = numberGenerator.send('b')
print('Generator yeilded: ' + str(yieldedValue))
print('')
print('C) Iterate to final value')
yieldedValue = next(numberGenerator)
print('Generator yeilded: ' + str(yieldedValue))
print('')