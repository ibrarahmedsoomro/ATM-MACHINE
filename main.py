import datetime

print("----------------- WELCOME TO UBL ATM MACHINE -----------------")

password = 272829
balance = 80000
transcation = []
attempts = 0
max_attempt = 3

while  attempts < max_attempt :
    pin = int(input("Enter Your ATM Pin: "))

    if pin == password:
        print("Welcome to the ubl bank")

        while True:
            print("\n Select An Option to Perform transcation")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Mini Statment")
            print("5. Exit")

            choice = int(input("Enter your Number for select options"))

            if choice == "1":
                print(f"Your Balance is {balance}")
            elif choice == "2":
                deposit = int(input("Enter you amount for deposit"))
                balance += deposit
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                