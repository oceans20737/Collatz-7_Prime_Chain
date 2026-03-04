#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

"""
Verification Script for 7-adic Prime Chains (Survival Mode)
Author: Hiroshi Harada
Date: March 5, 2026
License: MIT

This script verifies the primality and structure of a 7-adic prime chain
generated using the survival mode algorithm, where k ∈ {−1, +5, −3, +3, −5, +1}
is selected based on n mod 7 to ensure the result is an odd integer.

Usage:
    collatz_7adic_prime_chain_verification.py
"""

import sympy

def get_next_7adic_survival(n):
    """
    Computes the next value in the 7-adic survival-mode sequence.
    Returns the next number and the constant k used (as a string).
    """
    rem = n % 7

    if rem == 1:
        k = -1
    elif rem == 2:
        k = +5
    elif rem == 3:
        k = -3
    elif rem == 4:
        k = +3
    elif rem == 5:
        k = -5
    elif rem == 6:
        k = +1
    else:
        return None, None  # rem == 0 → invalid step

    numerator = 8 * n + k
    if numerator % 7 != 0:
        return None, None  # Sanity check failed

    return numerator // 7, f"{k:+d}"

def verify_7adic_chain(n0, length=9):
    """
    Verifies the primality and structure of a 7-adic prime chain starting from n0.
    Prints each step and returns the verified chain.
    """
    print(f"\n=== Verifying 7-adic Prime Chain (Survival Mode) from n₀ = {n0} ===")
    curr = n0
    chain = []

    for i in range(length):
        if sympy.isprime(curr):
            status = "PRIME"
            chain.append(curr)
        else:
            status = "COMPOSITE — Chain Broken"
            print(f"Step {i + 1}: {curr} → {status}")
            break

        print(f"Step {i + 1}: {curr} → {status}")

        if i < length - 1:
            nxt, k_used = get_next_7adic_survival(curr)
            if nxt is None:
                print(f"  [ Invalid step: n mod 7 = {curr % 7} → no valid k ]")
                break
            print(f"    [ Applied k = {k_used} → Next = {nxt} ]")
            curr = nxt

    print(f"\nFinal Result: Verified chain of length {len(chain)}")
    print(f"Chain: {chain}\n")
    return chain

if __name__ == "__main__":
    # Example: Length-9 chain discovered in 7-adic survival mode
    discovery = 68_542_687
    verify_7adic_chain(discovery, length=9)


# In[ ]:




