import pandas as pd
import os

# Load existing data if available  !!!
# if it  exists.
if os.path.exists("contacts.csv"):
    df = pd.read_csv("contacts.csv")
else:
    #make  if not exists
    df = pd.DataFrame(columns=["Name", "Address", "Number"])

def display_contacts():
    if df.empty:
        print("\nNo contacts found.\n")
    else:
      #  print(df_contacts)
        print("\nContacts List:\n", df.to_string(index=True), "\n") #index = false :removes leftmost column showing indices

def add_contact():
    global df  # since it is defined outside the function : so GLOBAL is used.
    name = input("Enter name: ")
    address = input("Enter address: ")
    number = input("Enter number: ")
    
    if not validate_number(number):
        print("!! wrong number ,enter again !!")
        number_1 = input("Enter number: ")
    else:
        number_1 = number


    '''
    new_row = pd.DataFrame([[name,address,number]])
    new_column = df["new_column"] # new row goes in the same orderas previous.
    df = pd.concat([df,new_row],ignore_index = True) # ignore_index removes the duplicate indices. 
    '''
    df.loc[len(df)] = [name, address, number_1]
    print("\nContact added successfully!\n")

# to  check the length
def validate_number(number):
    return number.isdigit() and len(number) >= 10

def update_contact():
    global df
    name = input("Enter the name to update: ")
    if name in df["Name"].values:
        new_name = input("Enter new name : ")
        new_address = input("Enter new address : ")
        new_number = input("Enter new number : ")

        if not validate_number(new_number):
            print("!! wrong number ,enter again !!")
            number_1 = int(input("Enter number: "))
        else:
            number_1 = new_number

        if new_name:
            df.loc[df["Name"] == name, "Name"] = new_name  #df.loc[ condition , "Column" ] = value
        if new_address:
            df.loc[df["Name"] == (new_name if new_name else name), "Address"] = new_address
        if new_number:
            df.loc[df["Name"] == (new_name if new_name else name), "Number"] = number_1

        print("\nContact updated successfully!\n")
    else:
        print("\nContact not found.\n")

def delete_contact():
    '''
    With inplace=False (default):

    A new DataFrame is returned, original stays the same.

    With inplace=True:

    The operation is applied directly on the original DataFrame, and nothing is returned (it becomes None).
   '''
    global df
    name = input("Enter the name to delete: ")
    if name in df["Name"].values:
        df.drop(df[df["Name"] == name].index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("\nContact deleted successfully!\n")
    else:
        print("\nContact not found.\n")

def save_data():
    df.to_csv("contacts.csv", index=False) # to save in cse file.

#in memory df existing.
#contacts_df = pd.read_csv('contacts.csv')

def clear_history():
    global df

    #to clear csv.
    empty_df = pd.DataFrame(columns=['Name','Address','Number'])
    empty_df.to_csv('contacts.csv', index=False)
    #to clear in terminal.
    df = empty_df.copy()

'''
def export_as_excel():

    global df

    df.to_excel('contacts.xlsx', index=False)
    print("\n Contacts exported as Excel successfully!\n")
'''

# Menu loop
while True:
    print(" Contact Manager")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Save & Exit")
    print("6. clear history")

    choice = input("Enter choice: ")

    if choice == "1":
        display_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        save_data()
        # export_as_excel()
        print("\nContacts saved!\n")
        break
    elif choice == "6":
        clear_history()
        print("done")
    else:
        print("\nInvalid choice, please try again.\n")

    