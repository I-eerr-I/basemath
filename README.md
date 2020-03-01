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
(F8F0).16
```

# Consistance:
* [bNUM](#bnum) class
* [de2array](#de2array) function
* [de2str](#de2str)   function
* [zeros](#zeros)    function
* [ones](#ones)     function
* [bnum_sum](#bnum_sum) function

# bNUM
> bNUM(value, 
Use this class to carry out operations with any-base number.
You can create **bnum** *(any-base number using bNUM class)* using:
1. Decimal number (integers only):
```python
number = 10 # or any integer you want
base   = 2  # or any base you want starting from 2
bnum   = bNUM(number, base)
```
1. String representation of your any-base number:
```python
str_basenum = '1010'
base        = 2
bnum        = bNUM(str_basenum, base)
```
1. List representation of your any-base number:
```python
list_basenum = ['1', '0', '1', '0']
base         = 2
bnum         = bNUM(list_basenum, base)
```
