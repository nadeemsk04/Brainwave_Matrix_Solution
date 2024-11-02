# ATM Interface System

This is a simple ATM interface system implemented in Python. The program allows users to perform basic banking transactions, such as viewing their account balance, withdrawing money, depositing money, changing their PIN, and quitting the application.

## Features

Login with PIN: Users can log into their account using a 4-digit ATM PIN. They have 3 attempts to enter the correct PIN before the system locks the account.

View Statement: Users can view their current account balance.

Withdraw Money: Users can withdraw money from their account, provided they have sufficient funds, and the withdrawal amount is in multiples of 10.

Deposit Money: Users can deposit money into their account, provided the deposit amount is in multiples of 10.

Change PIN: Users can change their ATM PIN by entering a new 4-digit number, different from their current PIN.

Quit the Program: Users can exit the ATM interface at any time by selecting the quit option.

## Program Flow
Welcome Screen: The program begins by welcoming the user and prompting them to enter their 4-digit PIN. Users have three attempts to enter the correct PIN. If the correct PIN is entered, they are logged into the system. Otherwise, the system locks the account after three failed attempts.

Main Menu: Once logged iSn, the user is presented with a menu of options:

View Statement (S): Displays the user’s current balance.
Withdraw (W): Prompts the user to enter an amount to withdraw. The withdrawal is successful only if the amount is a multiple of 10 and does not exceed the current balance.
Deposit (D): Prompts the user to enter an amount to deposit. The deposit is accepted only if the amount is a multiple of 10.
Change PIN (P): Allows the user to change their ATM PIN. The user must enter the new PIN twice for confirmation, and it must be a 4-digit number different from the old PIN.
Quit (Q): Exits the program.

Error Handling: The program includes error handling for several scenarios:

The PIN must be exactly 4 digits.
Withdrawal and deposit amounts must be multiples of 10.
The user cannot withdraw more money than is available in their account.
The new PIN must be confirmed correctly to change it.
Code Breakdown
User Data: The users, pins, and amounts lists store the usernames, PINs, and bank balances, respectively.
Login Process: The user is prompted to enter their ATM PIN. The system checks if the PIN is valid (a 4-digit number and matches an existing user). If correct, the user proceeds to the main menu.

## Main Menu Options:
Main Menu Options: Users can select from five options:
View account statement.
Withdraw money.
Deposit money.
Change their PIN.
Quit the system.
Validation: The system validates inputs for correct PIN length, multiples of 10 for cash transactions, and matching PIN entries when changing the PIN.


## Requirements
This program requires a basic Python setup and uses only built-in libraries. It is compatible with Python 3.
