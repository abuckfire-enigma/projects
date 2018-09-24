# Cases for using underscores in python:
1. Storing the value of the last expression in the interpreter
2. For ingnoring the specific values
3. To give special meanings and functions to name of variables/functions
4. To use internalization or localization functions
5. To sperate the digits of number literal value


## Case 1: Interpreter
```
>>> 10 
10 
>>> _ 
10 
>>> _ * 3 
30 
>>> _ * 20 
600
```
## Case 2: Ignoring Values
* Ignore value while unpacking: `x, _, y = (1, 2, 3) # x = 1, y = 3`
* Extending Unpacking (python 3.x only): `x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5`
* Ignore the index:
```
for _ in range(10):
    do_something()
```
* Ignore a value of specific location:
```
for _, val in list_of_tuple:
    do_something()
```

## Case 3: Special Meanings
1. `_single_leading_underscore`: for *private* variables, functions, methods, and classes in a module. Anything with this convention is ignored when importing the module
2. `single_trailing_underscore_`: Convention for avoiding conflict with python keywords or built-ins (eg. `list_ = [1,2,3]`)
3. `__double_leading_underscore`: see "mangling"
4. `__double_leading_and_trailing_underscore__`: Used for so-called magic method variables or methods (i.e. `__init__`, `__len__`)

## Case 4: Internalization/Localization
* See `gettext` documentation 

## Case 5: Digit Seperation (Python >3.6)
```
dec_base = 1_000_000 -> 1000000
bin_base = 0b_1111_0000 -> 240
hex_base = 0x_1234_abcd -> 305441741
```