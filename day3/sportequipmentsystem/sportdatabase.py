# Write initial data to the file
# sport equipment details
def display():
    try:  
        with open('sportequipment.txt','r') as file:
            data =file.readlines()
            print("{eid}|{name}|{condition}|{status}")
            for i in data:
                print(i , end=' |')
        return 
    except Exception as e:
        print(e)
        return

# Function to write initial data to the file
def appendcontent():
    try:
        with open("sportequipment.txt", 'a') as fs:
            eid = input("Enter the equipment ID: ")
            name = input("Enter equipment name: ")
            condition = input("enter the condition of Equipment :")
            status = input("enter the status of equipment :")            
            s = f"{eid}|{name}|{condition}|{status}\n"
            fs.write(s)
            return
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update the name based on eid
def update_status():
    
    try:
        with open('sportequipment.txt', 'r') as fn:
            lines = fn.readlines()  # Read all lines
        # print("1.eid 2.name 3.condition 4.status")
        # change = int(input)
        eid_to_find = input("Enter the eid to update: ")
        new_name = input("update the equipment status A/NA: ")
        updated_lines = []
        for line in lines:
            parts = line.strip().split('|')
            if parts[0] == eid_to_find:
                parts[3] = new_name  # Update the status
            updated_lines.insert(4,'|'.join(parts) + '\n')
        with open('sportequipment.txt', 'w') as fn:
            fn.writelines(updated_lines)  # Write updated lines back to the file
            return
    except Exception as e:
            print(f"An error occurred: {e}")
        


def delete():
    try:
        with open('sportequipment.txt', 'r') as fn:
            lines = fn.readlines()  # Read all lines

        eid_to_remove = input("Enter the eid to remove: ")
        if eid_to_remove in lines:
                
            updated_lines = []
            for line in lines:
                parts = line.strip().split('|')
                if parts[0] != eid_to_remove:
                    updated_lines.append(line)  # Keep the line if eid does not match

            with open('sportequipment.txt', 'w') as fn:
                fn.writelines(updated_lines)  # Write updated lines back to the file
                return
        else:
            print("Entered eid is not exist !")
            return
        
    except Exception as e:
        print(f"An error occurred: {e}")


            


