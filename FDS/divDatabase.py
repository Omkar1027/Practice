import pandas as pd

def n_email(database,name):
     for r in range(len(database)):
         n=database.loc[r,'Name']
         if name.lower() == n.lower():
            print(database.loc[r,'Email'])

def n_contact_no(database,name):
     for r in range(len(database)):
         n=database.loc[r,'Name']
         if name.lower() == n.lower():
             print(database.loc[r,'Contact_No'])

def r_email(database,roll):
     for r in range(len(database)):
         temp_roll=database.loc[r,'Roll_No']
         if int(roll) == int(temp_roll):
            print(database.loc[r,'Email'])

def r_contact_no(database,roll):
     for r in range(len(database)):
         temp_roll=database.loc[r,'Roll_No']
         if int(roll) == int(temp_roll):
             print(database.loc[r,'Contact_No'])



if __name__ == '__main__':
    list_data = [
    ["Sagar", "Jadhav", 8291076619, 24, "2023.sagar.jadhav@ves.ac.in"],
    ["Aary", "Jain", 8452976601, 25, "2023.aary.jain@ves.ac.in"],
    ["Guneet", "Jaisinghania", 8855880544, 26, "2023.guneet.jaisinghania@ves.ac.in"],
    ["Omkar", "Kadam", 9082215356, 27, "2023.omkar.kadam@ves.ac.in"],
    ["Lakhan", "Karani", 9579221424, 28, "2023.lakhan.karani@ves.ac.in"],
    ["Kaustubh", "Karnik", 8450919330, 29, "2023.kaustubh.karnik@ves.ac.in"],
    ["Jiya", "Kathpal", 8108290001, 30, "2023.jiya.kathpal@ves.ac.in"],
    ["Prativa", "Koturu", 9321088439, 31, "2023.prativa.koturu@ves.ac.in"],
    ["Nikhil", "Lalchandani", 8483817600, 32, "2023.nikhil.lalchandani@ves.ac.in"],
    ["Anuj", "Lolam", 9004306173, 33, "2023.anuj.lolam@ves.ac.in"],
    ["Milap", "Mahapatra", 9082612386, 34, "2023.milap.mahapatra@ves.ac.in"]
]

    list_column = ['Name', 'Surname', 'Contact_No', 'Roll_No', 'Email']

    database=pd.DataFrame(list_data,columns=list_column)

    print(database)

    # function to get email id by name 
    name=input("Enter name to get email ID: ")
    n_email(database,name)

    # function to get contact number by name 
    name=input("Enter name to get contact number: ")
    n_contact_no(database,name)

    # function to get contact number by roll 
    roll=input("Enter roll to get email ID: ")
    r_email(database,roll)

    # function to get contact number by name 
    roll=input("Enter roll to get contact number: ")
    r_contact_no(database,roll)

