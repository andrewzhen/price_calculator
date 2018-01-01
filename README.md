Price Calculator
This program totals the costs of product items in a cart and returns it. Each 
item has a base price that is found according to the data found on a JSON file.
Furthermore, an artist's markup price as well as the quantity of item are also 
used to determine the final cost of a cart.

Getting Started
Follow these instructions to install a copy of the project on your local machine

Prerequisites
python3

Running the program
To run the program, a cart file and a base prices file need to be specified.

>>>python3 price_calculator.py <cart.json> <base_prices.json>

Running the tests
These tests test for success in loading JSON file data into variables, 
accurately adding an arbitrary cost to the total price, and totaling the price 
for a cart that contains one of every item according to the data in a default 
base price file. There are two options to choose from when running tests on the 
command line. 

1)
>>>python3 test_price_calculator.py
No additional arguments are specified and a default cart and a base prices file
are used to test the program.

2)
>>>python3 test_price_calculator.py <cart.json> <base_prices.json>
A cart and a base prices file are specified, which are used to test the program.

Built With
unittest - Unit testing framework

Author
Andrew Zhen

Acknowledgements
RedBubble for project requirements and example JSON files.