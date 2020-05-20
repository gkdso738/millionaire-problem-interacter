# millionaire-problem-interacter

## Introduction
Yao's Millionaire problem is a classic problem in secure multiparty computation. Two people can decide who has larger number without disclosing any information about actual number. This is an implementation of Lin and Tseng's approach, with complexity polynomial with respect to the digits.

This implementation serves two functions, compare two numbers or decide whether two strings are identical.

## Prerequisites

It works with Python 3.x, with nonstandard library `gmpy2`.

## Usage

There are two modes of this interactor. Mode 1 is the typical millionaire problem, compare two side's numbers without disclosing them. Mode 2 is comparing two strings, decide whether they are identical, without disclosing the content.

1. Two people decide who to be side A or side B. They should be honest at all time.
2. A and B will decide a maximum number of bits (or maximum string length) of their input. They should have the same value here.
3. Side A runs `millionaire_side_A.py` and follows instructions to generate `enc_A.txt`, and send to B.
4. Side B puts `enc_A.txt` under the same folder, runs `millionaire_side_B.py` and follows instructions to generate `enc_B.txt`, and send to A.
5. Side A puts `enc_B.txt` under the same folder, runs `millionaire_side_A_2.py` and gets the result.
6. A shares the result with B.

## Remark

For why we should compare two strings with millionaires' protocol but not raw string hash, it's because you can test many possibilities with hashed string but not in this protocol.
