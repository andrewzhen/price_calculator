import sys
import os
import json

class Calculator:
	"""Calculates the cost of all items in a cart based on existing pricses."""

	def __init__(self, cart, base_prices):
		"""Initializes variables.

		Args:
			*args: Variable length argument list.
			**kwargs: Arbitrary keyword arguments.
		"""
		self.cents = 100
		self.total_price = 0
		self.cart = cart
		self.base_prices = base_prices

	def load_json(self):
		"""Loads the data from command-line arguments.
			
		Returns:
			bool: True for successful load, False otherwise.
		"""
		with open(self.cart) as cart_data:
			self.cart = json.load(cart_data)

		with open(self.base_prices) as base_prices_data:
			self.base_prices = json.load(base_prices_data)

		return True

	def add_cost(self, price):
		"""Adds to the total value of the current price

		Args: 
			price: The price to be added. 
		"""
		self.total_price += price

	def return_price(self):
		"""Returns the total price of all the items.

		Returns:
			The total price.
		"""
		return self.total_price

	def check_options(self, item_opts, base_opts):
		""" Checks if an item's options in the cart match 
			with a base price item's options.

		Args:
			item_opts: Dictionary of a product's options in a cart.
			base_opts: Dictionary of a product's options in the base prices.

		Returns:
			True if options match, False otherwise.
		"""
		for opt in base_opts:
			if item_opts[opt] not in base_opts[opt]:
				return False
		return True

	def add_cart_items(self):
		"""Sums the total price of each item in the cart."""

		# Iterate through every item in cart
		for item in self.cart:
			for base in self.base_prices:

				# Matches product type
				if item['product-type'] == base['product-type']:

					# If returns True, price calculated using given base price
					# Constant runtime
					if self.check_options(item['options'], base['options']):
						base_price = base['base-price']
						artist_markup = item['artist-markup'] / self.cents

						self.add_cost((base_price + round(base_price * 
							artist_markup)) * item['quantity'])

if __name__ == '__main__':

	# Store command-line arguments
	try:
		cart = sys.argv[1]
		base_prices = sys.argv[2]
	except IndexError:
		print('Usage: price_calculator.py <cart.json> <base_prices.json \n')
		sys.exit(1)

	calc = Calculator(cart, base_prices)
	calc.load_json()
	calc.add_cart_items()
	print(calc.return_price())