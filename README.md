# perfect_number_check
Python solution to check whether a given number is a Perfect Number using simple logic.
# Perfect Number Check 

## Problem Statement
A Perfect Number is a number that is equal to the sum of its proper divisors 
(excluding the number itself).

Write a program to check whether a given number is a Perfect Number.

## Example
Input
28

Output
Perfect Number

Explanation:
Factors of 28 → 1, 2, 4, 7, 14  
Sum = 1 + 2 + 4 + 7 + 14 = 28  
Since the sum equals the number, it is a Perfect Number.

## Input Format
Single integer N

## Output Format
Print:
Perfect Number
or
Not a Perfect Number

## Approach
1. Read the number.
2. Find all divisors except the number itself.
3. Sum those divisors.
4. If the sum equals the number, it is a Perfect Number.
