# Decorator to handle input errors gracefully
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter a valid phone number"
        except IndexError:
            return "Invalid number of arguments. Please check usage."
        except KeyError:
            return "Contact not found. Please check the name."
    return wrapper

# Function to add a contact to the contacts dictionary
@input_error
def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."

# Function to change the phone number of an existing contact
@input_error
def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Function to show the phone number of a specific contact
@input_error
def show_phone(username, contacts):
    return f"{username}'s phone number is: {contacts[username]}"

# Function to show all contacts and their phone numbers
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    else:
        result = "All contacts:\n"
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result.strip()  # Strip trailing newline

# Main function to handle user input and interact with the contact book
if __name__ == "__main__":

    def main():
        contacts = {}

        print("Welcome to the assistant bot!")

        while True:
            user_input = input("Enter a command: ").strip().lower()
            command, *args = user_input.split()

            if command in ["close", "exit"]:
                print("Goodbye!")
                break

            elif command == "add":
                if len(args) == 2:
                    username, phone = args
                    print(add_contact(username, phone, contacts))
                else:
                    print("Invalid command. Usage: add username phone")

            elif command == "change":
                if len(args) == 2:
                    username, phone = args
                    print(change_contact(username, phone, contacts))
                else:
                    print("Invalid command. Usage: change username phone")

            elif command == "phone":
                if len(args) == 1:
                    username = args[0]
                    print(show_phone(username, contacts))
                else:
                    print("Invalid command. Usage: phone username")

            elif command == "all":
                print(show_all(contacts))

            else:
                print("Invalid command")

    main()
