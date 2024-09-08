import os
import csv
import datetime

def title():
    line_1 = "------------------------------"
    title  = " Contact Managemanet System "
    line_2 = "------------------------------"

    print(line_1.center(130))
    print(title.center(130))
    print(line_2.center(130))

class contact_functions:
    contact_fields =["Name ", "Mobile_NO "]
    contact_database = "contacts.csv"
    #contact_data = []

    def create(self):
        self.contact_data = []
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-based systems
            os.system('clear')
        #os.system('cls')
        title()
        print("          Create Contact:    ")
        print("        ---------------------")
        print("")

        # Collect contact details
        for fields in self.contact_fields:
            contact_details = input("        Enter " + fields + ":")
            print("")
            self.contact_data.append(contact_details)

        # Append the current date
        Date = datetime.datetime.today()
        d = Date.strftime("%B %d %Y")
        self.contact_data.append(d)

        # Save the contact to the CSV file
        with open(self.contact_database, 'a', newline='') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

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
            for data1 in read:
                if len(data1) > 0:
                    count += 1
            print("Total Contacts: ", count)
            print('')

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("Contact book is empty, Please create contacts". center(129))
            else:
                for fields in self.contact_fields:
                    print('{0:<10}'.format(fields).center(10), end = "\t\t")
                    print('{0:<10}',format("Date"))
                    print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','----------','-----'))
                    print("")

                    for data in read:
                        for item in data:
                            print('{:<10}'.format(item).center(10), end = "\t\t")
                            print("")

        print("\n")
        input("\t Press enter key to continue..".center(120))
        os.system('cls')

    def search (self):
        os.system('cls')
        title()

        print("search Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match ='false'
        search_value = input("Enter your name: ")
        print("")

        for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10), end = "\t\t")
        print('{0:<10}',format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','----------','-----'))
        print("")

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))
        
        if self.contact_match == 'false':
            print("")
            print("Sorry !, there is no contact by this name".center(129))

        print("")

    def delete(self):
        os.system('cls')
        title()

        print("Delete Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match ='false'
        delete_value = input("Enter your name: ")
        update_list = [] 

        with open(self.contact_database,'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'

        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print("")
                print("Contact is deleted successfully".center(129))
                print("")

        if self.contact_match == 'false':
            print("")
            print("Sorry! data not found".center(129))
            print("")




contact_class = contact_functions()

os.system('cls')
title()

while True:

    print("1. View Contact".center(128))
    print("2. Create Contact".center(130))
    print("3. Search Contact".center(130))
    print("4. Delet Contact".center(128))
    print("5. Exit".center(119))
    print("------------------------------".center(131))
    option = int(input("\t\t\t\t\t\t\tChoose Your Option: "))
    
    #first condition 
    if option == 1:
        contact_class.view() 
        title()

    # #second condition
    if option == 2:
        while True:
            contact_class.create()
            ans = input("\t\t\t\t\t Do you want to create another contact number ? [Y/N]: ")

            if ans =='Y'  or ans =='y':
                continue
            else:
                break

        os.system('cls')
        title()

    #third condition
    if option == 3:
        while True:
            contact_class.search()
            print("")
            ans = input("\t\t\t\t\t Do you want to search another contact number ? [Y/N]: ")

            if ans =='Y'  or ans =='y':
                continue
            else:break 
        os.system('cls')
        title()

    #fourth condition
    if option == 4:
        while True:
            contact_class.delete()
            ans = input("\t\t\t\t\t Do you want to delete another contact number ? [Y/N]: ")

            if ans =='Y'  or ans =='y':
                continue
            else:break 
        os.system('cls')
        title()

    if option == 5:
        # os.system('cls')
        # line_1 = "------------------------------"
        # msg    = "    Thank You for using :)    "
        # line_2 = "------------------------------"

        # print(line_1.center(140))
        # print(msg.center(140))
        # print(line_2.center(140))
        break

    if option > 5 or  option < 1:
        os.system('cls')
        print("Invalid choice. Please choose valid option to proceed further. Thank you :) ") 

        input("Press enter key to continue....".center(140))
        os.system('cls')
        title()