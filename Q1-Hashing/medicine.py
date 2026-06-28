class Medicine:
    """Represents one medicine product in the pharmacy."""

    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"{self.medicine_id:<8} | "
            f"{self.name:<20} | "
            f"{self.category:<12} | "
            f"RM {self.price:<7.2f} | "
            f"Stock: {self.quantity}"
        )




