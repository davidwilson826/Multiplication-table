"""
multiplication-table.py
Author: David Wilson
Credit: Mr. Dennison
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be able to determine the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
import sys
Width = int(input("Width of multiplication table: "))
Height = int(input("Height of multiplication table: "))

LPrint = 1

while LPrint <= Height:
    for item in [(LPrint*n) for n in range(1, Width)]:
        print(("{0:>3}".format(item)), end=" ")
    print(("{0:>3}".format(LPrint*(Width))))
    LPrint = LPrint+1