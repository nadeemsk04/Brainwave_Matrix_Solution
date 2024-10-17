import getpass
import string
import os


# List of users, their PINs, and bank balances.
users = ['user1', 'user2', 'user3']
pins = ['1111', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
n = None  # This will store the logged-in user's index.


print("\n\n**********   Welcome TO The ATM Interface System  **********\n\n")


# Allow user to attempt entering their PIN 3 times.
while count < 3:
    pin = input("\n\nEnter your ATM PIN: ")
    print("\n\n")

    if pin.isdigit() and len(pin) == 4:  # Ensure PIN is a 4-digit number
        if pin in pins:  # Check if the entered PIN exists
            n = pins.index(pin)  # Store the index of the logged-in user
            print(f"*****  Welcome  {users[n]} *****\n")
            break
        else:
            count += 1
            print(f"INVALID PIN. Attempts remaining: {3 - count}")
    else:
        print("PIN must be a 4-digit number.")


if count == 3:
    print("\n\nToo many invalid attempts. Your account is locked.\n\n")
    exit()  # Exit if the user fails 3 attempts.



# Main ATM interface
while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choice: ').lower()
    valid_response = ["s", "w", "d", "p", "q"]

    if response not in valid_response:
        print("\n\nResponse Is Not Valid\n\n")
        continue  # Loop again if an invalid option is chosen

    if response == "s":  # Statement
        print("\n\n")
        print(str.capitalize(users[n]), "You Have", amounts[n], "EURO on Your Account\n")

    elif response == "w":  # Withdraw
        print("\n\n")
        cash_out = int(input("\n\nEnter the Amount You Would Like To Withdraw: "))
        if cash_out % 10 != 0:
            print("\n\nAmount You Want To Withdraw Must Match 10 Euro Notes\n\n")
        elif cash_out > amounts[n]:
            print("You Have Insufficient Balance!\n\n")
        else:
            amounts[n] = amounts[n] - cash_out
            print("\n\nCongratulations! You Successfully Withdrawn Your Amount!\n")
            print("Your New Balance is:", amounts[n], "EURO\n\n")

    elif response == "d":  # Deposit
        print("\n\n")
        cash_in = int(input("Enter Amount You Want To Deposit: "))
        if cash_in % 10 != 0:
            print("\n\nAmount You Want To Deposit Must Match 10 EURO Notes\n")
        else:
            amounts[n] = amounts[n] + cash_in
            print("\n\nYour New Balance is", amounts[n], "EURO\n\n")

    elif response == "p":  # Change PIN
        print("\n\n")
        new_pin = str(getpass.getpass("Enter Your New ATM PIN: "))
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = str(getpass.getpass("Confirm Your New ATM PIN: "))
            if new_ppin == new_pin:
                pins[n] = new_pin  # Update the user's PIN
                print("\n\nNew PIN Has Been Saved\n")
            else:
                print("\n\nPIN Does Not Match\n")
        else:
            print("\n\nNew PIN Must Consist Of 4 Digits Only And Must Be Different From The Previous PIN\n")

    elif response == "q":  # Quit
        print("\n\nThank you for using our ATM. Goodbye!\n\n")
        exit()

