# basemath
A small python library to work with numbers of any base

If you need to work with hex, bin, oct, any-base numbers, you can use this simple python library. Any-base number - is the number with the base you need to use it.
Using this library (version 1.0) you can carry out basic operations like: 
* **plus** 
* **minus**
* **mul** 

Also you can **convert a-base number to any other b-base**. You can find decimal number from any-base number anytime.

For example you need to find check sum for IP packet:
```python
# this is ip packet:
packet = '''45000034d5274000380600005fa77a0aac106429'''.upper()
# convert it into bnum type
packet = bNUM(packet, 16)
# get 10 bnums with length 4 and same base 16
parts  = packet.get_k_bnums(10, 4)
# get sum of this 10 bnums
result = bnum_sum(parts)
# cut the head of result and sum it with the rest
# to make result with length 4
result = result.cutdown(4)
# find check sum as FFFF - result
result = bNUM('FFFF', 16, 4) - result
```

The result will be check sum:
```python
'(F8F0).16'
```

# Consistance:
* [bNUM](#bnum) class
  * [length](#length-parameter) parameter
  * [to_len](#to_len) method
  * [cutdown](#cutdown) method
  * [math](#math-operations) operations
  * [other](#other-methods) methods
* [init](#init-functions) functions
* [additional](#additional-functions) functions

# bNUM
> bNUM(value, base, length=None, cut=None)

Use this class to carry out operations with any-base number.
You can create **bnum** *(any-base number using bNUM class)* using:
1. Decimal number (integers only):
```python
    number = 10 # or any integer you want
    base   = 2  # or any base you want starting from 2
    bnum   = bNUM(number, base)
    print(bnum)
    #
    >> '(1010).2'
```
1. String representation of your any-base number:
```python
    str_basenum = '1010'
    base        = 2
    bnum        = bNUM(str_basenum, base)
    print(bnum)
    
    >> '(1010).2'
```
1. List representation of your any-base number:
```python
    list_basenum = ['1', '0', '1', '0']
    base         = 2
    bnum         = bNUM(list_basenum, base)
    print(bnum)
    
    >> '(1010).2'
```
  You can also pass list of bnums as a value:
```python
    bnums = [bNUM('10', 2), bNUM('10', 2)]
    base  = 2
    bnum  = bNUM(bnums, base)
    print(bnum)
    
    >> '(1010).2'
```

As you can mention, the string output of bNUM object useing format (number).base: (10).10, (1010).2, (A).16 and etc
bNUM uses local list ORDER to represent and operate with any element of any base. ORDER list consists of strings that are representations of any-base digits:
ORDER = ['0', '1', '2', '3', '4', ..., 'A', 'B', 'C', ..., 'a', 'b', 'c', ..., !1A, !1B, !1C, ..........]
**THE ELEMENTS ARE CASE-SENSETIVE! SO YOU SHOULD PASS STINGS AND LISTS INTO bNUM KNOWING THAT, E.G. 'A' IS DIFFERENT THAN 'a':
'A' = 10, 'B' = 11, ..., 'Z' = 35, 'a' = 36, 'b' = 37, ..., 'z' = 61, '!1A' = 62, '!1B' = 63, ...***

As you can see, starting after 'z' it goes '!1A' - is the syntax to use next other any-base digits.It goes as ![period of repeating number]letter
There are '!' signs to indicate the start of the new any-base digit that is out of standard range from 0 to 9, from A to Z and from a to z:
 | String representations | Decimals |
 | --- | --- |
 | 0 - 9 | 0 - 9 |
 | A - Z | 10 - 35 |
 | a - z | 36 - 61 |
 | !1A - !1Z | 62 - 87 |
 | !1a - !1z | 88 - 113 |
 | !2A - !2Z | 114 - 139 |
 | !2a - !2z | 140 - 165 |
 | ... | ... |
 | !1000A - !1000Z | 52010 - 52035 |
 | !1000a - !1000z | 52036 - 52061 |
 
 So you can use up to 52061 base numbers.

### The attributes of bNUM object:
 * **string** - string representation of number: bNUM(10, 2).string -> '1010'
 * **array**  - array representation of number: bNUM(10, 2).array -> ['1', '0', '1', '0']
 * **base**   - base of number: bNUM(10, 2).base -> 2
 * **decimal** - decimal number representation: bNUM(10, 2).decimal -> 10

## length parameter
> length=None (int)

Use length parameter to keep this length of bnum. For example, if you pass number with zeros at the highest rank (e.g. '0001010') without length parameter, then this zeros is erased:
```python
  string = '0001010'
  base   = 2
  bnum   = bNUM(string, base)  print(bnum)
  
  >> '(1010).2'
```
Than, use length parameter to keep this length:
```python
  bnum = bNUM(string, base, length=7)
  print(bnum)
  
  >> '(0001010).2'
```

Use length parameter to expand the length of your bnum, filling it with zeros:
```python
  bnum = bNUM('1010', 2, length=10)
  print(bnum, len(bnum))
  
  >> '(0000001010).2', 10
```

If you pass length less than your any-base number, then nothing happens. Length parameter is only working to keep or expand by zeros original length of any-base number:
```python
  bnum = bNUM('01010', 2, length=4)
  print(bnum)
  
  >> '(01010).2'
```

To remove zeros from bnum use [cutzeros](#cutzeros) method.

## to_len
> to_len(length) -> bNUM

Use this method with your bnum to return new bnum with new or the same length. Again, the length can only be the same or expanded by filling with zeros:
```python
  bnum1 = bNUM('1010', 2)
  bnum2 = bnum1.to_len(10)
  print(bnum2)
  
  >> '(0000001010).2'
```

## cutdown
> cutdown(length) -> bNUM

The operation of cutdown can be defined by this algorithm:
  1. Take number A as input with length equals input_len, and reqired length equals output_len
  1. Save elements with the index greater than output_len
  1. Make new number B from this elements by adding zeros to the highest rank of the resulting number
  1. Make new number C from elements that left in A (index less than output_length)
  1. Find sum: B + C
  1. If sum length = output_len, then end of algorithm. If not, then cutdown sum

For example:
We have number 1010 of base 2. The cutdown to length = 3:
  A = 1010
  B = 001 (the first 1 from A expanded to length = 3)
  C = 010 (the rest of A)
  result := 001 + 010 = 011

The cutdown to length = 2:
  A = 1010
  B = 10 (the first to numbers from A)
  C = 10 (the rest elements from A)
  sum := 10 + 10 = 100
  Continuing...
  A = 100
  B = 01
  C = 00
  result := 01 + 00 = 01
  
```python
  bnum1 = bNUM('420', 10)
  bnum2 = bnum1.cutdown(2) # 04 + 20 = 24
  bnum3 = bnum1.cutdown(1) # 42 + 0 = 42; 4 + 2 = 6
  bnum4 = bnum1.cutdown(3) # the same as bnum1
  print(bnum2, bnum3, bnum4)
  
  >> '(24).10', '(6).10', '(420).10'
```

You can pass int cut parameter creating new bNUM to use cutdown operation on created bnum.

## math operations

You can find sum, multiplication, substraction of two bnums using standard python syntax:
```python
 bnum1 = bNUM('1010', 2) # 10
 bnum2 = bNUM('10', 2)   # 2
 print(bnum1 + bnum2)    # output = (1100).2  = 12
 print(bnum1 * bnum2)    # output = (10100).2 = 20
 print(bnum1 - bnum2)    # output = (1000).2  = 8
```

Pay attention, if the minued is less then subtrahend (negative result of substraction), than the return will be decimal number of type int (not a bNUM):
```python
 print(bnum2 - bnum1) # output = -8
 ```
 
 You can carry out some bitwise operations like XOR, bitwise OR and bitwise AND (or just bitwise multiplication):
 ```python
  bnum1 = bNUM('1010', 2) # 10
  bnum2 = bNUM('10', 2)   # 2
  print(bnum1 ^ bnum2)    # 1010 XOR 10 = 1000 = 8
  print(bnum1 | bnum2)    # 1010 OR  10 = 1010 = 10
  print(bnum1 & bnum2)    # 1010 AND 10 = 1000 = 2
```

## other methods

Use your bnums as standard python lists. Use index syntax to get bnum elements of type bNUM. **But, pay attention!** The indices here are not simple: the rank in bnums is left oriented, so are indices. Using indices you passes the power of digit position:
 1 0 1 0 - binary number
 3 2 1 0 - indices/powers of base
 
 A F F 3 C 1 - hex number
 5 4 3 2 1 0 - indices/powers of base
 
```python
 bnum = bNUM('123456789', 10)
 print(bnum.array, bnum.string)
 
 >> ['1', '2', '3', '4', '5', '6', '7', '8', '9'], '123456789'
 
 print(bnum[0], type(bnum[0]))
 
 >> (9).10, <class 'bNUM'>
 
 print(bnum[-1])
 
 >> (1).10
 
 for b in bnum:
  print(b, end=' ')
 
 >> (9).10, (8).10, (7).10, (6).10, (5).10, (4).10, (3).10, (2).10, (1).10
```

Just think of it like you get item by index using reverted bnum.array.
Don't forget that you can change single element of your bnum using index syntax.
```python
 bnum1 = bNUM('1010', 2)
 print(bnum1, bnum1.decimal)
 
 >> (1010).2, 10
 
 bnum1[0] = 1
 print(bnum1, bnum1.decimal)
 
 >> (1011).2, 11
```

Use method insert and append like you use it with python lists.

You can get copy of bNUM object using method *copy*:
```python
 bnum1 = bNUM('1010', 2)
 bnum2 = bnum1.copy()
 print(bnum2)
 
 >> (1010).2
 
 bnum1[0] = 1
 print(bnum1, bnum2)
 
 >> (1011).2, (1010).2
```

Or just copy parameters of another bnum to yours using method *copy_here(bnum)*:
```python
 bnum1 = bNUM('1010', 2)
 bnum2 = bNUM('FFFF', 16)
 bnum1.copy_here(bnum2)
 print(bnum1)
 
 >> (FFFF).16
```
