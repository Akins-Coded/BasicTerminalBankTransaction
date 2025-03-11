
# Pseudocode for the Bank account activity
# Step1:- Display Current Balance
# Step2 :- Show User Options: Check Balance, Withdraw, Deposit, Exit.
# Step3 :- User Input:
#     if Check, display Current Balace
#     if deposite, ask for the amount and add to the main balance making new balance.
#     if withdraw, ask for the amount,
#     check if the balance if sufficient and subtract from the balance, then display the new current balance.
# step4 :- Repeat the Step 2 and Step 3
#Initial Balance After Log in


balance = 0
while True:
    # Show Options
    print("Select an Option")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Transfer Money")
    print("4. Exit")

    # User Input
    option = input("Enter Your option Number: ")

    if option == '1':
        print(f"Your Current Balance is: {balance}")
    elif option == '2':
        deposit_amount = int(input('Enter the amount: '))
        balance += deposit_amount
        print(f"You have successfully deposited {deposit_amount} and your new balance is {balance}.")
    elif option == '3':
        withdraw_amount = int(input('Enter the amount: '))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have successfully withdrawn {withdraw_amount} and your new balance is {balance}.")
        else:
            print("You have insufficient funds.")
    elif option == '4':
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid Option")


