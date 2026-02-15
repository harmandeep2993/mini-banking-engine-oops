from datetime import date
class Customer:
    """
    Customer class represents and deal with creating unique banking customer.

    This ensures that each customers is uniquely identified using 
    first name, last name and date of birth.
    It will generate unique customer id and prevent any creation of duplication of customer record.
    Maintains all the accounts owned by the customer(Maximum 5 accounts/customer).
    
    Inshort, this class handles identity and owership management only.   
    
    """
    # Define class objects
    customer_registry = set()
    c_series = 70000           # Number series for assigning 6 digit customer unique ID.
    max_accounts = 5            # Maximum limit of accounts for a customer
    customers_id= []

    def __init__(self, fname:str, lastname:str, dob:date, address: str):
        self.identity = (fname, lastname, dob)
        if self.identity in Customer.customer_registry:
            raise ValueError ("Customer already exits.")

        # Register new customer
        Customer.customer_registry.add(self.identity)

        # Generate unique id
        Customer.c_series +=1
        self.c_id = Customer.c_series
        Customer.customers_id.append(self.c_id)
        
        # Store Customer information
        self.fname = fname
        self.lastname = lastname
        self.dob = dob
        self.address = address
        
        # Empty Account list to store accoount
        # assoicated to a customer
        self.accounts = []
    
    def add_account(self, account):
        # Allow only 5 accounts creation to customer
        if len(self.accounts)>= Customer.max_accounts:
            raise ValueError("Maximum account limit (5) reached.")
        self.accounts.append(account)
    
    def get_accounts(self):
        return self.accounts

    def get_customer_details(self):
        return {
            "Customer ID" : self.c_id,
            "Name" : f"{self.fname} {self.lastname}",
            "Date of Birth" :self.dob,
            "Address" : self.address,
            "Number of accounts" : len(self.accounts),
            "Account Numbers" : self.get_accounts()
        }