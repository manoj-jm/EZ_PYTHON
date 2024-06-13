import datetime as dt
# Write initial data to the file
# equipment rentening tracking
# Function to write initial data to the file
def update_barrow():
    try:
        with open("rentaldatabase.txt", 'a') as fs:
            usn = input("Enter USN: ")
            eid = input("Enter the equipment ID: ")
            name = input("Enter name: ")
            time_barrow = dt.datetime.now().time() # we can change the time() to date() also
            s = f"{usn}|{eid}|{name}|{time_barrow}"
            fs.write(s)
            print("Barrow sucessfull !")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update the name based on eid
def update_return():
    try:
        with open('rentaldatabase.txt', 'r') as fn:
            lines = fn.readlines()  # Read all lines

        eid_to_find = input("Enter the eid to update: ")
       
        updated_lines = []
        for line in lines:
            parts = line.strip().split('|')
            if parts[1] == eid_to_find:
                parts[4] = str(dt.datetime.now().time()) # Update the name
            updated_lines.append("|".join(parts) + '\n')

        with open('rentaldatabase.txt', 'w') as fn:
            fn.writelines(updated_lines)  # Write updated lines back to the file
    except Exception as e:
        print(f"An error occurred: {e}")




            



