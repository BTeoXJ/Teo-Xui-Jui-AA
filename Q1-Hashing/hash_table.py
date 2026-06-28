class MedicineHashTable:
    """Hash table that uses linear probing to resolve collisions."""

    def __init__(self, size=17):
        self.size = size
        self.buckets = [None] * size
        self.count = 0

    def hash_function(self, medicine_id):
        """Converts a medicine ID into a valid bucket index."""
        total = 0

        for character in medicine_id:
            total += ord(character)

        return total % self.size

    def insert(self, medicine):
        """Inserts a medicine object into the hash table."""

        if self.count == self.size:
            print("Hash table is full. Cannot insert more medicines.")
            return False

        index = self.hash_function(medicine.medicine_id)
        original_index = index

        while self.buckets[index] is not None:
            if self.buckets[index].medicine_id == medicine.medicine_id:
                print("Medicine ID already exists. Insertion cancelled.")
                return False

            # Linear probing: move to the next bucket.
            index = (index + 1) % self.size

            if index == original_index:
                print("Hash table is full.")
                return False

        self.buckets[index] = medicine
        self.count += 1
        return True

    def search(self, medicine_id):
        """Searches for a medicine using its medicine ID."""

        index = self.hash_function(medicine_id)
        original_index = index

        while self.buckets[index] is not None:
            if self.buckets[index].medicine_id == medicine_id:
                return self.buckets[index]

            index = (index + 1) % self.size

            if index == original_index:
                break

        return None

    def display(self):
        """Displays all buckets in the hash table."""

        print("\n========== HASH TABLE CONTENTS ==========")

        for index, medicine in enumerate(self.buckets):
            if medicine is None:
                print(f"Bucket {index}: Empty")
            else:
                print(f"Bucket {index}: {medicine}")

    def edit_quantity(self, medicine_id, new_quantity):
        """Updates the stock quantity of an existing medicine."""

        medicine = self.search(medicine_id)

        if medicine is None:
            print("Medicine not found.")
            return False

        medicine.quantity = new_quantity
        print("Medicine quantity updated successfully.")
        return True

    def delete(self, medicine_id):
        """Deletes a medicine record and rebuilds the probing sequence."""

        medicine = self.search(medicine_id)

        if medicine is None:
            print("Medicine not found.")
            return False

        remaining_medicines = []

        for item in self.buckets:
            if item is not None and item.medicine_id != medicine_id:
                remaining_medicines.append(item)

        self.buckets = [None] * self.size
        self.count = 0

        for item in remaining_medicines:
            self.insert(item)

        print("Medicine deleted successfully.")
        return True




