


import os
import csv
import datetime

def title():
    line_1 = "------------------------------"
    title  = " Contact Management System "
    line_2 = "------------------------------"

    print(line_1.center(130))
    print(title.center(130))
    print(line_2.center(130))

class ContactFunctions:
    contact_fields = ["Name", "Mobile_NO"]
    contact_database = "contacts.csv"

    def create(self):
        self.contact_data = []
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-based systems
            os.system('clear')
        
        title()
        print("          Create Contact:    ")
        print("        ---------------------")
        print("")

        # Collect contact details
        for field in self.contact_fields:
            contact_details = input("        Enter " + field + ": ")
            print("")
            self.contact_data.append(contact_details)

        # Append the current date
        date = datetime.datetime.today()
        d = date.strftime("%B %d %Y")
        self.contact_data.append(d)

        # Save the contact to the CSV file
        with open(self.contact_database, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.contact_data)

        print("")
        print("Contact is created successfully".center(129))
        print("\n")

    def view(self):
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-based systems
            os.system('clear')
        
        title()

        print("Contacts: ".center(10))
        print("---------".center(10))
        print("")

        count = 0
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    count += 1
            print("Total Contacts: ", count)
            print('')

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("Contact book is empty, Please create contacts".center(129))
            else:
                # Header
                header = self.contact_fields + ["Date"]
                print('{:<20} {:<20} {:<20}'.format(*header))
                print('{:<20} {:<20} {:<20}'.format('-' * 20, '-' * 20, '-' * 20))
                
                # Data Rows
                for data in read:
                    if len(data) > 0:
                        print('{:<20} {:<20} {:<20}'.format(*data))
    
        print("\n")
        input("\t Press enter key to continue..".center(120))
        os.system('cls')

    def search(self):
        os.system('cls')
        title()

        print("Search Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match = False
        search_value = input("Enter the name to search: ")
        print("")

        for field in self.contact_fields:
            print('{0:<20}'.format(field), end="")
        print('{0:<20}'.format("Date"))
        print('{:<20} {:<20} {:<20}'.format('-' * 20, '-' * 20, '-' * 20))
        
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = True
                        print('{:<20} {:<20} {:<20}'.format(data[0], data[1], data[2]))
        
        if not self.contact_match:
            print("Sorry, there is no contact by this name".center(129))

        print("")

    def delete(self):
        os.system('cls')
        title()

        print("Delete Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match = False
        delete_value = input("Enter the name to delete: ")
        update_list = [] 

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = True

        if self.contact_match:
            with open(self.contact_database, 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print("Contact is deleted successfully".center(129))
        else:
            print("Sorry, data not found".center(129))
        print("")


# Main program loop
contact_class = ContactFunctions()

os.system('cls')
title()

while True:
    print("1. View Contact".center(128))
    print("2. Create Contact".center(130))
    print("3. Search Contact".center(130))
    print("4. Delete Contact".center(128))
    print("5. Exit".center(119))
    print("------------------------------".center(131))
    option = int(input("\t\t\t\t\t\t\tChoose Your Option: "))
    
    if option == 1:
        contact_class.view() 
        title()

    if option == 2:
        while True:
            contact_class.create()
            ans = input("\t\t\t\t\t Do you want to create another contact? [Y/N]: ")

            if ans.lower() == 'y':
                continue
            else:
                break

        os.system('cls')
        title()

    if option == 3:
        while True:
            contact_class.search()
            ans = input("\t\t\t\t\t Do you want to search another contact? [Y/N]: ")

            if ans.lower() == 'y':
                continue
            else:
                break 
        os.system('cls')
        title()

    if option == 4:
        while True:
            contact_class.delete()
            ans = input("\t\t\t\t\t Do you want to delete another contact? [Y/N]: ")

            if ans.lower() == 'y':
                continue
            else:
                break 
        os.system('cls')
        title()

    if option == 5:
        print("Thank you for using the Contact Management System :)".center(130))
        break

    if option > 5 or option < 1:
        os.system('cls')
        print("Invalid choice. Please choose a valid option to proceed further. Thank you :)") 
        input("Press enter key to continue....".center(140))
        os.system('cls')
        title()
