"""Week 8 exercise 2"""
import colorama
from colorama import Fore, Style
import pygame
pygame.init()
colorama.init(autoreset=True)


products = [
{"item": "Apple", "price": 0.50},
{"item": "Banana", "price": 0.61},
{"item": "Chocolate", "price": 2.20}
]

print(f"--- {Fore.RED}Price List{Style.RESET_ALL} ---")
# Write your loop here:
for product in products:

    print(f"The price of {product['item']} is £{product['price']}")