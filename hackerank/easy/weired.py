#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    even = n %2 == 0
    if not even:
        print("Weird")
    elif even and 2<=n<=5:
        print("Not Weird")
    elif even and 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")

