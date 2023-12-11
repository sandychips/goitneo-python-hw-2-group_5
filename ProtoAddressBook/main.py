from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                return record_phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        return self.data.get(name)


if __name__ == "__main__":
    # Creating a new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Output of all entries in the book
    for name, record in book.data.items():
        print(record)

    # Find John's record in the address book
    john = book.find("John")
    if john:
        # Find and edit phone for John
        john.edit_phone("1234567890", "1112223333")

        print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

        # Search for a specific phone in the John record
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")  # Output: 5555555555
    else:
        print("John not found in the address book.")

    # Deleting Jane's entry
    book.delete_record("Jane")
