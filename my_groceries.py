class GroceriesManager:
    def __init__(self):
        self.groceries_list = []
        self.categories = {'fruits': [], 'vegetables': [], 'dairy': [], 'others': []}

    def add_item(self, item, category):
        if category not in self.categories:
            category = 'others'
        self.categories[category].append(item)
        self.groceries_list.append((item, category))
        print(f'Added {item} to {category}.')

    def remove_item(self, item):
        for cat, items in self.categories.items():
            if item in items:
                items.remove(item)
                self.groceries_list.remove((item, cat))
                print(f'Removed {item} from {cat}.')
                return
        print(f'Item {item} not found in the list.')

    def show_list(self):
        print("\nGrocery list")
        for item, cat in self.groceries_list:
            print(f'- {item}, ({cat})')

    def sort_list_alphabetically(self):
        self.groceries_list.sort(key=lambda x: x[0])
        print("List sorted alphabetically.")

    def sort_list_by_category(self):
        self.groceries_list.sort(key=lambda x: x[1])
        print("List sorted by category.")
        
def main():
    manager = GroceriesManager()

    while True:
        print("\nChoose your option:")
        print("1: Add Item")
        print("2: Remove Item")
        print("3: View list")
        print("4. Sort list alphabetically")
        print("5. Sort list by category")
        print("6: Quit\n")

        choice = input("Choose your option: ")
        if choice == '1':
            item = input("Put your item: ")
            cat = input("Put your cat: ")
            manager.add_item(item, cat)
        elif choice == '2':
            item = input("Put your item: ")
            manager.remove_item(item)
        elif choice == '3':
            manager.show_list()
        elif choice == '4':
            manager.sort_list_alphabetically()
            manager.show_list()
        elif choice == '5':
            manager.sort_list_by_category()
            manager.show_list()
        elif choice == '6':
            print("Exiting the program")
            return
if __name__ == "__main__":
    main()