def bank_chatbot(first_time=True):

    if first_time:
        print("Welcome to Bank Balance Chatbot!")
        print("You can ask about balance, deposit, withdraw, account type, loans, and ATM services.")
        print("Type bye to exit.\n")

    # Initial bank balance
    balance = 50000

    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot: Thank you for visiting our bank. Have a great day!")

    elif user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! How can I help you today?\n")
        bank_chatbot(False)

    elif "balance" in user:
        print(f"Bot: Your current account balance is Rs. {balance}\n")
        bank_chatbot(False)

    elif "deposit" in user:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Bot: Rs. {amount} deposited successfully.")
        print(f"Bot: Updated balance is Rs. {balance}\n")
        bank_chatbot(False)

    elif "withdraw" in user:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"Bot: Rs. {amount} withdrawn successfully.")
            print(f"Bot: Remaining balance is Rs. {balance}\n")
        else:
            print("Bot: Insufficient balance.\n")

        bank_chatbot(False)

    elif "account" in user:
        print("Bot: We offer Savings, Current, and Fixed Deposit accounts.\n")
        bank_chatbot(False)

    elif "loan" in user:
        print("Bot: We provide Home Loan, Car Loan, Education Loan, and Personal Loan services.\n")
        bank_chatbot(False)

    elif "atm" in user:
        print("Bot: ATM services are available 24/7 across India.\n")
        bank_chatbot(False)

    else:
        print("Bot: Sorry, I didn't understand.\n")
        bank_chatbot(False)


if __name__ == "__main__":
    bank_chatbot()