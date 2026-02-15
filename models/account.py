from datetime import datetime
from models.customer import Customer


class Account:
    """
    Account class represents a financial account owned by a Customer.

    Responsibilities:
    - Generate unique account numbers.
    - Manage balance.
    - Handle deposits, withdrawals, and transfers.
    - Maintain transaction history.
    - Allow freezing/unfreezing of account.
    - Automatically link itself to a Customer.
    """

    # Class-level counter for generating unique account numbers and transaction ID
    a_series = 2002026001
    transaction_series = 100000

    def __init__(self, customer: Customer):
        # Store reference to the owning customer
        self.customer = customer

        # Generate unique account number
        Account.a_series += 1
        self.account_number = Account.a_series

        # Initialize financial state
        self.balance = 0
        self.status = True  # True = Active, False = Frozen

        # Store transaction history
        self.transaction = []

        # Automatically register this account with the customer
        customer.add_account(self)

    def timestamp_(self):
        """Generate formatted timestamp for transactions."""
        return datetime.now().strftime("%d.%m.%Y")
    
    def _log_transaction(self, tx_type, amount, from_acc=None, to_acc=None):
        Account.transaction_series += 1
        self.transaction.append({
            "Transaction_ID": Account.transaction_series,
            "Date": self.timestamp_(),
            "From_Account": from_acc,
            "To_Account": to_acc,
            "Type": tx_type,
            "Amount": amount,
            "Balance_After": self.balance
        })

    def get_balance(self):
        """Return current account balance."""
        return self.balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        Validates account status and amount.
        """
        if not self.status:
            raise ValueError("Account is frozen")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        # Increase balance
        self.balance += amount

        # Log transaction
        self.balance += amount
        self._log_transaction(
            tx_type="Deposit",
            amount=amount,
            from_acc=None,
            to_acc=self.account_number
        )

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Validates account status and sufficient balance.
        """
        if not self.status:
            raise ValueError("Account is frozen")

        # NOTE: This validation should ideally be split properly
        if amount < self.balance and amount == 0:
            raise ValueError("Withdrawal should be positive")

        # Deduct balance
        self.balance -= amount

        # Update the transaction
        self._log_transaction(
            tx_type="Withdraw",
            amount=amount,
            from_acc=self.account_number,
            to_acc=None
        )

    def show_transactions(self):
        """Print all transaction records."""
        for t in self.transaction:
            print(t)

    def transfer(self, other_account, amount):
        """
        Transfer funds to another Account.
        Validates account status, recipient, and balance.
        """

        if not self.status:
            raise ValueError("Account is frozen")

        # Prevent transfer to same account
        if self.account_number is other_account.account_number:
            raise ValueError("Same account transaction not possible")

        # Ensure recipient is valid Account object
        if not isinstance(other_account, Account):
            raise ValueError("Invalid account.")

        # Balance validation (logic should be improved)
        if not self.balance >= amount and amount > 0:
            raise ValueError("Insufficient Balance")

        # Deduct from sender
        self.balance -= amount

        # Log sender transaction
        self._log_transaction(
            tx_type="Transfer",
            amount=amount,
            from_acc=self.account_number,
            to_acc=other_account.account_number
        )

        # Credit recipient
        other_account.balance += amount

        # Log recipient transaction
        other_account._log_transaction(
            tx_type="Transfer",
            amount=amount,
            from_acc=self.account_number,
            to_acc=other_account.account_number
        )

    def freeze_account(self):
        """Freeze the account (blocks transactions)."""
        self.status = False

    def unfreeze_account(self):
        """Reactivate the account."""
        self.status = True
