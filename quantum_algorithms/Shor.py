"""This module contains functions for solving Shor's algorithm"""
import numpy as np
import math
import random


def is_prime(number: int):
    """
    Tests if a number is prime.
    """
    if n%2==0 or n==1:
        return False
    elif n==2:
        return True
    for d in range(3, int(math.sqrt(n))+1, 2):
        if n%d==0:
            return False
    return True

def find_lowest_periond(a, N):
    """
    Find the lowest period, r.
    """
    for r in range(1, N, 1):
        remainder=(a^r)%N
        if remainder==1:
            break
    return remainder


def Shors_algorithm(N: int):
    """
    This function solves Shor's algorithm manually, finding the smallest positive integer r such that a^r = 1 modN.

    Inputs
    ------
    N : int
        A composite integer that is the product of two or more distinct prime numbers. 
    """

    #Determination of a, an integer that is coprime to N and chosen at random. 
    a=random.randint(1, N)

    #Validation that N is already prime.
    if is_prime(N):
        print(f"{N} is prime. Shor's algorithm is not needed.")
        return 
    
    #Validation that a is a coprime number
    if math.gcd(a, N)!=1:
        print(f"{N} and {a} are not coprime. Shor's algorithm is not needed.")

    #Calculate the period of r such that a^r=1(mod N)
    r=find_period(a, N)

    #Check if r is even or odd
    if r%2=1: 
        a=random.randint(1, N)
        r=find_period(a, N)
