import unittest
import sys
import re
from price_calculator import Calculator

class CalculatorTest(unittest.TestCase):
	"""Tests the Calculator class."""

	def setUp(self):
		"""Creates a Calculator object and provides the cart and base_prices
		   parameters.
		"""
		self.calc = Calculator(cart, base_prices)

	def test_load_json(self):
		"""Tests the load_json function."""
		self.assertTrue(self.calc.load_json())

	def test_add_cost(self):
		"""Tests the add_cost function."""
		self.calc.add_cost(123)
		self.assertEqual(123, self.calc.return_price())

	def test_add_cart_items(self):
		"""Tests the add_cart_items function."""
		self.calc.load_json()
		self.calc.add_cart_items()
		self.assertEqual(price, self.calc.return_price())

min_args = 3
first_arg = 1
second_arg = 2

# Store command-line arguments
if len(sys.argv) < min_args:
	cart = 'test-cart-34671.json'
	base_prices = 'base-prices.json'
	print('Running tests with default files ...\n')

elif len(sys.argv) == min_args:
	cart = sys.argv[first_arg]
	base_prices = sys.argv[second_arg]
	print('Running tests with', cart, 'and', base_prices, '...\n')

	# Removes argument from sys.argv before unittest.main() to prevent error
	del sys.argv[first_arg:]

else:
	raise Exception('Usage: test_*.py <cart.json> <base_prices.json>\n')

# Stores the price of the cart from the file name
price = int(re.findall(r'\d+', cart)[0])

# Run unittest
unittest.main()