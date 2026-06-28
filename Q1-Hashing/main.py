from medicine import Medicine
from hash_table import MedicineHashTable
from performance_test import performance_comparison


def load_sample_data(hash_table, medicine_list):
    """Loads predefined medicine records into both storage structures."""

    sample_medicines = [
        Medicine("MED101", "Antibiotics", "Tablet", 12.00, 120),
        Medicine("MED102", "Panadol", "Tablet", 11.90, 100),
        Medicine("MED103", "Cough Syrup", "Syrup", 12.50, 40),
        Medicine("MED104", "Vitamin C", "Supplement", 18.00, 70),
        Medicine("MED105", "Ibuprofen", "Tablet", 7.20, 95),
        Medicine("MED106", "Ryzodeg Insulin", "Prescription Drug", 85.00, 35),
        Medicine("MED107", "Fish Oil", "Supplement", 25.00, 50),
        Medicine("MED108", "Paracetamol", "Tablet", 9.60, 60),
        Medicine("MED109", "Multivitamin", "Supplement", 21.50, 45),
        Medicine("MED110", "Eye Drops", "Liquid", 14.30, 30)
    ]

    for medicine in sample_medicines:
        hash_table.insert(medicine)
        medicine_list.append(medicine)


def add_medicine(hash_table, medicine_list):
    """Allows the user to add a new medicine."""

    print("\n========== ADD MEDICINE ==========")

    medicine_id = input("Enter medicine ID: ").upper()

    if hash_table.search(medicine_id) is not None:
        print("Medicine ID already exists.")
        return

    name = input("Enter medicine name: ")
    category = input("Enter category: ")

    try:
        price = float(input("Enter price (RM): "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Price must be a decimal number and quantity must be a whole number.")
        return

    new_medicine = Medicine(medicine_id, name, category, price, quantity)

    if hash_table.insert(new_medicine):
        medicine_list.append(new_medicine)
        print("Medicine added successfully.")


def search_medicine(hash_table):
    """Allows the user to search for a medicine using its ID."""

    print("\n========== SEARCH MEDICINE ==========")

    medicine_id = input("Enter medicine ID to search: ").upper()
    medicine = hash_table.search(medicine_id)

    if medicine is None:
        print("Medicine not found.")
    else:
        print("Medicine found:")
        print(medicine)


def update_medicine_quantity(hash_table):
    """Allows the user to update a medicine stock quantity."""

    print("\n========== UPDATE MEDICINE QUANTITY ==========")

    medicine_id = input("Enter medicine ID: ").upper()

    try:
        new_quantity = int(input("Enter new quantity: "))

        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return

        hash_table.edit_quantity(medicine_id, new_quantity)

    except ValueError:
        print("Quantity must be a whole number.")


def delete_medicine(hash_table, medicine_list):
    """Allows the user to delete a medicine from both structures."""

    print("\n========== DELETE MEDICINE ==========")

    medicine_id = input("Enter medicine ID to delete: ").upper()
    medicine = hash_table.search(medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    if hash_table.delete(medicine_id):
        medicine_list.remove(medicine)


def display_menu():
    """Displays the main menu."""

    print("\n==============================================")
    print("       PHARMACY INVENTORY MANAGEMENT SYSTEM")
    print("==============================================")
    print("1. Display hash table")
    print("2. Add medicine")
    print("3. Search medicine")
    print("4. Update medicine quantity")
    print("5. Delete medicine")
    print("6. Compare search performance")
    print("7. Exit")


def main():
    """Runs the Pharmacy Inventory Management System."""

    hash_table = MedicineHashTable(size=17)
    medicine_list = []

    load_sample_data(hash_table, medicine_list)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            hash_table.display()

        elif choice == "2":
            add_medicine(hash_table, medicine_list)

        elif choice == "3":
            search_medicine(hash_table)

        elif choice == "4":
            update_medicine_quantity(hash_table)

        elif choice == "5":
            delete_medicine(hash_table, medicine_list)

        elif choice == "6":
            performance_comparison(hash_table, medicine_list)

        elif choice == "7":
            print("Thank you for using the Pharmacy Inventory Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()



