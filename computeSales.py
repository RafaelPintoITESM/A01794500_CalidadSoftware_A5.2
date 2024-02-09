# pylint: disable=invalid-name
"""
computeSales.py - A program to compute the total cost for sales
based on a price catalogue.

This program is designed to be invoked from the command line with
two JSON files as parameters. The first file contains information
about a catalogue of prices for products, and the second file
contains records of sales in a company. The program computes the
total cost for all sales, considering the cost for each item from
the first file, and prints the results on the screen and in a file
named SalesResults.txt.

Requirements:
- The program handles invalid data in the files, displaying errors
   in the console while allowing the execution to continue.
- The name of the program is computeSales.py.
- The minimum format to invoke the program is:
    python computeSales.py priceCatalogue.json salesRecord.json
- The program is designed to manage files with hundreds to thousands of items.
- The execution time for the program is displayed at the end and
   included in the results file.
- The program is compliant with PEP8 standards.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json

Example:
    python computeSales.py prices.json sales.json
"""
import json
import time
import sys


def compute_total_cost(price_catalogue, sales_record):
    """
    Computes the total cost for all sales in the given sales record using
    the provided price catalogue.

    Args:
        price_catalogue (list):
            A list of dictionaries containing product titles and their prices.
        sales_record (list):
            A list of dictionaries containing sales information.

    Returns:
        float: The total cost of all sales.
    """
    total_cost = 0.0
    product_prices = {item["title"]: item["price"] for item in price_catalogue}

    for sale in sales_record:
        product_name = sale.get('Product')
        quantity = sale.get('Quantity')

        if product_name in product_prices:
            product_price = product_prices[product_name]
            total_cost += product_price * quantity
        else:
            print(f" Product {product_name} not found in the price catalogue.")

    return total_cost


def main():
    """
    Main entry point of the program.

    Parses command line arguments, reads price catalogue and sales record from
    files, computes total cost, prints results on the screen and in a file,
    and measures execution time.
    """
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json sales.json")
        sys.exit(1)

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    try:
        with open(price_catalogue_file, 'r', encoding='utf-8') as price_file:
            price_catalogue = json.load(price_file)

        with open(sales_record_file, 'r', encoding='utf-8') as sales_file:
            sales_record = json.load(sales_file)

        start_time = time.time()
        total_cost = compute_total_cost(price_catalogue, sales_record)
        end_time = time.time()

        print(f"Total Cost: ${total_cost:.2f}")

        with open("SalesResults.txt", 'w', encoding='utf-8') as results_file:
            results_file.write(f"Total Cost: ${total_cost:.2f}\n")
            message = f"Execution Time: {end_time - start_time:.2f} seconds\n"
            results_file.write(message)

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in one file {e}")


if __name__ == "__main__":
    main()
