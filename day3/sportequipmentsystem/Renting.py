import datetime as dt
# Write initial data to the file
# equipment rentening tracking
# Function to write initial data to the file
def update_barrow():
    try:
        with open('rentaldatabase.txt','r')as ch:
            data = ch.read().strip().split('|')
            usn = input("Enter USN: ")
            for i in data:
                if usn not in i:
                    with open("rentaldatabase.txt", 'a') as fs:
                        
                        eid = input("Enter the equipment ID: ")
                        name = input("Enter name: ")
                        time_barrow = dt.datetime.now().time() # we can change the time() to date() also
                        s = f"{usn}|{eid}|{name}|{time_barrow}"
                        fs.write(s)
                        print("Barrow sucessfull !")
                else:
                    print("usn is already exist ")
                    return 
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update the name based on eid
def update_return():
    try:

         with open('rentaldatabase.txt','r')as ch:
            data = ch.read().strip().split('|')
            eid = input("Enter the equipment ID: ")
            for i in data:
                if eid in i:               
                    with open('rentaldatabase.txt', 'r') as fn:
                        lines = fn.readlines()  # Read all lines
                    #f"{usn}|{eid}|{name}|{time_barrow}" for position check                 
                    updated_lines = []
                    for line in lines:
                        parts = line.strip().split('|')
                        if parts[1] == eid:
                            parts[4] = str(dt.datetime.now().time()) # Update the name
                        updated_lines.append("|".join(parts) + '\n')

                    with open('rentaldatabase.txt', 'w') as fn:
                        fn.writelines(updated_lines)  # Write updated lines back to the file
                else:
                    print("eid is not exist :")
                    return
    except Exception as e:
        print(f"An error occurred: {e}")




            



