import pickle

# Клас для адресної книги
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone, favorite=False):
        contact = {
            "name": name,
            "email": email,
            "phone": phone,
            "favorite": favorite
        }
        self.contacts.append(contact)

    def show_contacts(self):
        if not self.contacts:
            print("Адресна книга порожня.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {'Вибраний' if contact['favorite'] else 'Не вибраний'}")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
        else:
            print("Невірний індекс!")

# Функції для збереження та завантаження даних за допомогою pickle
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# Основний цикл програми
def main():
    book = load_data()

    while True:
        print("\n1. Додати контакт")
        print("2. Показати всі контакти")
        print("3. Видалити контакт")
        print("4. Вихід")
        choice = input("Оберіть дію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            email = input("Введіть email: ")
            phone = input("Введіть телефон: ")
            favorite = input("Позначити як улюблений (y/n): ").lower() == "y"
            book.add_contact(name, email, phone, favorite)
        elif choice == "2":
            book.show_contacts()
        elif choice == "3":
            book.show_contacts()
            try:
                index = int(input("Оберіть номер контакту для видалення: "))
                book.delete_contact(index)
            except ValueError:
                print("Будь ласка, введіть коректне число.")
        elif choice == "4":
            save_data(book)
            print("Дані збережено. Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
