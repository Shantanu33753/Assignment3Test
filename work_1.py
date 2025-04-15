"""
work1 -- staff_info
Author: Shantanu Thakur
"""

def staff_info():
    requisition_id = []   #For every diferent name shows diferent requisition ids
    
    count = 10000

    while True:
        date = input("Enter Date (DD-MM-YYYY): ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")

        count += 1
        requisition_id = count   #calculte 
        
        more_entries = input("Do you want to add more entries? (yes/no): ")
        if more_entries.lower() != 'yes':  #this one shows enrtries on function according to lower
            break
        else:
            
            print(f"\n---Printing Staff Information:---")
            print(f"Date: {date} ")
            print(f"Staff ID: {staff_id}")
            print(f"Staff Name: {staff_name}")
            print(f"Requisition ID: {requisition_id}\n")

    return date, staff_id, staff_name, requisition_id  # Returning the obtained data to here at the end

