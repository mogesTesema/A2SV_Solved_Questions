# 2094C-Brr-Brrr-Patapim

**Problem:** [2094C-Brr-Brrr-Patapim](https://codeforces.com/contest/2094/problem/C)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

Brr Brrr Patapim is trying to learn of Tiramisù's secret passcode, which is a permutation^{\text{∗}} of 2⋅ n elements. To help Patapim guess, Tiramisù gave him an n× n grid G, in which G_{i,j} (or the element in the i-th row and j-th column of the grid) contains p_{i+j}, or the (i+j)-th element in the permutation. 

Given this grid, please help Patapim crack the forgotten code. It is guaranteed that the permutation exists, and it can be shown that the permutation can be determined uniquely.

^{\text{∗}}A permutation of m integers is a sequence of m integers which contains each of 1,2,…,m exactly once. For example, [1, 3, 2] and [2, 1] are permutations, while [1, 2, 4] and [1, 3, 2, 3] are not.


**Input**

The first line contains an integer t — the number of test cases (1 ≤q t ≤q 200).

The first line of each test case contains an integer n (1 ≤q n ≤q 800).

Each of the following n lines contains n integers, giving the grid G. The first of these lines contains G_{1,1}, G_{1,2},…,G_{1,n}; the second of these lines contains G_{2,1}, G_{2,2},…,G_{2,n}, and so on. (1 ≤q G_{i,j} ≤q 2⋅ n).

It is guaranteed that the grid encodes a valid permutation, and the sum of n over all test cases does not exceed 800.


**Output**

For each test case, please output 2n numbers on a new line: p_1,p_2,…,p_{2n}.


**Example**

**Input**

```
3
3
1 6 2
6 2 4
2 4 3
1
1
2
2 3
3 4
```

**Output**

```
5 1 6 2 4 3 
2 1 
1 2 3 4
```
