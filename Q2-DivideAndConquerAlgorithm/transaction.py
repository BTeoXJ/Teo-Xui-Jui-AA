class Transaction:
    """Represents one customer transaction in an online shopping system."""

    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return (
            f"{self.transaction_id:<8} | "
            f"{self.customer_name:<18} | "
            f"{self.product_name:<20} | "
            f"RM {self.amount:<8.2f} | "
            f"{self.transaction_date}"
        )



