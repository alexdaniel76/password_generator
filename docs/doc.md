#  Technical Documentation for Password Generator

## Introduction

This code generates a password for the user. The user can choose the length of the password, whether they want duplicates of characters in the password, and the character set from which the password is generated. The password generation is done through the use of the `random` module from Python Standard Library.

## Code Details

### Import

The code starts with the import of the `random` module. This module provides functions for generating pseudo-random numbers, which will be used to randomly select characters for the password.

```python
import random
```

### Functions

The code defines four functions: `duplication_length()`, `select_length()`, `generate_no_duplication()`, and `generate_with_duplication()`.

#### `duplication_length()`

This function prompts the user to select the length of the password. The minimum length is 4 characters and the maximum length is the number of characters in the `pass_base` list. If the user selects a length that is not within the acceptable range, an error message will be displayed and the function will continue to prompt the user until a valid length is entered.


```python
def duplication_length():
    while True:
        print("Выберите длину пароля. Минимальная длина 4 символа, максимальная длина", len(pass_base), "символов")
        pass_length = int(input("Длина: "))
        if pass_length > len(pass_base) or pass_length < 4:
            print("Неверно выбрана длина пароля! ")
        else:
            return pass_length
```

#### `select_length()`

This function is similar to `duplication_length()`, but the maximum length is 128 characters. If the user selects a length that is not within the acceptable range, an error message will be displayed and the function will continue to prompt the user until a valid length is entered.


```python
def select_length():
    while True:
        print("Выберите длину пароля. Минимальная длина 4 символа, максимальная длина 128 символов")
        pass_length = int(input("Длина: "))
        if pass_length > 128 or pass_length < 4:
            print("Неверно выбрана длина пароля! ")
        else:
            return pass_length
```


##  generate_no_duplication()

This function generates a password without duplicates. It takes two arguments, `pass_length` and `pass_base`, which are the length of the password and the list

## generate_with_duplication()

The `generate_with_duplication()` function generates a password that can have duplicate characters. It takes two parameters:

1.  `pass_length`: An integer that represents the length of the password to be generated.
2.  `pass_base`: A list of characters that will be used to generate the password.

The function starts by creating an empty list `user_password`. It then enters a for loop that runs `pass_length` number of times. In each iteration, it selects a random character from `pass_base` and converts it from an integer to a Unicode character using the `chr()` function. The character is then appended to the `user_password` list.

Finally, the `user_password` list is joined together into a single string using the `join()` method, and the resulting password is printed to the console.

## Conclusion

In conclusion, the code is a password generator that has two different functions for generating passwords with and without duplicates. The code uses the `random` module to select random characters from a list to generate the password. The generated password can be customized by changing the list of characters used to generate the password.
