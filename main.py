from models.customer import Customer
from models.account import Account
from datetime import date

def main():
    try:

        # Creaet Cusotomers
        cust1 = Customer("billa", "bong", date(2021,6,3), "Berlin")
        cust2 = Customer("john", "chacha", date(2014,5,8), address="Dresden")

        # Display Account Details
        print("Customer Details:")
        print(cust1.get_customer_details())
        print(cust2.get_customer_details())

        # Create account for customer 1
        acc1 = Account(cust1)
        acc2 = Account(cust1)
        print("Accounts are created for customer 1")

        # Create account for customer 2
        acc3 = Account(cust2)
        acc4 = Account(cust2)
        print("Accounts are created for customer 2")

        # Create dummy transactions
        acc1.deposit(1000)
        print("Deposited $1000 in account 1")

        acc1.transfer(acc3, 300)
        print("Transactioned happened from acc1 to acc3")

        acc1.transfer(acc4, 200)
        print("Transactioned happened from acc1 to acc4")

        acc1.transfer(acc2, 200)
        # print("Transactioned happened from acc1 to acc2")

        print("\nAccount 1 Transactions:")
        acc1.show_transactions()

        print("\nAccount 2 Transactions:")
        acc2.show_transactions()
       
        # print("\nAccount 3 Transactions:")
        # acc3.show_transactions()
        
        # print("\nAccount 4 Transactions:")
        # acc4.show_transactions()

        # Attempt to exceed account limit
        # acc3 = Account(cust1)
        # acc4 = Account(cust1)
        # acc5 = Account(cust1)
        # acc6 = Account(cust1)  # This should raise error
    
    except ValueError as e:
        print(f"Error: e")

if __name__== "__main__":
    main()