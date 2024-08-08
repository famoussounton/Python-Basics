class Contact:
    def __init__(self):
        self.contacts = []
    
    def add_name(self, nom, num):
        a = [nom, num]
        self.contacts.append(a)
        print(f'Add of {nom} num:{num}')
    
    def show_contact(self):
        print("List of contacts")
        for i in self.contacts:
            print(i)
    
    def recherche(self, nm):
        long = len(self.contacts)
        for i in range (0, long):
            if nm in self.contacts[i]:
                print(f"Voici le contact {self.contacts[i]}")
                return
        print("Le contact n'existe pas")

    def delete(self, nm):
        long = len(self.contacts)
        for i in range(0, long):
            if nm in self.contacts[i]:
                print(f"{self.contacts[i]} has been deleted")
                self.contacts.remove(self.contacts[i])
                return
        print("Le contact n'existe pas")

def main():
    Contactt = Contact()
    l = ["a", "b", "c"]
    print(l)
    print("*******Contacts*******")
    while True:
        print("1- Add contact")
        print("2- Show contact")
        print("3- Research")
        print("4- Remove contact")
        print("5- Quit")

        choic  = input("Enter your option: ")
        choice = int(choic)

        if (choice == 1):
            a= input("Nom:")
            b = input("Num")
            Contactt.add_name(a, b)
        elif (choice == 2):
            Contactt.show_contact()
        elif (choice == 3):
            print("Researching of contact")
            c = input("Name or number: ")
            Contactt.recherche(c)
        elif (choice == 4):
            print("Delete contact")
            d = input("Name or number: ")
            Contactt.delete(d)
        elif (choice == 5):
            return
        else:
            print("Invalide option")

if __name__ == "__main__":
    main()
