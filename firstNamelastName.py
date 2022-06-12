# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:31:26 2022

@author: shakti
"""

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)