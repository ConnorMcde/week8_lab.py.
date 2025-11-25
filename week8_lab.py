import colorama
from colorama import Fore, Style
import pygame
pygame.init()
colorama.init(autoreset=True)


students = [
{"name": "Alice", "score": 85, "passed": True},
{"name": "Bob", "score": 40, "passed": False},
{"name": "Charlie", "score": 92, "passed": True}]
# 2. The Loop
# "student" is a temporary variable that holds ONE dictionary at a time.

print(f"\n--- {Fore.RED}Class Results{Style.RESET_ALL} ---")
for student in students:
 # 3. Access specific data using the ["keys"]
 name = student["name"]
 score = student["score"]
 # 4. Print it nicely
 print(f"Student: {name} | Score: {score}")
 if student["passed"] is True:
     print(f"Status: {Fore.GREEN}Pass{Style.RESET_ALL}")

 elif student ["passed"] is False:
     print(f"Status: {Fore.RED}Fail{Style.RESET_ALL}")


print("---------------------")