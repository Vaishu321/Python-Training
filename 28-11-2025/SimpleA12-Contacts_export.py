from csv import DictReader
with open ("contacts.csv","r") as contacts_file:
    reader = DictReader(contacts_file)
    for row in reader:
        with open ("contacts_export.txt","a") as contacts:
            contacts.write(f"Name :{row["Names"]:<8}|Phone: {row["Contacts"]}\n") # Left-align name, keep contacts