# Password Generator

A password generator that creates random passwords without or with duplication of characters.

## Usage

The user is prompted to choose the length of the password between 4 and 128 characters, and to select if they want the characters to be unique or repeat. The generated password will then be displayed in the console.

## Requirements

-   Python 3.x

## Dependencies

-   random

## Functionality

-   `duplication_length()`: Prompts the user to choose the length of the password between 4 and the length of the character list.

-   `select_length()`: Prompts the user to choose the length of the password between 4 and 128 characters.

-   `generate_no_duplication(pass_length, pass_base)`: Generates a password of the selected length without duplication of characters.

-   `generate_with_duplication(pass_length, pass_base)`: Generates a password of the selected length with the possibility of duplicated characters.

## Usage

To run this code, simply run the following command in the terminal:

`python main.py`

The chatbot will start and will be available for use.
