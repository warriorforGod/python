requested_toppings= ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("\nSorry, we are out of green peppers right now.")
	else:
		print("\nAdding " + requested_topping + ".")
print("\nFinished making your pizza!")
